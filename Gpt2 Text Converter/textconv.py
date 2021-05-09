import gpt2thing as gpt2
import time


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

def GenResponse(prompt):
  prompt = prompt + "\n<|response|>\n"
  return gpt2.generate(sess,length=100,temperature=1,top_k=0,top_p=0.9,prefix=prompt,nsamples=1,batch_size=1,include_prefix=False,truncate='<|endoftext|>', return_as_list=True)[0]

def ParseResponse():
    pass

active = True
blacklist = "<|"

print("Ready to Game B)")
while active:
    f = open("../text.txt", "r")
    prompt = f.read()
    if prompt[:1] == '1':
        print("found input")
        print("generating...")
        fw = open("../text.txt", "w")
        resp = GenResponse(" " + prompt[1:])
        print(resp)

        if blacklist in resp:
            resp = resp[:resp.index(blacklist)]
        else:
            pass

        print("generated")
        fw.seek(0)
        fw.truncate()
        fw.write("0" + resp)
        fw.close()

    time.sleep(.300)
    f.close()
