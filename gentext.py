#slightly altered code from   https://github.com/minimaxir/gpt-2-simple
import gpt_2_simple as gpt2
model_name = "124M"
# model is saved into current directory under /models/124M/
##gpt2.download_gpt2(model_name=model_name) #need to run only once. comment out once done.
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
##gpt2.generate(sess, run_name='run1')
##gpt2.generate(sess, length=39, include_prefix=False, temperature=0.1, top_k=1, top_p=0.9,run_name='run1', prefix="Is there Earth No.2?", return_as_list=True)

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