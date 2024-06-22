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
NUM_CLK = 2650
NUM_SAM = 500
OUTSIZE_10 = NUM_CLK*10
LOWER = OFFSET
UPPER = OFFSET+NUM_CLK*NUM_SAM

TYPE = 'VA'
GROUP_SIZE = 100
BLOCK_SIZE = 10

def preprocessing(InputDir):
  # Processing traces.
  Small_Block = []
  for t in range(0, GROUP_SIZE):
    print('=============================================================')
    InputName = InputDir+'trace_'+str(t).zfill(4)+'_0_ch0.bin'
    print(InputName)
    Samples_10 = []
    input_file = svm.Open(InputName, 'rb')
    float_array = array('d')
    float_array.frombytes(input_file.read())
    Raw_Trace = float_array[LOWER:UPPER]
    input_file.close()
    for S in range(0, OUTSIZE_10):
      lower = S*RATE_10
      upper = lower+RATE_10
      sample = sum(Raw_Trace[lower:upper])
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
    tag_10 = TYPE+'_10_'+str(Set_n).zfill(4)
    in_dir = 'Raw_'+tag+'/'
    in_zip = '../Raw/Raw_'+tag+'.zip'
    svm.System(('unzip '+in_zip))
    Block.append(preprocessing(in_dir))
    svm.System(('rm -vr '+in_dir))
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

