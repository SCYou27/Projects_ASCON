import ascon_aead as AEAD
import numpy as np
import sys

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}

GROUP_SIZE = 160
SET_NUMBER = 400

def hex2num(str_hex):
  Number = 0
  for t in range(0, len(str_hex)):
    Number <<= 4
    Number += hexdict[str_hex[t]]
  return Number

def set_calculate(set_n):
  template = AEAD.ASCON_AEAD(True)
  ENC_128 = template.ASCON_128.Enc
  print("=====================================================")
  print("Calculating set #"+str(set_n).zfill(4))
  Keys = np.load(('keys/key_'+str(set_n).zfill(4)+'.npy'))
  Nonces = np.load(('nonces/nonce_'+str(set_n).zfill(4)+'.npy'))
  Plaintexts = np.load(('plaintexts/plaintext_'+str(set_n).zfill(4)+'.npy'))
  Ciphertags = np.load(('ciphertags/ciphertag_'+str(set_n).zfill(4)+'.npy'))
  A_DATA = ''
  INTER_INIT = []
  INTER_FIN = []
  for t in range(0, GROUP_SIZE):
    print("=====================================================")
    Key   = Keys[t]
    Nonce = Nonces[t]
    Plaintext  = Plaintexts[t]
    Cipher_Tag = Ciphertags[t]
    print("++ Trace #"+str(t).zfill(4))
    Results, Inter_I, Inter_F = ENC_128(Key, Nonce, A_DATA, Plaintext)
    print(Cipher_Tag == Results)
    print(Cipher_Tag)
    print(Results)
    INTER_INIT.append(Inter_I)
    INTER_FIN.append(Inter_F)
  Dir = "intermediate_HEX/intermediate_trace/"
  np.save((Dir+"I_set_"+str(set_n).zfill(4)+".npy"), INTER_INIT)
  np.save((Dir+"F_set_"+str(set_n).zfill(4)+".npy"), INTER_FIN)
  return

def set_check(set_n):
  print("=====================================================")
  print("Checking set #"+str(set_n).zfill(4))
  Keys = np.load(('keys/key_'+str(set_n).zfill(4)+'.npy'))
  Nonces = np.load(('nonces/nonce_'+str(set_n).zfill(4)+'.npy'))
  Plaintexts = np.load(('plaintexts/plaintext_'+str(set_n).zfill(4)+'.npy'))
  Ciphertags = np.load(('ciphertags/ciphertag_'+str(set_n).zfill(4)+'.npy'))
  A_DATA = ''
  Dir = "intermediate_HEX/intermediate_trace/"
  INTER_INIT = np.load((Dir+"I_set_"+str(set_n).zfill(4)+".npy"))
  INTER_FIN =  np.load((Dir+"F_set_"+str(set_n).zfill(4)+".npy"))
  CHECK_RESULTS = []
  for t in range(0, GROUP_SIZE):
    Inter_I = INTER_INIT[t]
    Inter_F = INTER_FIN[t]
    print("=====================================================")
    Key   = Keys[t]
    Nonce = Nonces[t]
    Plaintext  = Plaintexts[t]
    Cipher_Tag = Ciphertags[t]
    print("++ Trace #"+str(t).zfill(4))
    check = True
    K = hex2num(Key)
    Tag_1 = '80400c0600000000'+Key+Nonce
    if (Inter_I[0]==Tag_1):
      print("check 1: passed!")
    else:
      print("check 1: failed!")
      check = False
    Tag_2 = Plaintext+'80'+Key+hex(K^0x01)[2:].zfill(32)
    Result_2 = hex((hex2num(Inter_I[24])^hex2num(Inter_F[0])))[2:].zfill(80)
    if (Result_2==Tag_2):
      print("check 2: passed!")
    else:
      print("check 2: failed!")
      check = False
    cipher_len = len(Cipher_Tag)-32
    if (Inter_F[0][0:cipher_len]==Cipher_Tag[0:cipher_len]):
      print("check 3: passed!")
    else:
      print("check 3: failed!")
      check = False
    Result_4 = hex((hex2num(Inter_F[24])^K)&(2**128-1))[2:].zfill(32)
    if (Result_4==Cipher_Tag[-32:]):
      print("check 4: passed!")
    else:
      print("check 4: failed!")
      check = False
    print(check)
    CHECK_RESULTS.append(check)
  print(CHECK_RESULTS.count(True))
  if CHECK_RESULTS.count(True)==160:
    return 0
  else:
    return 1


if __name__=='__main__':
  Func = sys.argv[1]
  if (Func=='all')or(Func=='cal'):
    for s in range(0, SET_NUMBER):
      set_calculate(s)
  if (Func=='all')or(Func=='check'):
    A = [True]*SET_NUMBER
    for s in range(0, SET_NUMBER):
      if set_check(s):
        print("Set #"+str(s).zfill(4)+" did not pass.")
        A[s]=False
    for s in range(0, SET_NUMBER):
      print(s, A[s])
    print(str(A.count(True))+" sets passed.")

