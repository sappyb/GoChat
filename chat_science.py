import gpt_2_simple as gpt2
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
while True:
  ques = input("Question : ")

  inp = 'Teacher_SCIENCE : '+ques+'\n'+'Student_SCIENCE :'

  x = gpt2.generate(sess,
                length=20,
                temperature = 0.2,
                include_prefix=False,
                prefix=inp,
                nsamples=1,
                return_as_list=True)[0]
  print('Answer : {}'.format(x.split('\n')[1].split(':')[1].strip()))
