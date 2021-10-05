# -*- coding: utf-8 -*-


 
class TrainData:
 
    def __init__(self, function):
        self.function = function
 
    def __call__(self, *args, **kwargs):
 
        # before function
        result = self.function(*args, **kwargs)
 
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
    pass


def get_from_list_textfile(n):
    pass

def get_from_list_excelsheet(n):
    pass

