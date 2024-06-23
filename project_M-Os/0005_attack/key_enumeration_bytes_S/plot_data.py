import numpy as np
import sys
import os
import serv_manager as svm
import table_gen
import time

BOUNDS = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

def calculate(LEAVES, L, U):
  OUT_PRINT_Part1 = ''
  OUT_PRINT_Part2 = ''
  for leaf in LEAVES:
    #print('===========================================================')
    #print('Leaves: '+str(leaf).zfill(2))
    Record = []
    for t in range(0, len(BOUNDS)):
      Record.append([])
    BP_Ends = []
    for Tr in range(L, U):
      Tail = '_'+str(Tr).zfill(4)+'.npy'
      IterName = 'Iterations/L'+str(leaf).zfill(4)+'/iterate'+Tail
      End = svm.Load(IterName)
      OutName = 'Predictions/L'+str(leaf).zfill(4)+'/predict'+Tail
      Prediction = str(svm.Load(OutName))
      AnsName = 'data_key/key_set'+Tail
      Answer = str(svm.Load(AnsName))
      #print('===========================================================')
      #print(str(Tr).zfill(4)+':')
      #print('Out: 0x'+Prediction)
      #print('Ans: 0x'+Answer)
      for b in range(0, len(BOUNDS)):
        if (Prediction==Answer)and(End<=BOUNDS[b]):
          Record[b].append(End)
    print('===========================================================')
    print('Enumeration iterations calculating')
    OUT_PRINT_Part1 += ('===========================================================\nLeaves: '+str(leaf).zfill(2)+'\n\\hline\n')
    Final_Line = 'L'+str(leaf).zfill(4)
    for b in range(0, len(BOUNDS)):
      Head = 'Key with Tree BP (bytes and L'+str(leaf).zfill(2)+') & '+str(BOUNDS[b])
      strA = '{:.3f}'.format(len(Record[b])/(U-L))
      Final_Line += (' & '+strA)
      if len(Record[b])==0:
        strB = 'N/A'
        strC = 'N/A'
        strD = 'N/A'
        strE = 'N/A'
      else:
        strB = '{:.3f}'.format(np.median(Record[b]))
        strC = '{:.3f}'.format(np.mean(Record[b]))
        strD = '{:.3f}'.format(np.std(Record[b]))
        strE = '{:.3f}'.format(max(Record[b]))
      OUT_PRINT_Part1+=(Head+' & '+strA+' & '+strB+' & '+strC+' & '+strD+' & '+strE+'\\\\\n\\hline\n')
    OUT_PRINT_Part2+=(Final_Line+'\\\\\n\\hline\n')
  print('===========================================================')
  print('Enumeration iterations:')
  print(OUT_PRINT_Part1)
  print('===========================================================')
  print(OUT_PRINT_Part2)
  return

if __name__=='__main__':
  #Ex: python3 plot_data.py 0 10
  lower = int(sys.argv[1])
  upper = int(sys.argv[2])
  calculate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100], lower, upper)

