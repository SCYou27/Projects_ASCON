import numpy as np
import sys
import os
import time
import serv_manager as svm
import get_tables_KEY as get_tables
import trace_reader_multi as trace_reader
import table_MLE

TRACE_DIR = '../Samples/'

Target_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]

class Evaluation:
  def __init__(self):
    self.TEMPLATES = get_tables.Template_Recovering()
    return
  
  def calculate(self, Tr):
    MLE = table_MLE.TABLE_MLE(8)
    READER = trace_reader.Trace_Reader(TRACE_DIR, Tr)
    for L in range(0, 100):
      trace = READER.read(L)
      KEY_t = self.TEMPLATES.recover(trace)
      MLE_table = MLE.add_new_table(KEY_t)
      if (L+1) not in Target_Numbers:
        continue
      print('  ++++++++++++++++++++++++++++++++++++++++++++')
      print('  Key Table: '+str(L+1).zfill(4)+' traces.')
      svm.Save(('Tables/L'+str(L+1).zfill(4)+'/table_'+str(Tr).zfill(4)+'.npy'), np.array(MLE_table))
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

