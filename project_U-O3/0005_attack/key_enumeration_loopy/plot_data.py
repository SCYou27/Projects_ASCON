import numpy as np
import sys
import os
import serv_manager as svm
#import table_gen
import time

BOUNDS = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]

def calculate(tag, L, U):
  OUT_PRINT_Part1 = ''
  OUT_PRINT_Part2 = ''
  Record = []
  for t in range(0, len(BOUNDS)):
    Record.append([])
  BP_Ends = []
  for Tr in range(L, U):
    Tail = '_'+str(Tr).zfill(4)+'.npy'
    IterName = 'Iterations/'+tag+'/iterate'+Tail
    End = svm.Load(IterName)
    OutName = 'Predictions/'+tag+'/predict'+Tail
    Prediction = str(svm.Load(OutName))
    AnsName = 'data_key/key'+Tail
    Answer = str(svm.Load(AnsName))
    for b in range(0, len(BOUNDS)):
      if (Prediction==Answer)and(End<=BOUNDS[b]):
        Record[b].append(End)
  #print('Enumeration iterations calculating')
  OUT_PRINT_Part1 += ('===========================================================\n')
  Final_Line = tag
  for b in range(0, len(BOUNDS)):
    Head = 'Key Enumerations & '+str(BOUNDS[b])
    strA = '{:.3f}'.format((len(Record[b])/(U-L)))
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
  #print('===========================================================')
  #print('Enumeration iterations:')
  #print(OUT_PRINT_Part1)
  #print('===========================================================')
  print(OUT_PRINT_Part2)
  return

if __name__=='__main__':
  tag = sys.argv[1]
  lower = int(sys.argv[2])
  upper = int(sys.argv[3])
  calculate(tag, lower, upper)

