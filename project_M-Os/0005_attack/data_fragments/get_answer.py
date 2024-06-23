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

def hex2bin(hex_str):
  Size = len(hex_str)*4
  INT = 0
  for t in range(0, len(hex_str)):
    INT <<= 4
    INT += hexdict[hex_str[t]]
  return bin(INT)[2:].zfill(Size)

def Slice(combined_str):
  bin_str = hex2bin(combined_str)
  int_o = 0
  int_e = 0
  for bit in range(0, 64):
    int_o *= 2
    int_e *= 2
    int_o += int(bin_str[2*bit  ])
    int_e += int(bin_str[2*bit+1])
  hex_e = hex(int_e)[2:].zfill(16)
  hex_o = hex(int_o)[2:].zfill(16)
  return (hex_e[0:8]+hex_o[0:8]+hex_e[8:16]+hex_o[8:16])

def get_answers(t):
  print('===============================================================')
  key_name = 'key_set_'+str(t).zfill(4)+'.npy'
  print(key_name)
  key_string_O = str(np.load('data_key/'+key_name))
  key_string_S = Slice(key_string_O)
  key_bytes_O = key_str2bytes(key_string_O)
  key_bytes_S = key_str2bytes(key_string_S)
  np.save(('key_bytes_O/'+key_name), key_bytes_O)
  np.save(('key_bytes_S/'+key_name), key_bytes_S)
  print(key_bytes_O)
  print(key_bytes_S)
  return

if __name__=='__main__':
  L = int(sys.argv[1])
  U = int(sys.argv[2])
  for t in range(L, U):
    get_answers(t)
