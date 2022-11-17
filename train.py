# Train Model
## Date: 11/20/2022

import End2End

config = {'RESULTS_PATH': './results', 'DATASET': 'STEEL'}

train_model = End2End(config)
train_model.train()

