'''
    This file is part of the September 2018 Workshop at Yuan Ze University.

    You can use these examples in the way you seem fit, though I can't make sure
    it will work fine in your case.
'''

import tensorflow as tf
import numpy as np
from pprint import pprint

# input Matrix
test_batch = 1
test_channels = 1 # input channels for input tensor
test_matrix_cols = 5


# filter
test_input_channels = test_channels # this depends on input tensor
test_output_channels = 1 # try to change this
test_filter_cols = 3


# input convolution filter
input_filter = tf.placeholder("float", shape=[test_filter_cols, test_input_channels,
                                              test_output_channels])

# input matrix to convolve
input_matrix = tf.placeholder("float", shape=[test_batch, test_matrix_cols, test_channels])

# Convolution results=========
# keeps size
# output_conv = tf.nn.conv1d(value=input_matrix, filters=input_filter, stride=1, padding='SAME')

# changes size
output_conv = tf.nn.conv1d(value=input_matrix, filters=input_filter, stride=1, padding='VALID')

_inputfilter = np.zeros(shape=[test_filter_cols, test_input_channels,
                               test_output_channels], dtype="float")
_inputmatrix = np.zeros(shape=[test_batch, test_matrix_cols, test_channels], dtype="float")

# Filter part
initial_val = 1.0 / 2.0
for cols in range(test_filter_cols):
    for in_cha in range(test_input_channels):
        for out_cha in range(test_output_channels):
            _inputfilter[cols, in_cha, out_cha] = initial_val

# input matrix
initial_val = 1.0
for batch in range(test_batch):
    for cols in range(test_matrix_cols):
        for channels in range(test_channels):
            _inputmatrix[batch, cols, channels] = initial_val

with tf.Session() as sess:
    print("\nConvolution2D result on input tensor is (TENSORFLOW):\n")
    result_form_conv = sess.run(output_conv, feed_dict={input_filter: _inputfilter, input_matrix: _inputmatrix})
    print(result_form_conv.shape)
    pprint(result_form_conv)

