import h5py
import numpy as np

class Trace_Reader:
  def __init__(self, T_Dir, Tr):
    fname = T_Dir+'Samples_TS_'+str(Tr).zfill(4)+'.hdf5'
    print('Open '+fname)
    self.FILE = h5py.File(fname, 'r')
    return
  
  def read(self, leaf):
    trace = self.FILE['traces'][leaf]
    resampled_trace = []
    for t in range(0, len(trace)//5):
      resampled_trace.append(sum(trace[(5*t):(5*t+5)]))
    return np.array(resampled_trace)
  
  def close(self):
    self.FILE.close()
    return

if __name__=='__main__':
  TR = Trace_Reader('../Samples/', 10)
  trace = TR.read(37)
  print(trace)
  print(np.shape(trace))
  TR.close()

