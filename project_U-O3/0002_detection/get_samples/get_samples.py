import numpy as np
import os
from array import array
import sys
import serv_manager as svm
import h5py
trace_len = 1400000
OFFSET = 14000+455
PPC = 500
OUTSIZE = 2560
GROUP_SZIE = 160
class PREPROC:
  def __init__(self):
    self.FILE_HDF5 = h5py.File('Detect_Samples.hdf5', 'w')
    return
  
  def preprocessing(self, set_n):
    tag = 'DN_'+str(set_n).zfill(4)
    Input_Name = '../Raw/Raw_'+tag+'.hdf5'
    OutputTag = 'set_'+tag
    Samples = []
    print('=============================================================')
    print('Loading', Input_Name)
    FILE = h5py.File(Input_Name, 'r')
    Traces_int = FILE['traces'][()]
    Gains = FILE['gains'][()]
    Offsets = FILE['offsets'][()]
    FILE.close()
    print('Shape of raw traces:', np.shape(Traces_int))
    # Processing traces.
    for t in range(0, GROUP_SZIE):
      print('=============================================================')
      print((Input_Name+', trace:'+str(t).zfill(4)))
      raw_trace = Traces_int[t]*Gains[t]+Offsets[t]
      trace = []
      for s in range(0, OUTSIZE):
        lower = OFFSET+s*PPC+20
        upper = lower+50
        sample = sum(raw_trace[lower:upper])
        trace.append(sample)
      Samples.append(trace)
    Samples = np.array(Samples)
    self.FILE_HDF5.create_dataset(OutputTag, np.shape(Samples), 'f8', compression="gzip", compression_opts=9, data=Samples)
    return True
  
  def close(self):
    self.FILE_HDF5.close()

if __name__=='__main__':
  L = int(sys.argv[1])
  U = int(sys.argv[2])
  SEL = PREPROC()
  for Set_n in range(L, U):
    Suc = SEL.preprocessing(Set_n)
  SEL.close()
