import gpt_2_simple as gpt2
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
while True:
  ques = input("Question : ")

  inp = 'Teacher_GASLAWS : '+ques+'\n'+'Student_GASLAWS :'

  x = gpt2.generate(sess,
                length=20,
                temperature = 0.6,
                include_prefix=False,
                prefix=inp,
                nsamples=1,
                return_as_list=True)[0]
  print('Answer : {}'.format(x.split('\n')[1].split(':')[1].strip()))
