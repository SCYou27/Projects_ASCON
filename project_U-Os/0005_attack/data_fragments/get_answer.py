import numpy as np
import sys

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}

A = 2**np.array([7,6,5,4,3,2,1,0], dtype=np.uint8)

def key_str2bytes(Key_String):
  Key_Bytes = []
  for b in range(0, len(Key_String)//2):
    upper = hexdict[Key_String[2*b  ]]
    lower = hexdict[Key_String[2*b+1]]
    Key_Bytes.append(upper*16+lower)
  return np.array(Key_Bytes, dtype=np.uint8)

def key_bytes2frags(Key_Bytes):
  Key_16bits = []
  for f in range(0, len(Key_Bytes)//2):
    Key_16bits.append(256*Key_Bytes[2*f]+Key_Bytes[2*f+1])
  return np.array(Key_16bits, dtype=np.uint16)

def key_bytes2bits(Key_Bytes):
  Key_Bits = []
  for b in range(0, len(Key_Bytes)):
    Key_Bits.append((Key_Bytes[b]&A)//A)
  return np.hstack(Key_Bits)

def get_answers(t):
  print('===============================================================')
  key_name = 'key_'+str(t).zfill(4)+'.npy'
  print(key_name)
  key_string = str(np.load('data_key/'+key_name))
  key_bytes  = key_str2bytes(key_string)
  key_16bits = key_bytes2frags(key_bytes)
  key_bits   = key_bytes2bits(key_bytes)
  np.save(('key_bytes/'+key_name), key_bytes)
  np.save(('key_16bits/'+key_name), key_16bits)
  np.save(('key_bits/'+key_name), key_bits)
  print(key_bytes)
  print(key_16bits)
  print(key_bits)
  return

if __name__=='__main__':
  L = int(sys.argv[1])
  U = int(sys.argv[2])
  for t in range(L, U):
    get_answers(t)
