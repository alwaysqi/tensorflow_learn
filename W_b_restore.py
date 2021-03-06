import tensorflow as tf
import numpy as np

# restore variables
# redefine the same shape and same type for your variables
W = tf.Variable(np.arange(6).reshape(2, 3), dtype=tf.float32, name='Weights')#name must be the same with saver
b = tf.Variable(np.arange(3).reshape(1, 3), dtype=tf.float32, name='biases')

# not need init step

saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "my_net/save_net.ckpt")
    print("weight:", sess.run(W))
    print("biases:", sess.run(b))
