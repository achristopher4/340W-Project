# Main file for collecting data that will be used in model

import SteelDataset as sd

train_num = 3000
num_segmented = 50
training_data = sd.STEELDataAcquisition('TRAIN', train_num, num_segmented)
#testing_data = sd.STEELDataAcquisition('TEST')

print(training_data)
print(training_data.num_pos, training_data.num_neg)
#print(training_data.data)




""""

##################################
# Need to Complete:
    Get training number
    Get segmented number
    Transpose?
##################################

"""