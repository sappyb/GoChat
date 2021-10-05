# -*- coding: utf-8 -*-
import pandas as pd
from pathlib import Path
from ruamel.yaml import load, dump, Loader


class Configuration():
    def __init__(self, **kwargs):
        pass
    
    def read_config():
        defaultConfigPath = Path(Path(__file__).parent, 'default.yaml')
        with open(defaultConfigPath , 'r') as defaultConfigFile:
            defaultConf = load(defaultConfigFile, Loader=Loader)    
        return defaultConf

