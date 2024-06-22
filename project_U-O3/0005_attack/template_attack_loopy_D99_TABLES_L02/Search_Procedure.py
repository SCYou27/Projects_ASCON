import numpy as np
import sys
import os
import time
import serv_manager as svm
import SASCA_Multi_D99000 as SASCA_Multi
import get_tables
import ascon_aead
import trace_reader_multi as trace_reader

iteration_time = 1000
leaves = 2

ENC_128 = ascon_aead.ASCON_AEAD().ASCON_128.Enc

TRACE_DIR = '../Resample_HDF5/'

def Table_for_enumeration(Table):
  Size = len(Table[0])
  Output = []
  for t in range(0, Size):
    Output.append(np.array([[0.0, Table[0][t]], [1.0, Table[1][t]]]))
  return np.array(Output)

def Find_Prediction(Units):
  Value = 0
  for t in range(0, len(Units)):
    Value<<=1
    if Units[t]==1:
      Value+=1
  return hex(Value)[2:].zfill(32)

class Evaluation:
  def __init__(self):
    self.iteration_time = iteration_time
    self.size_leaves = leaves
    self.TEMPLATES = get_tables.Template_Recovering('CPA')
    self.READER = trace_reader.Trace_Reader(TRACE_DIR, 10)
    return
  
  def calculate(self, Tr):
    tail = '_'+str(Tr).zfill(4)+'.npy'
    ANS = str(svm.Load('data_key/key'+tail))
    N = svm.Load('data_nonce/nonce'+tail)[:self.size_leaves]
    P = svm.Load('data_plaintext/plaintext'+tail)[:self.size_leaves]
    CT = svm.Load('data_ciphertag/ciphertag'+tail)[:self.size_leaves]
    C = []
    T = []
    for t in range(0, self.size_leaves):
      C.append(CT[t][:14])
      T.append(CT[t][14:])
    C = np.array(C)
    T = np.array(T)
    KEY = np.zeros((self.size_leaves, 2, 128))
    F_INP = np.zeros((self.size_leaves, 2, 320))
    I_A = np.zeros((self.size_leaves, 12, 2, 320))
    I_B = np.zeros((self.size_leaves, 12, 2, 320))
    F_A = np.zeros((self.size_leaves, 12, 2, 320))
    F_B = np.zeros((self.size_leaves, 12, 2, 320))
    for s in range(0, self.size_leaves):
      print("Probability Evaluation, Leaf #"+str(s).zfill(2))
      trace = self.READER.read(s, Tr)
      KEY[s], F_INP[s], I_A[s], I_B[s], F_A[s], F_B[s] = self.TEMPLATES.recover(trace)
    Test = SASCA_Multi.SASCA_Procedure(KEY, F_INP, I_A, I_B, F_A, F_B, N, P, C, T)
    End, _ = Test.calculate(self.iteration_time)
    Table = Test.Ext_Factor.Zeta()
    svm.Save(("Tables/table_"+str(Tr).zfill(4)+".npy"), Table_for_enumeration(Table))
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
    print("======================================")
    print(time.asctime())
    print("data #"+str(t).zfill(4))
    SASCA_Proc.calculate(t)
  SASCA_Proc.close()
  tE = time.time()
  total_time = tE-tS
  print("======================================")
  print("finished!")
  print("Exe. time = "+str(total_time))

