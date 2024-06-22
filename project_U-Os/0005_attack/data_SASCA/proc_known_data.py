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
  for s in range(0, 10):
    DATA = []
    for g in range(0, 10):
      data_name = tag+"s/"+tag+"_"+str((g*10+s)).zfill(4)+".npy"
      DATA.append(svm.Load(data_name))
    for t in range(0, 100):
      trace_name = "data_"+tag+"/"+tag+"_"+str(s*100+t).zfill(4)+".npy"
      data_t = np.array([DATA[0][t], DATA[1][t], \
                         DATA[2][t], DATA[3][t], \
                         DATA[4][t], DATA[5][t], \
                         DATA[6][t], DATA[7][t], \
                         DATA[8][t], DATA[9][t]])
      print("Saving "+trace_name)
      svm.Save(trace_name, data_t)
  return

def Process(tag='nonce'):
  Command("unzip -qq ../inter_gen/"+tag+"s.zip")
  Command("mkdir data_"+tag+"/")
  Combine(tag)
  Command("zip -qq data_"+tag+".zip -r data_"+tag+"/")
  Command("rm -r data_"+tag+"/ "+tag+"s/")
  return

if __name__=='__main__':
  Process('ciphertag')
  Process('nonce')
  Process('plaintext')

