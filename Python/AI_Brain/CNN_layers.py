import tensorflow as tf
import numpy as np

image = np.array([
    [1,2,3,0],
    [4,5,6,1],
    [7,8,9,2],
    [3,4,5,6]
], dtype=np.float32)

image = image.reshape(1,4,4,1)
kernal = np.array([
    [[1],[0]],
    [[0],[1]]
],dtype=np.float32)

kernal = kernal.reshape(2,2,1,1)

conv_output = tf.nn.conv2d(
    image,
    filters=kernal,
    strides=[1,1,1,1],
    padding='VALID'
)

print("\nconvolution output:")
print(conv_output.numpy()[0,1,1,0])

pool_output = tf.nn.max_pool2d(
    conv_output,
    ksize=[1,2,2,1],
    strides=[1,2,2,1],
    padding='VALID'
)
print("\nmax pooling output:")
print(pool_output.numpy()[0,:,:,0])

Flatten = tf.keras.layers.Flatten()
flat_output = Flatten(pool_output)
print("\nflattened output:")
print(flat_output.numpy())

