import chacha20
import numpy as np
import h5py

hex2int = {'0': 0, '1': 1, '2': 2, '3': 3,\
           '4': 4, '5': 5, '6': 6, '7': 7,\
           '8': 8, '9': 9, 'a':10, 'b':11,\
           'c':12, 'd':13, 'e':14, 'f':15}

def OutPlusOne(Out_str):
  LastWord = Out_str[-8:]
  INT = 0
  for t in range(0, 8):
    INT <<= 4
    INT += hex2int[LastWord[t]]
  INT += 1
  INT &= ((2**32)-1)
  LastWord = hex(INT)[2:].zfill(8)
  Out_str = Out_str[0:-8]+LastWord
  return Out_str

class PRNG:
  def __init__(self):
    self.tail = '0'*32
    return
  
  def PRNG_Single(self, Counter_str):
    print(Counter_str)
    Out_str = Counter_str[8:16]+Counter_str[0:8]+('0'*(6*8))+self.tail
    Out_str = OutPlusOne(Out_str)
    Out_str = (chacha20.ChaCha20(Out_str))[0:96]
    ############################################
    Out_str = OutPlusOne(Out_str)
    State = chacha20.hex2arr(chacha20.ChaCha20(Out_str))
    ############################################
    Mask_str = ''
    for p in range(0, 16):
      Mask_str += hex(State[p])[2:].zfill(8)
    ############################################
    Out_str = OutPlusOne(Out_str)
    State = chacha20.hex2arr(chacha20.ChaCha20(Out_str))
    ############################################
    for p in range(0, 16):
      Mask_str += hex(State[p])[2:].zfill(8)
    print(Mask_str)
    print('Size:', len(Mask_str))
    ############################################
    Out_str = OutPlusOne(Out_str)
    Out_str = (chacha20.ChaCha20(Out_str))[0:96]
    self.tail = Out_str[-32:]
    return Mask_str

def get_masks(fname):
  FILE = h5py.File(fname, 'r')
  Counters_Str = FILE['counters'][()]
  FILE.close()
  Masks = []
  TASK = PRNG()
  for t in range(0, len(Counters_Str)):
    print('=='+str(t).zfill(4)+'===============================================')
    Masks.append(TASK.PRNG_Single(str(Counters_Str[t])[3:19]))
  return np.array(Masks)

if __name__=='__main__':
  ARR = get_masks('../Samples/Samples_PD_0000.hdf5')
  np.save('test_0000.npy', ARR)
