import numpy as np
import h5py

def compare(part):
  print('=================================================')
  name = 'part_'+str(part).zfill(2)+'.hdf5'
  print('Checking '+name)
  FILE_OLD = h5py.File('../Resample/HDF5_10/'+name, 'r')
  FILE_NEW = h5py.File(name, 'r')
  Traces_OLD = FILE_OLD['Traces'][()]
  Traces_NEW = FILE_NEW['Traces'][()]
  FILE_OLD.close()
  FILE_NEW.close()
  Number = np.count_nonzero(Traces_OLD==Traces_NEW)
  print('Number of the same values:', Number)
  print('All the same?', Number==(1000*25600))
  return

if __name__=='__main__':
  for p in range(0, 10):
    compare(p)
