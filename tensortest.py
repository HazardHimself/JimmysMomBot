from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
# Create tensor
hello = tf.string_join(["Hello, World"])
# Launch session
sess = tf.Session()
print(sess.run(hello))