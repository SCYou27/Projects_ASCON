import numpy as np
import sys
import prng
import masked_ascon 
import time

GROUP_SIZE = 100
SET_NUM = 40
GROUP_TYPE = 'VA'

hex2int = {'0': 0, '1': 1, '2': 2, '3': 3,\
           '4': 4, '5': 5, '6': 6, '7': 7,\
           '8': 8, '9': 9, 'a':10, 'b':11,\
           'c':12, 'd':13, 'e':14, 'f':15}

def StrXOR(str1, str2):
  INT = 0
  for t in range(0, 32):
    INT <<= 4
    INT += (hex2int[str1[t]]^hex2int[str2[t]])&0xf
  return hex(INT)[2:].zfill(32)

def hex2bin(hex_str):
  Size = len(hex_str)*4
  INT = 0
  for t in range(0, len(hex_str)):
    INT <<= 4
    INT += hex2int[hex_str[t]]
  return bin(INT)[2:].zfill(Size)

def Combine(sliced_str):
  hex_E = sliced_str[ 0: 8]+sliced_str[16:24]
  hex_O = sliced_str[ 8:16]+sliced_str[24:32]
  bin_E = hex2bin(hex_E)
  bin_O = hex2bin(hex_O)
  INT = 0
  for bit in range(0, 64):
    INT *= 4
    INT += (2*int(bin_O[bit])+int(bin_E[bit]))
  return hex(INT)[2:].zfill(32)

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

def slice_recover(Sliced_array):
  Combined_array = []
  for t in range(0, len(Sliced_array)):
    Combined_array.append(Combine(Sliced_array[t]))
  return np.array(Combined_array)

def slice_cut(Combined_array):
  Sliced_array = []
  for t in range(0, len(Combined_array)):
    Sliced_array.append(Slice(Combined_array[t]))
  return np.array(Sliced_array)

def calculate():
  ## KEY ####################################################################
  Keys = []
  for set_n in range(0, SET_NUM):
    set_name = 'keys/key_'+str(set_n).zfill(4)+'.npy'
    print(set_name)
    set_keys = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      Keys.append(set_keys[t])
  np.save(('intermediate_HEX/KEY_O_HEX.npy'), Keys)
  ## NONCE ##################################################################
  Nonces = []
  for set_n in range(0, SET_NUM):
    set_name = 'nonces/nonce_'+str(set_n).zfill(4)+'.npy'
    print(set_name)
    set_nonces = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      Nonces.append(set_nonces[t])
  ## PLAINTEXT ##############################################################
  Plaintexts = []
  for set_n in range(0, SET_NUM):
    set_name = 'plaintexts/plaintext_'+str(set_n).zfill(4)+'.npy'
    print(set_name)
    set_plaintexts = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      Plaintexts.append(set_plaintexts[t])
  ## CIPHERTAG ##############################################################
  Ciphertags = []
  for set_n in range(0, SET_NUM):
    set_name = 'ciphertags/ciphertag_'+str(set_n).zfill(4)+'.npy'
    print(set_name)
    set_ciphertags = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      Ciphertags.append(set_ciphertags[t])
  ## MASK ###################################################################
  Masks = []
  for set_n in range(0, SET_NUM):
    fname = '../Samples/Samples_'+GROUP_TYPE+'_'+str(set_n).zfill(4)+'.hdf5'
    print('Processing Mask '+fname)
    Masks.append(prng.get_masks(fname))
  Masks = np.hstack(Masks)
  ## Calculate ##############################################################
  print('Calculating masked ASCON-128')
  sliced_KEY = []
  sliced_K_A = []
  sliced_K_B = []
  sliced_L_A = []
  sliced_L_B = []
  sliced_T_A = []
  sliced_T_B = []
  sliced_TAG = []
  combined_K_A = []
  combined_K_B = []
  combined_L_A = []
  combined_L_B = []
  combined_T_A = []
  combined_T_B = []
  combined_TAG = []
  for t in range(0, GROUP_SIZE*SET_NUM):
    if t%GROUP_SIZE==0:
      print('ASCON-128 trace '+str(t), time.asctime())
    cipher, tag, key_A, key_B, last_A, last_B, tag_A, tag_B = masked_ascon.My_Enc(Keys[t], Nonces[t], Plaintexts[t], Masks[t], True)
    if (cipher+tag)!=Ciphertags[t]:
      print('Error in trace '+str(t))
      exit()
    sliced_KEY.append(StrXOR(key_A, key_B))
    sliced_K_A.append(key_A)
    sliced_K_B.append(key_B)
    sliced_L_A.append(last_A)
    sliced_L_B.append(last_B)
    sliced_T_A.append(tag_A)
    sliced_T_B.append(tag_B)
    sliced_TAG.append(StrXOR(tag_A, tag_B))
  print('Saving sliced values')
  np.save(('intermediate_HEX/KEY_S_HEX.npy'), sliced_KEY)
  np.save(('intermediate_HEX/K_A_S_HEX.npy'), sliced_K_A)
  np.save(('intermediate_HEX/K_B_S_HEX.npy'), sliced_K_B)
  np.save(('intermediate_HEX/L_A_S_HEX.npy'), sliced_L_A)
  np.save(('intermediate_HEX/L_B_S_HEX.npy'), sliced_L_B)
  np.save(('intermediate_HEX/T_A_S_HEX.npy'), sliced_T_A)
  np.save(('intermediate_HEX/T_B_S_HEX.npy'), sliced_T_B)
  np.save(('intermediate_HEX/TAG_S_HEX.npy'), sliced_TAG)
  print('Processing combined values')
  np.save(('intermediate_HEX/K_A_O_HEX.npy'), slice_recover(sliced_K_A))
  np.save(('intermediate_HEX/K_B_O_HEX.npy'), slice_recover(sliced_K_B))
  np.save(('intermediate_HEX/L_A_O_HEX.npy'), slice_recover(sliced_L_A))
  np.save(('intermediate_HEX/L_B_O_HEX.npy'), slice_recover(sliced_L_B))
  np.save(('intermediate_HEX/T_A_O_HEX.npy'), slice_recover(sliced_T_A))
  np.save(('intermediate_HEX/T_B_O_HEX.npy'), slice_recover(sliced_T_B))
  np.save(('intermediate_HEX/TAG_O_HEX.npy'), slice_recover(sliced_TAG))
  return

def check_equal(array_1, array_2):
  correct = np.count_nonzero((array_1==array_2))
  if correct==GROUP_SIZE*SET_NUM:
    print('Passed!')
  else:
    print('Failed!')
    exit()
  return

def check():
  ## KEY ####################################################################
  print('===================================================================')
  print('checking keys (raw)')
  Keys = []
  for set_n in range(0, SET_NUM):
    set_name = 'keys/key_'+str(set_n).zfill(4)+'.npy'
    set_keys = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      Keys.append(set_keys[t])
  Keys = np.array(Keys)
  Combined_KEY = np.load('intermediate_HEX/KEY_O_HEX.npy')
  check_equal(Keys, Combined_KEY)
  print('===================================================================')
  print('checking keys (sliced)')
  Sliced_KEY = np.load('intermediate_HEX/KEY_S_HEX.npy')
  check_equal(Sliced_KEY, slice_cut(Combined_KEY))
  ## TAG ####################################################################
  print('===================================================================')
  print('checking tags (raw)')
  Tags = []
  for set_n in range(0, SET_NUM):
    set_name = 'ciphertags/ciphertag_'+str(set_n).zfill(4)+'.npy'
    set_tags = np.load(set_name)
    for t in range(0, GROUP_SIZE):
        Tags.append(set_tags[t][14:46])
  Tags = np.array(Tags)
  Combined_TAG = np.load('intermediate_HEX/TAG_O_HEX.npy')
  check_equal(Tags, Combined_TAG)
  print('===================================================================')
  print('checking tags (sliced)')
  Sliced_TAG = np.load('intermediate_HEX/TAG_S_HEX.npy')
  check_equal(Sliced_TAG, slice_cut(Combined_TAG))
  ## K_A ####################################################################
  print('===================================================================')
  print('checking K_A')
  Combined_K_A = np.load('intermediate_HEX/K_A_O_HEX.npy')
  Sliced_K_A   = np.load('intermediate_HEX/K_A_S_HEX.npy')
  check_equal(Sliced_K_A, slice_cut(Combined_K_A))
  ## K_B ####################################################################
  print('===================================================================')
  print('checking K_B')
  Combined_K_B = np.load('intermediate_HEX/K_B_O_HEX.npy')
  Sliced_K_B   = np.load('intermediate_HEX/K_B_S_HEX.npy')
  check_equal(Sliced_K_B, slice_cut(Combined_K_B))
  ## L_A ####################################################################
  print('===================================================================')
  print('checking L_A')
  Combined_L_A = np.load('intermediate_HEX/L_A_O_HEX.npy')
  Sliced_L_A   = np.load('intermediate_HEX/L_A_S_HEX.npy')
  check_equal(Sliced_L_A, slice_cut(Combined_L_A))
  ## L_B ####################################################################
  print('===================================================================')
  print('checking L_B')
  Combined_L_B = np.load('intermediate_HEX/L_B_O_HEX.npy')
  Sliced_L_B   = np.load('intermediate_HEX/L_B_S_HEX.npy')
  check_equal(Sliced_L_B, slice_cut(Combined_L_B))
  ## T_A ####################################################################
  print('===================================================================')
  print('checking T_A')
  Combined_T_A = np.load('intermediate_HEX/T_A_O_HEX.npy')
  Sliced_T_A   = np.load('intermediate_HEX/T_A_S_HEX.npy')
  check_equal(Sliced_T_A, slice_cut(Combined_T_A))
  ## T_B ####################################################################
  print('===================================================================')
  print('checking T_B')
  Combined_T_B = np.load('intermediate_HEX/T_B_O_HEX.npy')
  Sliced_T_B   = np.load('intermediate_HEX/T_B_S_HEX.npy')
  check_equal(Sliced_T_B, slice_cut(Combined_T_B))
  ## END ####################################################################
  print('===================================================================')
  print('All passed.')
  return

if __name__=='__main__':
  Func = sys.argv[1]
  if (Func=='all')or(Func=='cal'):
    calculate()
  if (Func=='all')or(Func=='check'):
    check()


