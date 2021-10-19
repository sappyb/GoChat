# -*- coding: utf-8 -*-
import pandas as pd
from pathlib import Path
 
class TrainData:
 
    def __init__(self, function):
        self.function = function
        self.write_file = Path(Path(__file__).parent.parent, 'data/chatdata.txt')
 
    def __call__(self, *args, **kwargs):
        
        # before function
        result = self.function(*args, **kwargs)
        with open(self.write_file, 'a') as fp:
            fp.write(result)
        
        # after function
        return result
 
 # adding class decorator to the function
@TrainData
def get_from_textfile(n):
    pass
    #print("given number is:", n)
    #return n * n
 
@TrainData
def get_from_excelsheet(n):
    df = pd.read_csv(n,header='infer')
    df['full_string'] = df['speaker'] + '_' + df['source'] + ' : ' + df['utterance']
    st = '\n'.join(df['full_string'].to_list())
    return st


def get_from_list_textfile(n):
    pass

def get_from_list_excelsheet(n):
    pass

