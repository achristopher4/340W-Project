# Classification Model
## Date: 11/20/2022


import SteelDataset as sd
import os

import matplotlib.pyplot as plt
import numpy as np
import PIL
from PIL import Image
import tensorflow as tf

from tensorflow import keras
from keras import layers
from keras.models import Sequential

class Classification(object):
    def __init__(self, train_num, num_segmented, fold) :
        self.train_datadir = './datasets/STEEL/train_images'
        self.data =  sd.STEELDataAcquisition('TRAIN', train_num, num_segmented)
        self.result_path = ['./result', self.generate_result_name()]
        ##
        # Appears to be testing model on testing data
        self.validation = sd.STEELDataAcquisition('TEST', train_num, num_segmented)
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
        #img = PIL.Image.open(str( './datasets/STEEL/train_images/0a1cade03.jpg' ))
        #img.show()
        data_dir = './STEEL_TRAINING'
        batch_size = 32
        img_height, img_width = (Image.open('./datasets/STEEL/train_images/0a1cade03.jpg')).size

        train_ds = tf.keras.utils.image_dataset_from_directory(
            data_dir,
            validation_split = 0.2, 
            subset = "training",
            seed = 123,
            image_size =(img_height, img_width),
            batch_size = batch_size
        )
        
        val_ds = tf.keras.utils.image_dataset_from_directory(
            data_dir,
            validation_split = 0.2,
            subset = "validation",
            seed = 123, 
            image_size = (img_height, img_width),
            batch_size = batch_size
        )

        class_names = list(self.data.training.keys())

        AUTOTUNE = tf.data.AUTOTUNE
        
        train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds.cache().prefetch(buffer_size = AUTOTUNE)

        num_classes = len(class_names)

        normalization_layer = layers.Rescaling(1./255)

        normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
        image_batch, labels_batch = next(iter(normalized_ds))
        first_image = image_batch[0]

        #print(np.min(first_image), np.max(first_image))

        num_classes = len(class_names)
        model = Sequential([
            layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes)
        ])

        model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

        print(model.summary())

        epochs=10
        history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=epochs
        )

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

        data_augmentation = keras.Sequential(
            [
                layers.RandomFlip("horizontal",
                                input_shape=(img_height,
                                            img_width,
                                            3)),
                layers.RandomRotation(0.1),
                layers.RandomZoom(0.1),
            ]
        )

        plt.figure(figsize=(10, 10))
        for images, _ in train_ds.take(1):
            for i in range(9):
                augmented_images = data_augmentation(images)
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(augmented_images[0].numpy().astype("uint8"))
                plt.axis("off")
        
        model = Sequential([
            data_augmentation,
            layers.Rescaling(1./255),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Conv2D(64, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(),
            layers.Dropout(0.2),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes, name="outputs")
        ])

        model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
        
        model.summary()

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(epochs)

        plt.figure(figsize=(8, 8))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

    def save_train_results(self):
        pass

    def save_model(self):
        pass

    def eval(self):
        pass


