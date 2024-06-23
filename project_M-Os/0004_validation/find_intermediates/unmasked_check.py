import ascon_aead as AEAD
import numpy as np
import sys

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}

GROUP_SIZE = 160
SET_NUMBER = 10

def hex2num(str_hex):
  Number = 0
  for t in range(0, len(str_hex)):
    Number <<= 4
    Number += hexdict[str_hex[t]]
  return Number

def set_calculate(set_n):
  template = AEAD.ASCON_AEAD(False)
  ENC_128 = template.ASCON_128.Enc
  print("=====================================================")
  print("Calculating set #"+str(set_n).zfill(4))
  Keys = np.load(('keys/key_'+str(set_n).zfill(4)+'.npy'))
  Nonces = np.load(('nonces/nonce_'+str(set_n).zfill(4)+'.npy'))
  Plaintexts = np.load(('plaintexts/plaintext_'+str(set_n).zfill(4)+'.npy'))
  Ciphertags = np.load(('ciphertags/ciphertag_'+str(set_n).zfill(4)+'.npy'))
  A_DATA = ''
  for t in range(0, GROUP_SIZE):
    print("=====================================================")
    Key   = Keys[t]
    Nonce = Nonces[t]
    Plaintext  = Plaintexts[t]
    Cipher_Tag = Ciphertags[t]
    print("++ Trace #"+str(GROUP_SIZE*set_n+t))
    Results = ENC_128(Key, Nonce, A_DATA, Plaintext)
    print(Cipher_Tag == Results)
    print(Cipher_Tag)
    print(Results)
    if Cipher_Tag!=Results:
      print('Error!')
      exit()
  return

if __name__=='__main__':
  for s in range(0, SET_NUMBER):
    set_calculate(s)

