import gpt_2_simple as gpt2

global sess
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
global phrases
global model_name
model_name = "124M"
phrases = []

def aitext(hello):
    global phrases
    global sess
    if not phrases:
        """gpt2.load_gpt2(sess)"""
        single_text = gpt2.generate(sess,
                                    return_as_list=True,
                                    model_name=model_name,
                                    length=100,
                                    temperature=0.7,
                                    top_p=0.9,
                                    nsamples=5,
                                    batch_size=1,
                                    include_prefix=False)[0]
        phrases = single_text.splitlines()
        phrases[:] = [x for x in phrases if ((x != "<|endoftext|>") and (x != "{Attachments}"))]
    retval = phrases[0]
    phrases.pop(0)
    return retval

def contextgen(context):
    global sess
    response = gpt2.generate(sess, model_name=model_name, length=30, prefix=context, nsamples=1, batch_size=1, truncate='\n', include_prefix=False, return_as_list=True)
    return response[0]

