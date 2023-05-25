import tensorflow as tf
import os
from models.unets import Unet2D

# try:
#     import h5py
# except ImportError:
#     h5py = None
#     print('failed')

# print(tf.config.list_physical_devices('GPU'))
# path = './training_history/'
# filename = 'test'
# print(os.path.abspath(path))
# # f=open(path+"2023-03-30 09:29.hdf5", "x")
# unet2d = Unet2D(n_filters=200, input_dim_x=None, input_dim_y=None, num_channels=3)
# model, model_name = unet2d.get_unet_model_yuanqing()
# model.save('{}{}.hdf5'.format(path, filename))

def program(function, text):
    function(text)
    
program(print, 'test')
