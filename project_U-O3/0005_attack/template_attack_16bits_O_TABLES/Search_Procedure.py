import numpy as np
import sys
import os
import time
import serv_manager as svm
import get_tables_KNT as get_tables
import ascon_aead
import trace_reader_multi as trace_reader
import tree_BP_multi as tree_BP

ENC_128 = ascon_aead.ASCON_AEAD().ASCON_128.Enc

TRACE_DIR = '../Resample_HDF5/'

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}


def Find_Prediction(Units):
  Value = ''
  for t in range(0, len(Units)):
    Value += hex(Units[t])[2:].zfill(4)
  return Value

def tag2twobyte(my_string):
  if len(my_string)==32:
    Output = []
    for fr in range(0, 8):
      Output.append(((16**3)*hexdict[my_string[(4*fr+0)]]\
                    +(16**2)*hexdict[my_string[(4*fr+1)]]\
                    +(16**1)*hexdict[my_string[(4*fr+2)]]\
                    +(16**0)*hexdict[my_string[(4*fr+3)]]))
    return np.array(Output)
  else:
    return np.array([0]*8)

class Evaluation:
  def __init__(self):
    self.TEMPLATES = get_tables.Template_Recovering()
    self.READER = trace_reader.Trace_Reader(TRACE_DIR, 10)
    return
  
  def calculate(self, Tr):
    tail = '_'+str(Tr).zfill(4)+'.npy'
    ANS = str(svm.Load('data_key/key'+tail))
    CT = svm.Load('data_ciphertag/ciphertag'+tail)
    TREE_BPer = tree_BP.TREE_BP(16)
    for L in range(0, 10):
      print('  +++++++++++++++++++++++++++++++++++')
      print('  Leaves: '+str(L).zfill(2))
      Tag_Fragments = tag2twobyte(CT[L][-32:])
      trace = self.READER.read(L, Tr)
      print('  Probability Evaluation')
      KEY_t, Out_t= self.TEMPLATES.recover(trace)
      print('  Belief Propagation')
      BP_table = TREE_BPer.propagate_add(KEY_t, Out_t, Tag_Fragments)
      svm.Save(('Tables/L'+str(L+1).zfill(2)+'/table_'+str(Tr).zfill(4)+'.npy'), np.array(BP_table))
    svm.Save(('Key_fragments/key_frags_'+str(Tr).zfill(4)+'.npy'), tag2twobyte(ANS))
    return
  
  def close(self):
    self.READER.close()
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
  SASCA_Proc.close()
  tE = time.time()
  total_time = tE-tS
  print('======================================')
  print('finished!')
  print('Exe. time = '+str(total_time))

