##Originally taken from https://medium.com/@stasinopoulos.dimitrios/a-beginners-guide-to-training-and-generating-text-using-gpt2-c2f2e1fbd10a

#slightly altered code from   https://github.com/minimaxir/gpt-2-simple
import gpt_2_simple as gpt2
model_name = "1558M"
# model is saved into current directory under /models/124M/
##gpt2.download_gpt2(model_name=model_name) #need to run only once. comment out once done.

sess = gpt2.start_tf_sess()
##gpt2.load_gpt2(sess)

gpt2.finetune(sess,
              'shakespeare.txt',
              steps=10,
              checkpoint_dir=checkpoint_dir)   # steps is max number of training steps

output = input("Do file output? Y/N ")

if output == "Y":
    for i in range(5):
        prefix = input("Supply prefix: ")
        gpt2.generate_to_file(
            sess,
            model_name=model_name,
            prefix=prefix,
            length=100,
            temperature=0.7,
            top_p=0.9,
            nsamples=1,
            batch_size=1,
            destination_path='gpt_2_gen_texts.txt'
        )
else:
    for i in range(5):
        prefix = input("Supply prefix: ")
        gpt2.generate(sess,
                      model_name=model_name,
                      prefix=prefix,
                      length=100,
                      temperature=0.7,
                      top_p=0.9,
                      nsamples=1,
                      batch_size=1,
                      include_prefix=False
                      ##return_as_list=True
                      )