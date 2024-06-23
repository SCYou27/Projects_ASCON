import numpy as np
import sys
import os
import time
import serv_manager as svm
import get_tables_MASK as get_tables
import trace_reader_multi as trace_reader
import tree_BP_multi_mask as tree_BP

TRACE_DIR = '../Samples/'

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}

Target_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]

def get_tag_numbers(TAG):
  Numbers = []
  for t in range(0, 16):
    Numbers.append(16*hexdict[TAG[(2*t)]]+hexdict[TAG[(2*t+1)]])
  return np.array(Numbers)

def hex2bin(hex_str):
  Size = len(hex_str)*4
  INT = 0
  for t in range(0, len(hex_str)):
    INT <<= 4
    INT += hexdict[hex_str[t]]
  return bin(INT)[2:].zfill(Size)

def Slice(combined_str):
  bin_str = hex2bin(combined_str)
  int_o = 0
  int_e = 0
  for bit in range(0, 64):
    int_o *= 2
    int_e *= 2
    int_o += int(bin_str[2*bit  ])
    int_e += int(bin_str[2*bit+1])
  hex_e = hex(int_e)[2:].zfill(16)
  hex_o = hex(int_o)[2:].zfill(16)
  return (hex_e[0:8]+hex_o[0:8]+hex_e[8:16]+hex_o[8:16])

class Evaluation:
  def __init__(self):
    self.TEMPLATES = get_tables.Template_Recovering()
    return
  
  def calculate(self, Tr):
    tail = '_set_'+str(Tr).zfill(4)+'.npy'
    CT = svm.Load('data_ciphertag/ciphertag'+tail)
    TREE_BPer = tree_BP.TREE_BP(8)
    READER = trace_reader.Trace_Reader(TRACE_DIR, Tr)
    for L in range(0, 100):
      trace = READER.read(L)
      KEY_t, K_A_t, K_B_t, L_A_t, L_B_t = self.TEMPLATES.recover(trace)
      tag_numbers = get_tag_numbers(Slice(CT[L][14:46]))
      BP_table = TREE_BPer.propagate_add(KEY_t, K_A_t, K_B_t, L_A_t, L_B_t, tag_numbers)
      if (L+1) not in Target_Numbers:
        continue
      print('  ++++++++++++++++++++++++++++++++++++++++++++')
      print('  Key Table: '+str(L+1).zfill(4)+' traces.')
      svm.Save(('Tables/L'+str(L+1).zfill(4)+'/table_'+str(Tr).zfill(4)+'.npy'), np.array(BP_table))
    READER.close()
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

