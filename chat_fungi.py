import gpt_2_simple as gpt2
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
print('Start Now')
host = '127.0.0.1'
port = int(2004)
s.bind((host, port))
s.listen(1)

while True:
  #ques = input("Question : ")
  conn, addr = s.accept()
  ques = conn.recv(100000)
  ques = ques.decode("utf-8")
  #print(ques)
  #if not ques:
  #    continue
  #if ques == 'exit':
  #    break
  while ques:
    inp = 'Teacher_FUNGI : '+ques+'\n'+'Student_FUNGI :'
  
    x = gpt2.generate(sess,
                length=20,
                temperature = 0.2,
                include_prefix=False,
                prefix=inp,
                nsamples=1,
                return_as_list=True)[0]
    print('Answer : {}'.format(x.split('\n')[1].split(':')[1].strip()))
  conn.close()
  break
