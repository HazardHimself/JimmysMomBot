import gpt_2_simple as gpt2
model_name = "124M"
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
gpt2.generate(sess,
              model_name=model_name,
              prefix="We are",
              length=100,
              temperature=0.7,
              top_p=0.9,
              nsamples=1,
              batch_size=1
              )