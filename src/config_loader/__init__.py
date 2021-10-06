"""Configuration loader & provider"""

import os
import os.path
from typing import Any, Dict

from yaml import load, SafeLoader
from logbook import Logger

class ConfigLoader:
    """Load configuration files and make them available for the project"""
    
    
    def __init__(self,
                log: Logger,
                path: str) -> None:
        self.__config = {}
        config = {}
        file_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        file_names = ['.'.join(fn.split('.')[:-1]) for fn in
                           file_list if fn.split('.')[-1] == 'yml']
        for name in file_names:
            file_path = path + '/' + name + '.yml'
            with open(file_path, encoding='utf-8') as f:
                config[name] = load(f, Loader=SafeLoader)
                log.info(f"Config file {name}.yml loaded")
        self.populate_config(config)
        log.info(f"Config fully loaded")

    def populate_config(self,
                        config: Dict[str, Any]) -> None:
        for key in config.keys():
            self.__config = {
                **self.__config,
                **config[key],
            }
        self.__config = {
            **self.__config,
            **config,
        }

    def get_config_value(self,
                         config_key: str) -> str:
        return self.__config.get(config_key)

    def get_config_file_values(self,
                               config_file_key: str) -> Dict[str, Any]:
        return self.__config.get(config_file_key)