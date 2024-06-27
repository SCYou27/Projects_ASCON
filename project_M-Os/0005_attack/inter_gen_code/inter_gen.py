import ascon as official
import random
import sys
import time
import numpy as np

GROUP_SIZE = 100

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}


class GENERATOR:
  def __init__(self, variant):
    self.variant = variant
    self.Key_Bytes = []
    for set_n in range(0, 1000):
      key = official.get_random_bytes(16)
      self.Key_Bytes.append(key)
    return
  
  def gen_single(self, group_index, count):
    print("  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("  #"+str(count).zfill(4)+":")
    key = self.Key_Bytes[group_index]
    nonce = official.get_random_bytes(16)
    A_data = official.get_random_bytes(0)
    if self.variant=="Ascon-128":
      P_data = official.get_random_bytes(7)
    elif self.variant=="Ascon-128a":
      P_data = official.get_random_bytes(15)
    C_data = official.ascon_encrypt(key, nonce, A_data, P_data, self.variant)
    R_data = official.ascon_decrypt(key, nonce, A_data, C_data, self.variant)
    if R_data == None: 
      print("verification failed in official codes.")
      exit()
    official.demo_print([("K",key),("N",nonce),("P",P_data),("A",A_data),("C+T",C_data),("R",R_data)])
    if P_data!=R_data:
      print("wrong answer in official codes")
      exit()
    K_off = key.hex()
    N_off = nonce.hex()
    P_off = P_data.hex()
    C_off = C_data.hex()
    return K_off, N_off, P_off, C_off
  
  def gen_multiple(self, group_index):
    KEYS = []
    NONCES = []
    PLAINTEXTS = []
    CIPHERTAGS = []
    for t in range(0, GROUP_SIZE):
      key, nonce, plaintext, ciphertag = self.gen_single(group_index, t)
      KEYS.append(key)
      NONCES.append(nonce)
      PLAINTEXTS.append(plaintext)
      CIPHERTAGS.append(ciphertag)
    np.save(("keys/key_"+str(group_index).zfill(4)+".npy"), KEYS)
    np.save(("nonces/nonce_"+str(group_index).zfill(4)+".npy"), NONCES)
    np.save(("plaintexts/plaintext_"+str(group_index).zfill(4)+".npy"), PLAINTEXTS)
    np.save(("ciphertags/ciphertag_"+str(group_index).zfill(4)+".npy"), CIPHERTAGS)
    return
  
if __name__=='__main__':
  tS = time.time()
  Variant = "Ascon-128" # either 'Ascon-128' or 'Ascon-128a'
  if (Variant=='Ascon-128')or(Variant=='Ascon-128a'):
    GEN = GENERATOR(Variant)
    for g in range(0, 1000):
      print("===================================================================")
      print("Group: #"+str(g).zfill(4))
      GEN.gen_multiple(g)
  tE = time.time()
  print((tE-tS))

