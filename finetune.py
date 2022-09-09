import gpt_2_simple as gpt2
import os as os
model_name = "124M"

sess = gpt2.start_tf_sess()

##gpt2.download_gpt2(model_name=model_name)

##os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

gpt2.finetune(
            sess,
            dataset='new 1.txt',
            model_name=model_name, # Model you have already downloaded
            steps=-1, # -1 will do unlimited. Enter number of iterations otherwise
            restore_from='fresh', # Also allows 'fresh' which will overwrite old training
            run_name='run1', # The name to pull or create a checkpoint under
            print_every=10, # Print iterations every X numebr
            sample_every=150, # Generate a text sample ever X number of iter.
            save_every=500, # Save a snapshot every X number of iter.
            learning_rate=0.0001, # Lower to 0.00001 if you are not getting massive changes in results
            batch_size=1 # Keep at 1 or 2, will use up more memory if you raise this
)

##gpt2.finetune(sess,
##              'shakespeare.txt',
##              steps=10,
##              model_name=model_name,
##              ##use_memory_saving_gradients=True,
##              ##only_train_transformer_layers = True,
##              ##accumulate_gradients = 1
##             )   # steps is max number of training steps