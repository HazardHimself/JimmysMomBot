import gpt_2_simple as gpt2
import tensorflow as tf
from tensorflow.python.client import device_lib
import os as os

model_name = "1558M"

##os.environ["TF_GPU_ALLOCATOR"]="cuda_malloc_async"
##os.environ["TF_CPP_VMODULE"]="gpu_process_state=10,gpu_cudamallocasync_allocator=10"

#sess = gpt2.start_tf_sess()

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)


##def limitgpu(maxmem):
##    gpus = tf.config.list_physical_devices('GPU')
##    if gpus:
##        # Restrict TensorFlow to only allocate a fraction of GPU memory
##        try:
##            for gpu in gpus:
##                tf.config.experimental.set_virtual_device_configuration(gpu,
##                                                                        [
##                                                                            tf.config.experimental.VirtualDeviceConfiguration(
##                                                                                memory_limit=maxmem)])
##            print('Success!')
##        except RuntimeError as e:
##            # Virtual devices must be set before GPUs have been initialized
##            print(e)
##
##
### 4.0GB
##limitgpu(4096)

##gpt2.download_gpt2(model_name=model_name)

gpt2.finetune(sess,
              'shakespeare.txt',
              steps=10,
              model_name=model_name,
              ##use_memory_saving_gradients=True,
              # only_train_transformer_layers=True,
              # accumulate_gradients = 1,
              )  # steps is max number of training steps