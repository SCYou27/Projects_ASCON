import numpy as np
import os
from array import array
import sys
import serv_manager as svm
import time
import h5py

trace_len = 1400000
OFFSET = 14000+455
RATE_10 = 50
NUM_CLK = 2560
NUM_SAM = 500
OUTSIZE_10 = NUM_CLK*10
LOWER = OFFSET
UPPER = OFFSET+NUM_CLK*NUM_SAM

TYPE = 'VA'
GROUP_SIZE = 100
BLOCK_SIZE = 10

def preprocessing(Input_Name):
  # Processing traces.
  Small_Block = []
  print('=============================================================')
  print('Loading', Input_Name)
  FILE = h5py.File(Input_Name, 'r')
  Traces_int = FILE['traces'][()]
  Gains = FILE['gains'][()]
  Offsets = FILE['offsets'][()]
  FILE.close()
  print('Shape of raw traces:', np.shape(Traces_int))
  for t in range(0, GROUP_SIZE):
    print('=============================================================')
    print((Input_Name+', trace:'+str(t).zfill(4)))
    Samples_10 = []
    Trace = Traces_int[t]*Gains[t]+Offsets[t]
    Trace = Trace[LOWER:UPPER]
    for S in range(0, OUTSIZE_10):
      lower = S*RATE_10
      upper = lower+RATE_10
      sample = sum(Trace[lower:upper])
      Samples_10.append(sample)
    Small_Block.append(Samples_10)
  return np.vstack(Small_Block)

def block_preproc(block_num):
  L = block_num*BLOCK_SIZE
  U = L+BLOCK_SIZE
  tS = time.time()
  Block = []
  for Set_n in range(L, U):
    tag = TYPE+'_'+str(Set_n).zfill(4)
    in_name = '../Raw/Raw_'+tag+'.hdf5'
    Block.append(preprocessing(in_name))
  print('=========================================')
  block_name = 'part_'+str(block_num).zfill(2)+'.hdf5'
  Block = np.vstack(Block)
  print('Shape of block:', np.shape(Block))
  print('Saving '+block_name)
  FILE = h5py.File(block_name, 'w')
  FILE.create_dataset('Traces', np.shape(Block), 'f8', compression="gzip", compression_opts=9, data=Block)
  FILE.close()
  print('=========================================')
  tE = time.time()
  print((tE-tS))
  return

if __name__=='__main__':
  lower = int(sys.argv[1])
  upper = int(sys.argv[2])
  for part in range(lower, upper):
    block_preproc(part)

