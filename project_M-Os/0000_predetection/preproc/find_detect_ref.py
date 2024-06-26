import numpy as np
import os
import h5py

GROUPSIZE = 160
SETS = 10

print('Loading Samples...')
Samples = []
for t in range(0, SETS):
  fname = '../Samples/Samples_PD_'+str(t).zfill(4)+'.hdf5'
  print('Loading '+fname)
  FILE = h5py.File(fname, 'r')
  Samples.append(FILE['detects'][()])
  FILE.close()
Samples = np.vstack(Samples)
print('Calculating Reference Trace...')
Reference = np.mean(Samples, axis=0)
print('Saving Reference Trace...')
np.save('ref_detection.npy', Reference)


