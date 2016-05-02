#! /usr/bin/python
# -*- coding: utf-8 -*-


def start_tf():
    os.environ['CUDA_HOME'] = '/usr/local/cuda'
    os.environ['LD_LIBRARY_PATH'] = '/usr/local/cuda/lib64'

    import tensorflow as tf
    globals()['tf'] = tf
    print('* Imported TensorFlow as `tf`')

    globals()['isess'] = tf.InteractiveSession()
    print('* Created InteractiveSession as `isess`')
