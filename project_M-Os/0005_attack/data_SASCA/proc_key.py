import os
import sys
import numpy as np
import time
import serv_manager as svm

def Command(cmd):
  print(cmd)
  svm.System(cmd)
  return

def Combine(tag='key'):
  for s in range(0, 1000):
    data_name = tag+'s/'+tag+'_'+str(s).zfill(4)+'.npy'
    key = svm.Load(data_name)[0]
    set_name = 'data_'+tag+'/'+tag+'_set_'+str(s).zfill(4)+'.npy'
    DATA = svm.Load(data_name)
    passed = True
    for t in range(0, 100):
      if DATA[t]!=key:
        passed = False
    if passed:
      print('Saving '+set_name)
      svm.Save(set_name, key)
    else:
      print('No '+set_name)
      time.sleep(5)
  return

def Process(tag='key'):
  Command('unzip -qq ../inter_gen/'+tag+'s.zip')
  Command('mkdir data_'+tag+'/')
  Combine(tag)
  Command('zip -qq data_'+tag+'.zip -r data_'+tag+'/')
  Command('rm -r data_'+tag+'/ '+tag+'s/')
  return

if __name__=='__main__':
  Process('key')

