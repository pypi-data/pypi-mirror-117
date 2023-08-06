import os
import re
from pathlib import Path
from mabledsocli.logger import Logger
from mabledsocli.config import Configs
from mabledsocli.providers import Providers
from mabledsocli.templates import TemplateProvider
from mabledsocli.stages import Stages
from mabledsocli.constants import *
from mabledsocli.exceptions import DSOException
from mabledsocli.contexts import Contexts
from mabledsocli.local_utils import *
from mabledsocli.settings import *


_default_spec = {
    'path': os.path.join(Configs.config_dir, 'templates')
}


def get_default_spec():
    return _default_spec.copy()


class LocalTemplateProvider(TemplateProvider):


    def __init__(self):
        super().__init__('template/local/v1')


    @property
    def root_dir(self):
        return Configs.template_spec('path')


    def get_path_prefix(self):
        return self.root_dir + os.sep


    def list(self, project, application, stage, uninherited=False, include_contents=False, filter=None):
        templates = load_context_templates(stage, path_prefix=self.get_path_prefix(), uninherited=uninherited, include_contents=include_contents, filter=filter)
        result = {'Templates': []}
        for key, details in templates.items():
            item = {'Key': key}
            item.update(details)
            result['Templates'].append(item)
        return result



    def add(self, project, application, stage, key, contents, render_path=None):
        if not Stages.is_default(stage) and not ALLOW_STAGE_TEMPLATES:
            raise DSOException(f"Templates may not be added to stage scopes, as the feature is currently disabled. It may be enabled by setting 'ALLOW_STAGE_TEMPLATES' to 'yes' in the DSO global settings.")
        response = add_local_template(stage, key, path_prefix=self.get_path_prefix(), contents=contents)
        result = {
                'Key': key,
                'Stage': Stages.shorten(stage),
                'Path': response['Path'],
            }
        return result


    def get(self, project, application, stage, key, revision=None):
        if revision:
            raise DSOException(f"Template provider 'local/v1' does not support versioning.")
        Logger.debug(f"Getting template: stage={stage}, key={key}")
        found = locate_template_in_context_hierachy(stage, key, path_prefix=self.get_path_prefix())
        if not found:
            raise DSOException(f"Template '{key}' not found nor inherited in the given context:stage={Stages.shorten(stage)}")
        result = {
                'Key': key, 
            }
        result.update(found[key])
        return result


    def delete(self, project, application, stage, key):
        Logger.debug(f"Locating template:stage={stage}, key={key}")
        ### only parameters owned by the context can be deleted, hence uninherited=True
        found = locate_template_in_context_hierachy(stage, key, path_prefix=self.get_path_prefix(), uninherited=True)
        if not found:
            raise DSOException(f"Template '{key}' not found in the given context:stage={Stages.shorten(stage)}")
        Logger.info(f"Deleting template: path={found[key]['Path']}")
        fullPath = os.path.join(Configs.working_dir, found[key]['Path'])
        os.remove(fullPath)
        return {
                'Key': key, 
                'Scope': found[key]['Scope'],
                'Origin': found[key]['Origin'],
                'Path': found[key]['Path'],
                }


    def history(self, project, application, stage, key, include_contents=False):
        raise DSOException(f"Template provider 'local/v1' does not support versioning.")



def register():
    Providers.register(LocalTemplateProvider())
