# Classification Model
## Date: 11/20/2022


import SteelDataset as sd
import os
import random
import string

class Classification(object):
    def __init__(self, train_num, num_segmented, fold) :
        self.data =  sd.STEELDataAcquisition('TRAIN', train_num, num_segmented)
        self.result_path = './result'
        self.result_name = self.generate_result_name()
        self.validation = None
        self.train_results = self.train_model()
        self.saved_model = self.save_model()
        self.eval_model = self.eval()
    
    def generate_result_name(self):
        name = 'STEEL_CLASSSIFICATION_' + ''.join(random.choices(string.ascii_lowercase, k=4))
        print('\n', '-'*50, '\n', 'Model Name:\n\t' ,name, '\n', '-'*50, '\n')
        return name

    def set_results_path(self):
        pass
    
    def train_model(self):
        pass

    def save_train_results(self):
        pass

    def save_model(self):
        pass

    def eval(self):
        pass


