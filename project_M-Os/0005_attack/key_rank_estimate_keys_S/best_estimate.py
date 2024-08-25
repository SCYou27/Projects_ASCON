import numpy as np
import sys
import os
import time
import serv_manager as svm
import enumeration
import histogram_GE as GE
import math

iteration_time = 2**20
Target_Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]
BIN_NUM = 60000
ROUND_DIGIT = 5

class Evaluation:
  def __init__(self):
    self.iteration_time = iteration_time
    return
  
  def calculate(self, Tr):
    tail = '_'+str(Tr).zfill(4)+'.npy'
    ANS_frags = svm.Load('key_bytes_S/key'+tail)
    for L in Target_Numbers:
      print('  ++++++++++++++++++++++++++++++++++++++++++++')
      print('  Key set #'+str(Tr).zfill(4)+' estimating with '+str(L).zfill(4)+' traces.')
      print('  Table loading...')
      BP_table = svm.Load('Tables/L'+str(L).zfill(4)+'/table_'+str(Tr).zfill(4)+'.npy')
      print('  Rank estimating...')
      Step = round((np.max(BP_table[:,:,1])-np.min(BP_table[:,:,1]))/BIN_NUM, ROUND_DIGIT)
      L_B, U_B, log_L, log_U = GE.Estimate_GE(ANS_frags, BP_table, Step)
      print('  lower bound:', L_B, '(2^'+str(log_L)+')')
      print('  upper bound:', U_B, '(2^'+str(log_U)+')')
      Best = (log_L+log_U)/2
      if L_B>self.iteration_time:
        print('  Lower bound larger than search capacity, key enumeration skipped.')
        print('  Geometric mean of lower and upper bounds: (2^'+str(Best)+')')
      else:
        print('  Key enumerating...')
        Enumeration = enumeration.Enumerator(BP_table)
        for count in range(1, self.iteration_time+1):
          Units, Prob = Enumeration.Next_one()
          if (ANS_frags==np.array(Units, dtype=np.uint8)).all():
            print('  Hit!')
            Best = math.log2(count)
            print('  Enumeration Number:', count, '(2^'+str(Best)+')')
            break
          if count==self.iteration_time:
            print('  Not found!')
      svm.Save(('Rank_log/L'+str(L).zfill(4)+'/rank_log_'+str(Tr).zfill(4)+'.npy'), np.array([log_L, Best, log_U]))
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

