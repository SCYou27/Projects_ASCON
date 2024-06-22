import numpy as np
import sys
import os
import time
import serv_manager as svm
import enumeration
import ascon_aead

ENC_128 = ascon_aead.ASCON_AEAD().ASCON_128.Enc

iteration_time = 100000

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}


def Find_Prediction(Units):
  Value = 0
  for t in range(0, len(Units)):
    Value *= 2
    if Units[t]==1:
      Value +=1
  return hex(Value)[2:].zfill(32)

class Evaluation:
  def __init__(self, tag='L01'):
    self.iteration_time = iteration_time
    self.tag = tag
    return
  
  def calculate(self, Tr):
    tail = '_'+str(Tr).zfill(4)+'.npy'
    ANS = str(svm.Load('data_key/key'+tail))
    N = svm.Load('data_nonce/nonce'+tail)[0]
    P = svm.Load('data_plaintext/plaintext'+tail)[0]
    CT = svm.Load('data_ciphertag/ciphertag'+tail)[0]
    print('  Table loading')
    BP_table = svm.Load('Tables/'+self.tag+'/table_'+str(Tr).zfill(4)+'.npy')
    Enumeration = enumeration.Enumerator(BP_table)
    print('  Key Enumeration')
    for count in range(1, self.iteration_time+1):
      Units, Prob = Enumeration.Next_one()
      prediction = Find_Prediction(Units)
      Results = ENC_128(prediction, N, '', P)
      if Results==CT:
        break
    print('  ANS    : 0x'+ANS)
    print('  Predict: 0x'+prediction)
    print('  Correct?', ANS==prediction)
    print('  Enumeration Number:', count)
    svm.Save(('Iterations/'+self.tag+'/iterate_'+str(Tr).zfill(4)+'.npy'), count)
    svm.Save(('Predictions/'+self.tag+'/predict_'+str(Tr).zfill(4)+'.npy'), prediction)
    return

if __name__=='__main__':
  #Ex: python3 table_enumerate.py L01 0 10
  SASCA_Proc = Evaluation(sys.argv[1])
  lower = int(sys.argv[2])
  upper = int(sys.argv[3])
  tS = time.time()
  for t in range(lower, upper):
    print('======================================')
    print(time.asctime())
    print('data #'+str(t).zfill(4))
    SASCA_Proc.calculate(t)
  tE = time.time()
  total_time = tE-tS
  print('======================================')
  print('finished!')
  print('Exe. time = '+str(total_time))

