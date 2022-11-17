# Train Model
## Date: 11/20/2022

import os
import tensorflow as tf
import Classification


class End2End:
    def __init__(self, cfg):
        self.cfg = cfg
        self.storage_path: str = os.path.join(self.cfg['RESULTS_PATH'], self.cfg['DATASET'])

    def train(self):
        model = Classification.Model()
        optimizer = None
        loss_seg = None
        loss_dec = None
        training_dataset = None
        validation_dataset = None
        train_results = self.train_results()
        eval_results = None
    
    def train_model(self):
        pass

    def eval_results(self):
        pass