import numpy as np
import os
from array import array
import sys
import serv_manager as svm
trace_len = 1400000
GROUP_SIZE = 160

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

def ref_calculate(L, U):
  total = np.array([0.0]*trace_len)
  for Set_n in range(L, U):
    tag = "RE_"+str(Set_n).zfill(4)
    in_dir = "./Raw_"+tag+"/"
    in_zip = "../Raw/Raw_"+tag+".zip"
    svm.System(("unzip "+in_zip))
    Responses = svm.Load((in_dir+"responses.npy"))
    Ciphertags = svm.Load(("ciphertags/ciphertag_"+str(Set_n).zfill(4)+".npy")) 
    for t in range(0, GROUP_SIZE):
      print("=============================================================")
      print("checking cipher: "+str((Responses[t]==Ciphertags[t])))
      if Responses[t]!=Ciphertags[t]:
        print("Error: Response and cihphertag do not match.")
        exit()
      InputName = in_dir+"trace_"+str(t).zfill(4)+"_0_ch0.bin"
      trace = read_wave(InputName)
      total += trace
    svm.System(("rm -vr "+in_dir))
  Average = total/(GROUP_SIZE*(U-L))
  svm.Save("ref_trace.npy", Average)


if __name__=='__main__':
  try:
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
    ref_calculate(lower, upper)
  except:
    ref_calculate(0, 10)
