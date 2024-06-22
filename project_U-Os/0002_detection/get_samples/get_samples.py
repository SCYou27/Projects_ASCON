import numpy as np
import os
from array import array
import sys
import serv_manager as svm
import h5py
trace_len = 1400000
OFFSET = 14000+455
PPC = 500
OUTSIZE = 2650
GROUP_SZIE = 160
class PREPROC:
  def __init__(self):
    self.FILE_HDF5 = h5py.File('Detect_Samples.hdf5', 'w')
    return
  
  def preprocessing(self, InputDir):
    Samples = []
    OutputTag = 'set_'+InputDir[6:-1]
    # Processing traces.
    for t in range(0, GROUP_SZIE):
      print('=============================================================')
      InputName = InputDir+'trace_'+str(t).zfill(4)+'_0_ch0.bin'
      print(InputName)
      input_file = svm.Open(InputName, 'rb')
      float_array = array('d')
      float_array.frombytes(input_file.read())
      input_file.close()
      trace = []
      for s in range(0, OUTSIZE):
        lower = OFFSET+s*PPC+20
        upper = lower+50
        sample = sum(float_array[lower:upper])
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
    tag = 'DN_'+str(Set_n).zfill(4)
    in_dir = './Raw_'+tag+'/'
    in_zip = '../Raw/Raw_'+tag+'.zip'
    svm.System(('unzip '+in_zip))
    Suc = SEL.preprocessing(in_dir)
    svm.System(('rm -vr '+in_dir))
  SEL.close()
