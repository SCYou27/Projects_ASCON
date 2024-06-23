import os
import sys
import numpy as np
import time
import serv_manager as svm

def Command(cmd):
  print(cmd)
  svm.System(cmd)
  return

def Combine(tag='nonce'):
  for s in range(0, 1000):
    data_name = tag+'s/'+tag+'_'+str(s).zfill(4)+'.npy'
    DATA = svm.Load(data_name)
    set_name = 'data_'+tag+'/'+tag+'_set_'+str(s).zfill(4)+'.npy' 
    print('Saving '+set_name)
    svm.Save(set_name, DATA)
  return

def Process(tag='nonce'):
  Command('unzip -qq ../inter_gen/'+tag+'s.zip')
  Command('mkdir data_'+tag+'/')
  Combine(tag)
  Command('zip -qq data_'+tag+'.zip -r data_'+tag+'/')
  Command('rm -r data_'+tag+'/ '+tag+'s/')
  return

if __name__=='__main__':
  Process('ciphertag')
  Process('nonce')
  Process('plaintext')

