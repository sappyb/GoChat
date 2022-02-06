import gpt_2_simple as gpt2
gpt2.download_gpt2(model_name="355M")
'''
raw_data = '/content/drive/My Drive/data.json'
import json


with open(raw_data, 'r') as f:
    df =json.load(f)


data = []

for x in df:
    for y in range(len(x['dialog'])-1):
        a = '[BOT] : ' + x['dialog'][y+1]['text']
        q = '[YOU] : ' + x['dialog'][y]['text']
        data.append(q)
        data.append(a)
        
with open('chatbot.txt', 'w') as f:
     for line in data:
        try:
            f.write(line)
            f.write('\n')
        except:
            pass
'''
file_name = "/home/sappbhow768/GoChat/data/chatdata.txt"

sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset=file_name,
              model_name='355M',
              steps=100,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=100,
              save_every=100
              )
'''
while True:
  ques = input("Question : ")

  inp = '[YOU] : '+ques+'\n'+'[BOT] :'

  x = gpt2.generate(sess,
                length=20,
                temperature = 0.6,
                include_prefix=False,
                prefix=inp,
                nsamples=1,
                return_as_list=True)[0]
  print(x)
'''
