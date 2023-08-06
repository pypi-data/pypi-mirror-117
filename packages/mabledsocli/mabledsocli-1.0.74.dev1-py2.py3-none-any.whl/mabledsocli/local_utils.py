import os
import re
from .contexts import Contexts
from .logger import Logger
from .stages import Stages
from mabledsocli.config import Configs
from mabledsocli.file_utils import *
from mabledsocli.exceptions import DSOException
from mabledsocli.dict_utils import *


def encode_local_path(stage, key):
    result = Stages.normalize(stage)
    if key:
        result = os.path.join(result, key)
    return result.replace('/', os.sep)


def decode_local_path(path):
    """
        path is in the form of [/]stage/env_no/[key]
    """
    parts = path.split(os.sep)
    if not parts[0]: parts.pop(0)
    stage = f"{parts[0]}/{parts[1]}"
    key = os.sep.join(parts[2:]) if len(parts) > 2 else None
    return stage, key


def get_local_path(stage, key=None, path_prefix=None):
    return path_prefix + encode_local_path(stage, key)


def get_context_hierachy_local_paths(stage, path_prefix=None, uninherited=False, reverse=False):
    stage = Stages.normalize(stage)
    result = []
    if uninherited:
        result.append(get_local_path(stage, path_prefix=path_prefix))
    else:
        ### Add the application context: /project/application/default/0
        result.append(get_local_path('default/0', path_prefix=path_prefix))
        if not stage is None and not Stages.is_default(stage):
            ### Add the project stage context: /project/application/stage/0
            result.append(get_local_path(Stages.get_default_env(stage), path_prefix=path_prefix))
            ### Add the application numbered stage context: /dso/project/application/stage/env
            if not Stages.is_default_env(stage):
                result.append(get_local_path(stage, path_prefix=path_prefix))

    return list(reversed(result)) if reverse else result


def load_templates_from_path(result, path, stage, include_contents=False, filter=None):
    for pth, subdirs, files in os.walk(path):
        for name in files:
            filePath = os.path.join(pth, name)
            if is_binary_file(filePath): continue
            key = filePath[len(path)+1:].replace(os.sep, '/')
            if filter and not re.match(filter, key): continue
            if key in result:
                Logger.warn(f"Inherited template '{key}' has been overridden.")
            result[key] = {
                'Stage': Stages.shorten(stage),
                'Scope': Contexts.translate_context('project', 'application', stage),
                'Path': filePath[len(Configs.working_dir) + 1:],
                'Date': get_file_modified_date(filePath)
            }
            if include_contents:
                with open(filePath, 'r', encoding='utf-8') as f:
                    result[key]['Contents'] = f.read()

    return result



# def __patch_loaded_template(template, path_prefix):
#     if os.path.isabs(template['Path']):
#         template['Path'] = template['Path'][len(Configs.working_dir) + 1:]
#     ### set Stage if it has not previousely been set, i.e. for newly loaded templates
#     if not 'Stage' in template.keys():
#         template['Stage'] = Stages.shorten(decode_local_path(template['Path'][len(path_prefix):])[0])
#     ### set Scope if it has not previousely been set, i.e. for newly loaded templates
#     if not 'Scope' in template.keys():
#         template['Scope'] = Contexts.translate_context('project', 'application', decode_local_path(template['Path'][len(path_prefix):])[0])


def load_context_templates(stage, path_prefix=None, uninherited=False, include_contents=False, filter=None):
    paths = get_context_hierachy_local_paths(stage, path_prefix=path_prefix, uninherited=uninherited)
    templates = {}
    for path in paths:
        Logger.debug(f"Loading template: path={path}")
        load_templates_from_path(templates, decode_local_path(path[len(path_prefix):])[0], os.path.join(Configs.working_dir, path), include_contents=include_contents, filter=filter)
        # for k in templates: __patch_loaded_template(templates[k], path_prefix)

    return templates


def locate_template_in_context_hierachy(stage, key, path_prefix=None, uninherited=False):
    templates = {}
    paths = get_context_hierachy_local_paths(stage, path_prefix=path_prefix, uninherited=uninherited, reverse=True)
    for path in paths:
        load_templates_from_path(templates, decode_local_path(path[len(path_prefix):])[0], os.path.join(Configs.working_dir, path), include_contents=True, filter=key)
        # for k in templates: __patch_loaded_template(templates[k], path_prefix)
        if key in templates: break

    return templates


def add_local_template(stage, key, path_prefix, contents):
    path = get_local_path(stage, key, path_prefix)
    Logger.debug(f"Adding local template: path={path}")
    fullPath = os.path.join(Configs.working_dir, path)
    os.makedirs(os.path.dirname(fullPath), exist_ok=True)
    with open(fullPath, 'w', encoding='utf-8') as f:
        f.write(contents)
    result = {
        'Path': path
    }
    return result


def get_parameter_store_path(stage, store_name, path_prefix=None, create=True):
    path = os.path.join(get_local_path(stage, path_prefix=path_prefix), store_name)
    if not os.path.exists(path):
        if create:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, 'w').close()
    return path


def load_parameter_store(result, path, stage, filter=None):
    parameters = flatten_dict(load_file(path))
    for key, value in parameters.items():
        if filter and not re.match(filter, key): continue
        if key in result:
            Logger.warn(f"Inherited parameter '{key}' has been overridden.")
        
        result[key] = {
            'Value': value,
            'Path': path,
            'Stage': Stages.shorten(stage),
            'Scope': Contexts.translate_context('project', 'application', stage)

        }

    return result


def get_context_hierachy_parameter_stores(stage, store_name, path_prefix=None, uninherited=False, reverse=False):
    paths = get_context_hierachy_local_paths(stage, path_prefix=path_prefix, uninherited=uninherited, reverse=reverse)
    stores = []
    for path in paths:
        stores.append({
            'Stage': Stages.shorten(decode_local_path(path[len(path_prefix):])[0]),
            'Path': os.path.join(path, store_name)
        })
    return stores


def load_context_local_parameters(stage, store_name, path_prefix=None, uninherited=False, filter=None):
    stores = get_context_hierachy_parameter_stores(stage, store_name, path_prefix, uninherited)
    parameters = {}
    for store in stores:
        Logger.debug(f"Loading store: path={store['Path']}")
        load_parameter_store(parameters, store['Path'], store['Stage'], filter=filter)

    return parameters



def add_local_parameter(stage, key, value, store_name, path_prefix=None):
    path = get_parameter_store_path(stage, store_name, path_prefix)
    params = load_file(path)
    set_dict_value(params, key.split('.'), value, overwrite_parent=False, overwrite_children=False)
    save_data(params, path)
    result = {
        'Key': key,
        'Value': value,
        'Stage': Stages.shorten(stage),
        'Scope': Contexts.translate_context('project', 'application', stage),
        'Path': path
    }
    return result


def locate_parameter_in_context_hierachy(stage, key, path_prefix=None, uninherited=False):
    stores = get_context_hierachy_parameter_stores(stage, store_name, path_prefix, uninherited, reverse=True)
    parameters = {}
    for store in stores:
        Logger.debug(f"Loading store: path={store['Path']}")
        load_parameter_store(parameters, store['Path'], store['Stage'], filter=key)
        if key in parameters: break

    return parameters
