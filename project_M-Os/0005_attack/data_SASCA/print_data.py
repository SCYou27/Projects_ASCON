import numpy as np
import sys

def LOAD(t):
  tail = '_'+str(t).zfill(4)+'.npy'
  K = np.load('data_key/key'+tail)
  P = np.load('data_plaintext/plaintext'+tail)
  N = np.load('data_nonce/nonce'+tail)
  CT = np.load('data_ciphertag/ciphertag'+tail)
  C = []
  T = []
  for s in range(0, len(CT)):
    C.append(CT[s][:14])
    T.append(CT[s][14:])
  C = np.array(C)
  T = np.array(T)
  return K, N, P, C, T

def PRINT(Size, K, N, P, C, T):
  print('K:', [K])
  print('N:', N[:Size])
  print('P:', P[:Size])
  print('C:', C[:Size])
  print('T:', T[:Size])
  return

if __name__=='__main__':
  K, N, P, C, T = LOAD(int(sys.argv[1]))
  PRINT(int(sys.argv[2]), K, N, P, C, T)
