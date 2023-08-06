import os
import re
from pathlib import Path
from mabledsocli.logger import Logger
from mabledsocli.config import Configs
from mabledsocli.providers import Providers
from mabledsocli.parameters import ParameterProvider
from mabledsocli.stages import Stages
from mabledsocli.constants import *
from mabledsocli.exceptions import DSOException
from mabledsocli.contexts import Contexts
from mabledsocli.local_utils import *
from mabledsocli.settings import *


_default_spec = {
    'path': os.path.join(Configs.config_dir, 'parameters'),
    'store': 'local.yaml',
    'format': 'yaml',
    'allowGroups': 'no',
    'prependGroups': 'yes',
    'groupDelimiter': '/',
    'nestedDelimiter': '.',
}


def get_default_spec():
    return _default_spec.copy()



config = {
    # 'parameters_dir' : '{0}/parameters'.format(Configs.dir_name),
    'file_extension' : {
        'yaml' : 'yml',
        'json' : 'json',
    }
}

class LocalParameterProvider(ParameterProvider):

    def __init__(self):
        super().__init__('parameter/local/v1')

    @property
    def root_dir(self):
        return Configs.parameter_spec('path')


    def get_path_prefix(self):
        return self.root_dir + os.sep

    @property
    def store_name(self):
        return Configs.parameter_spec('store')

 
    def add(self, project, application, stage, key, value):
        Logger.debug(f"Adding local parameter: stage={stage}, key={key}")
        response = add_local_parameter(stage, key, value, store_name=self.store_name, path_prefix=self.get_path_prefix())
        return response


    def list(self, project, application, stage, uninherited=False, filter=None):
        parameters = load_context_local_parameters(stage, store_name=self.store_name, path_prefix=self.get_path_prefix(), uninherited=uninherited, filter=filter)
        result = {'Parameters': []}
        for key, details in parameters.items():
            item = {
                'Key': key,
            }
            item.update(details)
            result['Parameters'].append(item)

        return result



    def get(self, project, application, stage, key, revision=None):
        if revision:
            raise DSOException(f"Parameter provider 'local/v1' does not support versioning.")
        Logger.debug(f"Getting parameter: stage={stage}, key={key}")
        found = locate_parameter_in_context_hierachy(stage, key, path_prefix=self.get_path_prefix())
        if not found:
            raise DSOException(f"Parameter '{key}' not found nor inherited in the given context: stage={Stages.shorten(stage)}")
        result = {
                'Key': key, 
            }
        result.update(found[key])
        return result



    def delete(self, context, key):
        self.__assert_param_file_exists(context, key)
        params = self.__load_param_file_from_key(context, key)
        keys = self.__get_param_name_from_key(key).split('.')
        if not del_dict_item(params, keys):
            raise DSOException(CLI_MESSAGES['ParameterNotFound'].format(key))
        ### recursively delet empty parent scopes 
        del_dict_empty_item(params, keys[:-1])
        path = self.__get_param_file_path_from_key(context, key)
        if len(params.keys()) > 0:
            self.__save_param_file(params, path)
        else:
            os.remove(path)
            conetxt_root_path = self.__get_params_root_path(context)
            if len(os.listdir(conetxt_root_path)) == 0:
                os.rmdir(conetxt_root_path)



def register():
    Providers.register(LocalParameterProvider())
