import os 
import math
import os
import math
import numpy as np
import glob
import datetime
import argparse
import time

import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten, Reshape
from keras.layers import Embedding, Input, merge
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import adam_v2
from keras.regularizers import l2, l1
from keras.utils.np_utils import to_categorical
from keras import backend as K
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard


# Import image crop window and other pre defined settings
from defines import *


def train_model_from_args(args):
    args.directories.sort()
    time_format='%Y-%m-%d_%H-%M-%S'
    trainstart=datetime.datetime.now()
    time_string=trainstart.strftime(time_format)

    steer=np.array([])
    data_lengths=[]
    for directory in args.directories:
        ctlfiles=glob.glob(os.path.join(directory, 'commands*.npz'))
        for ctlfile in sorted(ctlfiles):
            ctldata=np.load(ctlfile)['arr_0']
            data_to_append=np.trim_zeros(ctldata[:, 0], trim='b')
            data_lengths.append(len(data_to_append))
            steer=np.concatenate((steer, data_to_append[args.delay:len(data_to_append)]), axis=0)

    steerSampleMean=steer.mean()
    steerSampleSTD=steer.std()
    np.savez("steerstats.npz", [steerSampleMean, steerSampleSTD])

    row_offset=ROW_OFFSET
    nrows=NROWS
    ncols=NCOLS

    total_training_samples=sum(data_lengths)
    training_images=np.zeros((total_training_samples-args.delay*len(data_lengths), nrows, ncols, 3)).astype('float32')

    i=0
    n=0
    for directory in args.directories:
        imgfiles=glob.glob(os.path.join(directory, 'imgs*.npz'))
        for imgfile in sorted(imgfiles):
            imdata=np.load(imgfile)['arr_0'].astype('float32')
            for image in imdata[0:data_lengths[i]-args.delay]:
                crop_image=image[row_offset:row_offset+nrows, :]
                image_mean=crop_image.mean()
                image_std=crop_image.std()
                training_images[n]=(crop_image-image_mean)/image_std
                n+=1
            i+=1

    from dropout_model import model
    num_epochs=args.epochs
    save_epochs=args.save_frequency
    if args.init_weights!="":
        model.load_weights(args.init_weights)

    checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join('checkpoints', args.weight_filename + '_{epoch:02d}.h5'),
        save_weights_only=True,
        save_freq=args.save_frequency * (total_training_samples // 25),
        verbose=1
    )

    tensorboard_callback = TensorBoard(
        log_dir='logs',
        histogram_freq=1,
        write_graph=True,
        write_images=True,
        update_freq='epoch',
        profile_batch=0
    )

    hist = np.zeros([num_epochs])

    for n in range(num_epochs):
        print("starting epoch {0}".format(n))
        h = model.fit(
            [training_images],
            [(steer-steerSampleMean)/steerSampleSTD],
            batch_size=25,
            epochs=1,
            verbose=1,
            validation_split=0.1,
            shuffle=True,
            callbacks=[checkpoint_callback, tensorboard_callback]
        )
        hist[n] = h.history['val_loss'][0]

    import matplotlib.pyplot as plt
    plt.plot(np.array(range(hist.shape[0])), hist)
    plt.savefig('training_hist.png')
    plt.show()

def train_model(epochs, batch_size, learning_rate, dataset_path, weight_filename='weights', init_weights='', delay=0, save_frequency=10):
    class CustomArgs:
        pass

    args = CustomArgs()
    args.epochs = epochs
    args.batch_size = batch_size
    args.learning_rate = learning_rate
    args.directories = [dataset_path] 
    args.dataset_path = dataset_path
    args.weight_filename = weight_filename
    args.init_weights = init_weights
    args.delay = delay
    args.save_frequency = save_frequency

    train_model_from_args(args)


# Keep the argparse code here
if __name__ == "__main__":
    #This code sets up the parser for command line arguments specifying parameters for training.
    parser=argparse.ArgumentParser()
    parser.add_argument('--weight_filename', action='store', default='weights', help='prefix for saved weight files')
    parser.add_argument('--init_weights', action='store', default='', 
            help='specifies an existing weight file to use as an initial condition for the network at the start of training')
    parser.add_argument('--delay', action='store', default=0, type=int, 
            help='delay between image and steering training data to compensate for processing delay during runtime')
    parser.add_argument('--epochs', action='store', default=100, type=int, 
            help='number of epochs to train over')
    parser.add_argument('--save_frequency', action='store', default=10, type=int, 
            help='number of epochs between weight file saves')
    parser.add_argument('directories', nargs='+', help='list of directories to read training data from')
    args = parser.parse_args()

    # Call the train_model_from_args function
    train_model_from_args(args)