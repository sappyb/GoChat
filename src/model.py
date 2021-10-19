# -*- coding: utf-8 -*-
#tensorflow_version 1.x
#pip install gpt-2-simple
#import gpt_2_simple as gpt2
class Model():
    def __init__(self, **kwargs):
        self.model_configs = kwargs.get('configs', None).get('model', None).get('params', None)
        self.model_name = self.model_configs.get('model_name', None)
        self.dataset = self.model_configs.get('dataset', None)
        self.steps = self.model_configs.get('steps', None)
        self.restore_from = self.model_configs.get('restore_from', None)
        self.run_name = self.model_configs.get('run_name', None)
        self.print_every = self.model_configs.get('print_every', None)
        self.sample_every = self.model_configs.get('sample_every', None)
        self.save_every = self.model_configs.get('save_every', None)
        self.length = self.model_configs.get('length', None)
        self.temperature = self.model_configs.get('temperature', None)
        self.include_prefix = self.model_configs.get('include_prefix', None)
        self.nsamples = self.model_configs.get('nsamples', None)
'''     
    def finetune():
        gpt2.download_gpt2(model_name=self.model_name)
        sess = gpt2.start_tf_sess()
        TrainData tf()
        gpt2.finetune(sess,
                      dataset=self.dataset,
                      model_name=self.model_name,
                      steps=self.steps,
                      restore_from=self.restore_from,
                      run_name=self.run_name,
                      print_every=self.print_every,
                      sample_every=self.sample_every,
                      save_every=self.save_every
                      )
    def query():
        self.finetune()
        while True:
          ques = input("Question : ")
          input = 'T : '+ques+'\n'+'S :'
          answer = gpt2.generate(sess,
                        length=self.length,
                        temperature=self.temperature,
                        include_prefix=self.include_prefix,
                        prefix=input,
                        nsamples=self.nsamples,
                        )
          print(answer)

'''
