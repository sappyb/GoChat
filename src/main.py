# -*- coding: utf-8 -*-
from src.configuration import Configuration
from src.train_data import get_from_excelsheet
from src.model import Model
#Read Configurations
configs = Configuration()
all_configs_dict = configs.read_config()
#print(all_configs_dict)

#Read training Data from excel sheet
file_list = all_configs_dict.get('reader', None).get('defaultFilePath', None)
with open(file_list, 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        get_from_excelsheet(line.strip())

#Train Data
my_model = Model(configs=all_configs_dict)


#Run Chatbot