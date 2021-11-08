import gpt_2_simple as gpt2
model_name = "1558M"

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              'shakespeare.txt',
              steps=10,
              model_name=model_name,
              only_train_transformer_layers=True)   # steps is max number of training steps