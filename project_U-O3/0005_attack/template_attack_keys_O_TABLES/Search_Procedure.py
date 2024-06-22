import numpy as np
import sys
import os
import time
import serv_manager as svm
import get_tables_KEY as get_tables
import trace_reader_multi as trace_reader
import table_MLE

TRACE_DIR = '../Resample_HDF5/'

class Evaluation:
  def __init__(self):
    self.TEMPLATES = get_tables.Template_Recovering()
    self.READER = trace_reader.Trace_Reader(TRACE_DIR, 10)
    return
  
  def calculate(self, Tr):
    MLE = table_MLE.TABLE_MLE(8)
    for L in range(0, 10):
      print('  +++++++++++++++++++++++++++++++++++')
      print('  Leaves: '+str(L).zfill(2))
      trace = self.READER.read(L, Tr)
      print('  Probability Evaluation')
      KEY_t = self.TEMPLATES.recover(trace)
      print('  MLE table generation')
      MLE_table = MLE.add_new_table(KEY_t)
      svm.Save(('Tables/L'+str(L+1).zfill(2)+'/table_'+str(Tr).zfill(4)+'.npy'), np.array(MLE_table))
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

