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

Target_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]

def Find_Prediction(Units):
  Value = ''
  for t in range(0, len(Units)):
    Value += hex(Units[t])[2:].zfill(2)
  return Value

class Evaluation:
  def __init__(self):
    self.iteration_time = iteration_time
    return
  
  def calculate(self, Tr):
    tail = '_set_'+str(Tr).zfill(4)+'.npy'
    ANS = str(svm.Load('data_key/key'+tail))
    N = svm.Load('data_nonce/nonce'+tail)[0]
    P = svm.Load('data_plaintext/plaintext'+tail)[0]
    CT = svm.Load('data_ciphertag/ciphertag'+tail)[0]
    for L in Target_Numbers:
      BP_table = svm.Load('Tables/L'+str(L).zfill(4)+'/table_'+str(Tr).zfill(4)+'.npy') 
      print('  ++++++++++++++++++++++++++++++++++++++++++++')
      print('  Key Enumeration: '+str(L).zfill(4)+' traces.')
      Enumeration = enumeration.Enumerator(BP_table)
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
      svm.Save(('Iterations/L'+str(L).zfill(4)+'/iterate_'+str(Tr).zfill(4)+'.npy'), count)
      svm.Save(('Predictions/L'+str(L).zfill(4)+'/predict_'+str(Tr).zfill(4)+'.npy'), prediction)
    return

if __name__=='__main__':
  #Ex: python3 Search_Procedure.py 0 10
  SASCA_Proc = Evaluation()
  lower = int(sys.argv[1])
  upper = int(sys.argv[2])
  tS = time.time()
  for t in range(lower, upper):
    print('======================================')
    print(time.asctime())
    print('data #'+str(t).zfill(4))
    SASCA_Proc.calculate(t)
  print('======================================')
  tE = time.time()
  total_time = tE-tS
  print('======================================')
  print('finished!')
  print('Exe. time = '+str(total_time))

