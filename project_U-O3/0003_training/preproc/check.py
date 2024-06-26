import numpy as np
import os
from array import array
import sys
import serv_manager as svm
import time
import h5py

trace_len = 1400000
GROUP_SIZE = 160
TYPE = "TR"
THRESHOLD = 0.99

def corr_calculate(L, U):
  trace_ref = np.load("../../0001_reference/preproc/ref_trace.npy")
  for Num in range(L, U):
    print("=====================================================")
    tS = time.time()
    Corrs = []
    tag = TYPE+"_"+str(Num).zfill(4)
    input_name = "../Raw/Raw_"+tag+".hdf5"
    print(input_name)
    FILE = h5py.File(input_name, 'r')
    Traces_int = FILE['traces'][()]
    Gains = FILE['gains'][()]
    Offsets = FILE['offsets'][()]
    R = FILE['responses'][()]
    CT = FILE['ciphertags'][()]
    FILE.close()
    if np.count_nonzero(R==CT)!=GROUP_SIZE:
      print("Check Failed!")
      exit()
    for t in range(0, GROUP_SIZE):
      print("+++++++++++++++++++++++++++++++++++++++++++++++")
      print(input_name+': Trace #'+str(t).zfill(4))
      trace = Traces_int[t]*Gains[t]+Offsets[t]
      corr = np.corrcoef(trace, trace_ref)[0][1]
      Corrs.append(corr)
      print(corr)
      if corr<THRESHOLD:
        print("Warning: Correlation coefficient too low.")
        time.sleep(0.3)
    svm.Save(("Corrcoef/corrcoef_set_"+str(Num).zfill(4)+".npy"), Corrs)
    tE = time.time()
    print("Exe. time: "+str(tE-tS))
  return

def show_statistics(L, U):
  for set_n in range(L, U):
    print("==========================================================")
    print("Set #"+str(set_n).zfill(4))
    Corrs = svm.Load(("Corrcoef/corrcoef_set_"+str(set_n).zfill(4)+".npy"))
    ALL_PASSED = True
    for t in range(0, GROUP_SIZE):
      if Corrs[t]<THRESHOLD:
        ALL_PASSED = False
        print("Set: "+str(set_n).zfill(4)+", Index: "+str(t).zfill(4)+", Corrcoef: "+str(Corrs[t]))
    if ALL_PASSED:
      print("No traces under threshold in this set.")
  return

if __name__=='__main__':
  Tag = sys.argv[1]
  lower = int(sys.argv[2])
  upper = int(sys.argv[3])
  if (Tag=="find") or (Tag=="all"):
    corr_calculate(lower, upper)
  if (Tag=="show") or (Tag=="all"):
    show_statistics(lower, upper)
