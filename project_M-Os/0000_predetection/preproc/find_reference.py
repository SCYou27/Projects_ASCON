import numpy as np
import os
import h5py
import time
import sys

GROUPSIZE = 160
SETS = 10
THRESHOLD = 0.99

def load_traces():
  print('Loading Samples...')
  Samples = []
  for t in range(0, SETS):
    fname = '../Samples/Samples_PD_'+str(t).zfill(4)+'.hdf5'
    print('Loading '+fname)
    FILE = h5py.File(fname, 'r')
    Samples.append(FILE['traces'][()])
    FILE.close()
  Samples = np.vstack(Samples)
  return Samples

def find_ref():
  Samples = load_traces()
  print('Calculating Reference Trace...')
  Reference = np.mean(Samples, axis=0)
  print('Saving Reference Trace...')
  np.save('ref_trace.npy', Reference)
  return

def check():
  Samples = load_traces()
  Ref = np.load('ref_trace.npy')
  Corrs = []
  for t in range(0, len(Samples)):
    print('=========================================================================')
    print('trace:', t)
    corr = np.corrcoef(Samples[t], Ref)[0][1]
    Corrs.append(corr)
    print(corr)
    if corr<THRESHOLD:
      print('Warning: smaller than the threshold.')
      time.sleep(0.2)
  np.save('Corrcoefs.npy', Corrs)
  return

if __name__=='__main__':
  if (sys.argv[1]=='all')or(sys.argv[1]=='cal'):
    find_ref()
  if (sys.argv[1]=='all')or(sys.argv[1]=='check'):
    check()
