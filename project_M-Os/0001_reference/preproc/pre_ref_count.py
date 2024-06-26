import numpy as np
import os
import sys
import serv_manager as svm
import h5py

trace_len = 60000
GROUP_SIZE = 160

def read_wave(input_name):
  print(input_name)
  Traces = []
  FILE = h5py.File(input_name, 'r')
  Traces_int = FILE['traces'][()]
  R = FILE['responses'][()]
  CT = FILE['ciphertags'][()]
  FILE.close()
  for t in range(0, GROUP_SIZE):
    print(input_name+': Trace #'+str(t).zfill(4))
    Traces.append(Traces_int[t])
  return np.vstack(Traces), np.count_nonzero(R==CT)==GROUP_SIZE

def ref_calculate(L, U):
  Traces = []
  for Set_n in range(L, U):
    trace_block, check = read_wave('../Samples/Samples_RE_'+str(Set_n).zfill(4)+'.hdf5')
    if check==False:
      exit()
    Traces.append(trace_block)
  Average = np.mean(np.vstack(Traces), axis=0)
  svm.Save("ref_trace.npy", Average)

def corr_calculate(set_size, set_num):
  trace_ref = np.load("ref_trace.npy")
  Corrs = []
  for Num in range(0, set_num):
    trace_block, check = read_wave('../Samples/Samples_RE_'+str(Num).zfill(4)+'.hdf5')
    for t in range(0, set_size):
      print("================================================")
      corr = np.corrcoef(trace_block[t], trace_ref)[0][1]
      Corrs.append(corr)
      print(corr)
  svm.Save("corrcoef.npy", Corrs)
  return

def show_statistics(set_size, set_num, Times):
  total_size = set_size*set_num
  Corrs = np.load("corrcoef.npy")
  Mean = np.mean(Corrs)
  Std = np.std(Corrs)
  print("=================================================================")
  print("Mean              : "+str(Mean))
  print("Standard deviation: "+str(Std))
  L_bound = Mean-Times*Std
  U_bound = Mean+Times*Std
  print("Interval ("+str(Times)+"x): ["+str(L_bound)+", "+str(U_bound)+"]")
  print("=================================================================")
  print("Non-qualified traces:")
  for t in range(0, total_size):
    if (Corrs[t]<L_bound) or (Corrs[t]>U_bound):
        print("Index: "+str(t).zfill(4)+", Corrcoef: "+str(Corrs[t]))
  return

if __name__=='__main__':
  Tag = sys.argv[1]
  if (Tag=="ref") or (Tag=="all"):
    ref_calculate(0, 10)
  if (Tag=="find") or (Tag=="all"):
    corr_calculate(GROUP_SIZE, 10)
  if (Tag=="show") or (Tag=="all"):
    Ts = int(sys.argv[2])
    show_statistics(GROUP_SIZE, 10, Ts)
