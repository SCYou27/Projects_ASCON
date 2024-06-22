import numpy as np
import sys
import os
import serv_manager as svm
import table_gen
import time


def calculate(IT_Max, L, U):
  Correct = []
  Combinations = []
  Record = []
  for Tr in range(L, U):
    Tail = '_'+str(Tr).zfill(4)+".npy"
    CombName = "Combinations/combine"+Tail
    Search = svm.Load(CombName)
    Combinations.append(Search)
    OutName = "Predictions/predict"+Tail
    Prediction = str(svm.Load(OutName))
    ItName = "Iterations/iterate"+Tail
    ItTimes = svm.Load(ItName)
    if (ItTimes>-1)and(ItTimes<1000):
      Record.append(ItTimes)
    AnsName = "data_key/key"+Tail
    Answer = str(svm.Load(AnsName))
    print("===========================================================")
    print(str(Tr).zfill(4)+":")
    print("Combinations: "+str(Search))
    print("Out: 0x"+Prediction)
    print("Ans: 0x"+Answer)
    if (Prediction==Answer)and(Search<=IT_Max):
      print("Correct!")
      Correct.append(1)
    else:
      print("Failed!")
      Correct.append(0)
  print("===========================================================")
  print("Iteration statistics:")
  strA = str(Correct.count(1))
  print('Number of successfully recovered traces: '+strA)
  if len(Record)==0:
    strB = 'N/A'
    strC = 'N/A'
    strD = 'N/A'
    strE = 'N/A'
  else:
    strB = '{:.3f}'.format(np.median(Record))
    strC = '{:.3f}'.format(np.mean(Record))
    strD = '{:.3f}'.format(np.std(Record))
    strE = '{:.3f}'.format(max(Record))
  print('Med. : '+strB)
  print('Mean : '+strC)
  print('Sigma: '+strD)
  print('Max. : '+strE)
  print(' & '+strA+' & '+strB+' & '+strC+' & '+strD+' & '+strE+'\\\\')
  return

if __name__=='__main__':
  #Ex: python3 statistics.py 100000 0 10
  T = int(sys.argv[1])
  lower = int(sys.argv[2])
  upper = int(sys.argv[3])
  calculate(T, lower, upper)
