import h5py
import numpy as np

class Trace_Reader:
  def __init__(self, T_Dir, L_Num):
    self.T_Dir = T_Dir
    self.L_Num = L_Num
    self.FILEs = []
    for L in range(0, self.L_Num):
      fname = self.T_Dir+'part_'+str(L).zfill(2)+'.hdf5'
      print('Open '+fname)
      self.FILEs.append(h5py.File(fname, 'r'))
    return
  
  def read(self, leaf, t):
    trace = self.FILEs[leaf]['Traces'][t]
    return trace
  
  def close(self):
    for L in range(0, self.L_Num):
      print('Close Leaf '+str(L).zfill(2))
      self.FILEs[L].close()
    return

if __name__=='__main__':
  TR = Trace_Reader('../Resample_HDF5/', 10)
  trace = TR.read(9, 999)
  print(trace)
  print(np.shape(trace))
  TR.close()

