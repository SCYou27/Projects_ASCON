import numpy as np
import os
from array import array
import sys
import serv_manager as svm
import time

trace_len = 1400000
GROUP_SIZE = 100
TYPE = "VA"
THRESHOLD = 0.99

def read_wave(input_name):
  print(input_name)
  input_file = svm.Open(input_name, 'rb')
  float_array = array('d')
  float_array.frombytes(input_file.read())
  input_file.close()
  if len(float_array)==trace_len:
    return float_array
  else:
    print("Error: length.")
    exit()

def corr_calculate(L, U):
  trace_ref = np.load("../../0001_reference/preproc/ref_trace.npy")
  for Num in range(L, U):
    tS = time.time()
    Corrs = []
    tag = TYPE+"_"+str(Num).zfill(4)
    tr_dir = "./Raw_"+tag+"/"
    tr_zip = "../Raw/Raw_"+tag+".zip"
    cmd = "unzip -qq "+tr_zip
    print(cmd)
    svm.System(cmd)
    Responses = svm.Load((tr_dir+"responses.npy"))
    CTs = svm.Load(("ciphertags/ciphertag_"+str(Num).zfill(4)+".npy"))
    for t in range(0, GROUP_SIZE):
      print("================================================")
      print("checking cipher: "+str((Responses[t]==CTs[t])))
      if Responses[t]!=CTs[t]:
        print("Error: Response and ciphertag do not match.")
        exit()
      tr_name = tr_dir+"trace_"+str(t).zfill(4)+"_0_ch0.bin"
      trace = read_wave(tr_name)
      corr = np.corrcoef(trace, trace_ref)[0][1]
      Corrs.append(corr)
      print(corr)
      if corr<THRESHOLD:
        print("Warning: Correlation coefficient too low.")
        time.sleep(0.3)
    cmd = "rm -r "+tr_dir
    print(cmd)
    svm.System(cmd)
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
