# Classification Model
## Date: 11/20/2022


import SteelDataset as sd
import os

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

class Classification(object):
    def __init__(self, train_num, num_segmented, fold) :
        self.data =  sd.STEELDataAcquisition('TRAIN', train_num, num_segmented)
        self.result_path = ['./result', self.generate_result_name()]
        ##
        # Appears to be testing model on testing data
        self.validation = self.data =  sd.STEELDataAcquisition('TEST', train_num, num_segmented)
        ##
        self.model = self.train_model()
        self.saved_model = self.save_model()
        self.eval_model = self.eval()
    
    def generate_result_name(self):
        models = (os.listdir('./results'))
        baseName = 'STEEL_CLASSSIFICATION'
        if len(models) == 0:
            postfix = 0
        else:
            postfix = 1
            path = f'./results/{baseName}_{postfix}'
            while os.path.exists(path):
                postfix += 1
                path += f'./results/{baseName}_{postfix}'
        name = f'{baseName}_{postfix}'
        print('\n', '-'*50, '\n', 'Model Name:\n\t' ,name, '\n', '-'*50, '\n')
        return name
    
    def train_model(self):
        PIL.Image.open(str(self.data['pos'][1]))

    def save_train_results(self):
        pass

    def save_model(self):
        pass

    def eval(self):
        pass


