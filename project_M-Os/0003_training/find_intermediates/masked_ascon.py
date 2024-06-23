import numpy as np

RC = [0xf0, 0xe1, 0xd2, 0xc3, 0xb4, 0xa5, 0x96, 0x87, 0x78, 0x69, 0x5a, 0x4b]

RC_sliced = np.array([12, 12, 9, 12, 12, 9, 9, 9, 6, 12, 3, 12, 6, 9, 3, 9, 12, 6, 9, 6, 12, 3, 9, 3], dtype=np.uint32)


L_Mask = 2**64-1
half_mask = 2**32-1

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}

def find_hex(x0, x1, x2, x3, x4):
  h0 = hex(x0)[2:].zfill(16)
  h1 = hex(x1)[2:].zfill(16)
  h2 = hex(x2)[2:].zfill(16)
  h3 = hex(x3)[2:].zfill(16)
  h4 = hex(x4)[2:].zfill(16)
  Output = h0+h1+h2+h3+h4
  return Output

def hex2int(hex_str):
  num = 0
  for t in range(0, len(hex_str)):
    num *= 16
    num += hexdict[hex_str[t]]
  return num

def Slice(num_H, num_L):
  bin64 = bin((num_H&half_mask))[2:].zfill(32)+bin((num_L&half_mask))[2:].zfill(32)
  num_e = 0
  num_o = 0
  for t in range(0, 32):
    num_o *= 2
    num_e *= 2
    num_o += int(bin64[(2*t)])
    num_e += int(bin64[(2*t+1)])
  return (num_e&half_mask), (num_o&half_mask)

def Combine(num_e, num_o):
  num_e &= half_mask
  num_o &= half_mask
  bin_e = bin(num_e)[2:].zfill(32)
  bin_o = bin(num_o)[2:].zfill(32)
  num_H = 0
  num_L = 0
  for t in range(0, 16):
    num_H *= 4
    num_H += (2*int(bin_o[t])+int(bin_e[t]))
  for t in range(16, 32):
    num_L *= 4
    num_L += (2*int(bin_o[t])+int(bin_e[t]))
  return (num_H&half_mask), (num_L&half_mask)

def and_not_xor_sliced(a0, a1, a2, b0, b1, b2):
  new_a0 = a0 ^ ((half_mask^a1)&b2) ^ ((half_mask^a1)&a2)
  new_b0 = b0 ^ (b1&b2) ^ (b1&a2)
  return new_a0, new_b0

def RightRotate(b, word32):
  bin32 = bin(word32&half_mask)[2:].zfill(32)
  new32 = bin32[(32-b):32]+bin32[0:(32-b)]
  num = 0
  for t in range(0, 32):
    num *= 2
    num += int(new32[t])
  return (num&half_mask)

def ascon_linear_sliced_share(SE, SO):
  # x0 ^= rightRotate19_64(x0) ^ rightRotate28_64(x0)
  tE = SE[0] ^ RightRotate(4, SO[0])
  tO = SO[0] ^ RightRotate(5, SE[0])
  SE[0] ^= RightRotate(9,  tO)
  SO[0] ^= RightRotate(10, tE)
  # x1 ^= RightRotate61_64(x1) ^ RightRotate39_64(x1)
  tE = SE[1] ^ RightRotate(11, SE[1])
  tO = SO[1] ^ RightRotate(11, SO[1])
  SE[1] ^= RightRotate(19, tO)
  SO[1] ^= RightRotate(20, tE)
  # x2 ^= RightRotate1_64(x2)  ^ RightRotate6_64(x2)
  tE = SE[2] ^ RightRotate(2, SO[2])
  tO = SO[2] ^ RightRotate(3, SE[2])
  SE[2] ^= tO
  SO[2] ^= RightRotate(1, tE)
  # x3 ^= RightRotate(10_64(x3) ^ RightRotate(17_64(x3)
  tE = SE[3] ^ RightRotate(3, SO[3])
  tO = SO[3] ^ RightRotate(4, SE[3])
  SE[3] ^= RightRotate(5, tE)
  SO[3] ^= RightRotate(5, tO)
  # x4 ^= RightRotate(7_64(x4)  ^ RightRotate(41_64(x4)
  tE = SE[4] ^ RightRotate(17, SE[4])
  tO = SO[4] ^ RightRotate(17, SO[4])
  SE[4] ^= RightRotate(3, tO)
  SO[4] ^= RightRotate(4, tE)
  return SE, SO

def ascon_permute_masked_x2(SAE, SAO, SBE, SBO, MASK_H, MASK_L):
  T0 = np.array([MASK_H, MASK_L], dtype=np.uint32)
  TAE = np.array(SAE, dtype=np.uint32)
  TAO = np.array(SAO, dtype=np.uint32)
  TBE = np.array(SBE, dtype=np.uint32)
  TBO = np.array(SBO, dtype=np.uint32)
  a_t0_e = T0[0]
  a_t0_o = T0[1]
  # Load the state into local variables
  for r in range(0, 12):
    a_x0_e = TAE[0]
    a_x0_o = TAO[0]
    a_x1_e = TAE[1]
    a_x1_o = TAO[1]
    a_x2_e = TAE[2]
    a_x2_o = TAO[2]
    a_x3_e = TAE[3]
    a_x3_o = TAO[3]
    a_x4_e = TAE[4]
    a_x4_o = TAO[4]
    b_x0_e = TBE[0]
    b_x0_o = TBO[0]
    b_x1_e = TBE[1]
    b_x1_o = TBO[1]
    b_x2_e = TBE[2]
    b_x2_o = TBO[2]
    b_x3_e = TBE[3]
    b_x3_o = TBO[3]
    b_x4_e = TBE[4]
    b_x4_o = TBO[4]
    #=================================================================#
    a_x2_e ^= RC_sliced[(2*r)]
    #Substitution layer (even half)
    a_x0_e ^= a_x4_e
    b_x0_e ^= b_x4_e
    a_x4_e ^= a_x3_e
    b_x4_e ^= b_x3_e
    a_x2_e ^= a_x1_e
    b_x2_e ^= b_x1_e
    a_t1_e = a_x0_e
    b_t1_e = b_x0_e
    b_t0_e = a_t0_e
    a_t0_e, b_t0_e = and_not_xor_sliced(a_t0_e, a_x0_e, a_x1_e, b_t0_e, b_x0_e, b_x1_e) # t0 ^= (~x0) & x1
    a_x0_e, b_x0_e = and_not_xor_sliced(a_x0_e, a_x1_e, a_x2_e, b_x0_e, b_x1_e, b_x2_e) # x0 ^= (~x1) & x2
    a_x1_e, b_x1_e = and_not_xor_sliced(a_x1_e, a_x2_e, a_x3_e, b_x1_e, b_x2_e, b_x3_e) # x1 ^= (~x2) & x3
    a_x2_e, b_x2_e = and_not_xor_sliced(a_x2_e, a_x3_e, a_x4_e, b_x2_e, b_x3_e, b_x4_e) # x2 ^= (~x3) & x4
    a_x3_e, b_x3_e = and_not_xor_sliced(a_x3_e, a_x4_e, a_t1_e, b_x3_e, b_x4_e, b_t1_e) # x3 ^= (~x4) & t1
    a_x4_e ^= a_t0_e
    b_x4_e ^= b_t0_e
    a_x1_e ^= a_x0_e
    b_x1_e ^= b_x0_e
    a_x0_e ^= a_x4_e
    b_x0_e ^= b_x4_e
    a_x3_e ^= a_x2_e
    b_x3_e ^= b_x2_e
    a_x2_e = (half_mask^a_x2_e)&half_mask
    #=============================================================================================================#
    a_x2_o ^= RC_sliced[(2*r+1)]
    #Substitution layer (old half)
    a_x0_o ^= a_x4_o
    b_x0_o ^= b_x4_o
    a_x4_o ^= a_x3_o
    b_x4_o ^= b_x3_o
    a_x2_o ^= a_x1_o
    b_x2_o ^= b_x1_o
    a_t1_o = a_x0_o
    b_t1_o = b_x0_o
    b_t0_o = a_t0_o
    a_t0_o, b_t0_o = and_not_xor_sliced(a_t0_o, a_x0_o, a_x1_o, b_t0_o, b_x0_o, b_x1_o) # t0 ^= (~x0) & x1
    a_x0_o, b_x0_o = and_not_xor_sliced(a_x0_o, a_x1_o, a_x2_o, b_x0_o, b_x1_o, b_x2_o) # x0 ^= (~x1) & x2
    a_x1_o, b_x1_o = and_not_xor_sliced(a_x1_o, a_x2_o, a_x3_o, b_x1_o, b_x2_o, b_x3_o) # x1 ^= (~x2) & x3
    a_x2_o, b_x2_o = and_not_xor_sliced(a_x2_o, a_x3_o, a_x4_o, b_x2_o, b_x3_o, b_x4_o) # x2 ^= (~x3) & x4
    a_x3_o, b_x3_o = and_not_xor_sliced(a_x3_o, a_x4_o, a_t1_o, b_x3_o, b_x4_o, b_t1_o) # x3 ^= (~x4) & t1
    a_x4_o ^= a_t0_o
    b_x4_o ^= b_t0_o
    a_x1_o ^= a_x0_o
    b_x1_o ^= b_x0_o
    a_x0_o ^= a_x4_o
    b_x0_o ^= b_x4_o
    a_x3_o ^= a_x2_o
    b_x3_o ^= b_x2_o
    a_x2_o = (half_mask^a_x2_o)&half_mask
    TAE = np.array([a_x0_e, a_x1_e, a_x2_e, a_x3_e, a_x4_e], dtype=np.uint32)
    TAO = np.array([a_x0_o, a_x1_o, a_x2_o, a_x3_o, a_x4_o], dtype=np.uint32)
    TBE = np.array([b_x0_e, b_x1_e, b_x2_e, b_x3_e, b_x4_e], dtype=np.uint32)
    TBO = np.array([b_x0_o, b_x1_o, b_x2_o, b_x3_o, b_x4_o], dtype=np.uint32)
    TAE, TAO = ascon_linear_sliced_share(TAE, TAO)
    TBE, TBO = ascon_linear_sliced_share(TBE, TBO)
  return TAE, TAO, TBE, TBO

def reverse_32(num32):
  num32 &= half_mask
  hex32 = hex(num32)[2:].zfill(8)
  new32 = hex32[6:8]+hex32[4:6]+hex32[2:4]+hex32[0:2]
  return hex2int(new32)&half_mask

def ASCON128_masked_Enc(KEY, NONCE, PLAINTEXT, MASKS, find_value=False):
  #Initialize the ASCON state in masked form
  # 64-bit arrays.
  IV0 = 0x80400c06
  IV1 = 0x00000000
  #ascon_mask_key_128_x2(&key, ASCON128_IV, k) # 6 32-bit words
  KAE = np.zeros((3), dtype=np.uint32)
  KAO = np.zeros((3), dtype=np.uint32)
  KBE = np.zeros((3), dtype=np.uint32)
  KBO = np.zeros((3), dtype=np.uint32)
  KAE[0], KAO[0] = Slice(IV0^MASKS[0], IV1^MASKS[1])
  KAE[1], KAO[1] = Slice(KEY[0]^MASKS[2], KEY[1]^MASKS[3])
  KAE[2], KAO[2] = Slice(KEY[2]^MASKS[4], KEY[3]^MASKS[5])
  KBE[0], KBO[0] = Slice(MASKS[0], MASKS[1])
  KBE[1], KBO[1] = Slice(MASKS[2], MASKS[3])
  KBE[2], KBO[2] = Slice(MASKS[4], MASKS[5])
  #================================================================#
  if find_value:
    sliced_K_A = hex(KAE[1])[2:].zfill(8)+hex(KAO[1])[2:].zfill(8)+hex(KAE[2])[2:].zfill(8)+hex(KAO[2])[2:].zfill(8)
    sliced_K_B = hex(KBE[1])[2:].zfill(8)+hex(KBO[1])[2:].zfill(8)+hex(KBE[2])[2:].zfill(8)+hex(KBO[2])[2:].zfill(8)
  #================================================================#
  #ascon_masked_init_key_x2(&state, &key, npub, 0) # (10+2) 32-bit words
  SAE = np.zeros((5), dtype=np.uint32)
  SAO = np.zeros((5), dtype=np.uint32)
  SBE = np.zeros((5), dtype=np.uint32)
  SBO = np.zeros((5), dtype=np.uint32)
  for t in range(0, 3):
    SAE[t] = np.bitwise_xor(KAE[t], MASKS[2*t+6])
    SAO[t] = np.bitwise_xor(KAO[t], MASKS[2*t+7])
    SBE[t] = np.bitwise_xor(KBE[t], MASKS[2*t+6])
    SBO[t] = np.bitwise_xor(KBO[t], MASKS[2*t+7])
  SAE[3], SAO[3] = Slice(NONCE[0]^MASKS[12], NONCE[1]^MASKS[13])
  SAE[4], SAO[4] = Slice(NONCE[2]^MASKS[14], NONCE[3]^MASKS[15])
  SBE[3], SBO[3] = Slice(MASKS[12], MASKS[13])
  SBE[4], SBO[4] = Slice(MASKS[14], MASKS[15])
  SAE, SAO, SBE, SBO = ascon_permute_masked_x2(SAE, SAO, SBE, SBO, MASKS[16], MASKS[17])
  SAE[3] ^= KAE[1]
  SAO[3] ^= KAO[1]
  SAE[4] ^= KAE[2]
  SAO[4] ^= KAO[2]
  SBE[3] ^= KBE[1]
  SBO[3] ^= KBO[1]
  SBE[4] ^= KBE[2]
  SBO[4] ^= KBO[2]
  #================================================================#
  #ascon_masked_separator_x2(&state)
  SAE[4] ^= 0x01
  #================================================================#
  #ascon_masked_encrypt_8_x2(&state, c, m, mlen, 6) # 2 32-bit words
  mask_rev_0 = reverse_32(MASKS[18])
  mask_rev_1 = reverse_32(MASKS[19])
  TAE, TAO = Slice(PLAINTEXT[0]^mask_rev_0, PLAINTEXT[1]^mask_rev_1)
  TBE, TBO = Slice(mask_rev_0, mask_rev_1)
  SAE[0] ^= TAE
  SAO[0] ^= TAO
  SBE[0] ^= TBE
  SBO[0] ^= TBO
  CSE = SAE[0]^SBE[0]
  CSO = SAO[0]^SBO[0]
  CIPHER = np.array(Combine(CSE, CSO), dtype=np.uint32)
  #================================================================#
  #ascon_masked_finalize_128_x2(&state, &key, c + mlen) # (10+2) 32-bit words
  for t in range(0, 5):
    SAE[t] = np.bitwise_xor(SAE[t], MASKS[2*t+20])
    SAO[t] = np.bitwise_xor(SAO[t], MASKS[2*t+21])
    SBE[t] = np.bitwise_xor(SBE[t], MASKS[2*t+20])
    SBO[t] = np.bitwise_xor(SBO[t], MASKS[2*t+21])
  SAE[1] ^= KAE[1]
  SAO[1] ^= KAO[1]
  SAE[2] ^= KAE[2]
  SAO[2] ^= KAO[2]
  SBE[1] ^= KBE[1]
  SBO[1] ^= KBO[1]
  SBE[2] ^= KBE[2]
  SBO[2] ^= KBO[2]
  SAE, SAO, SBE, SBO = ascon_permute_masked_x2(SAE, SAO, SBE, SBO, MASKS[30], MASKS[31])
  #================================================================#
  if find_value:
    sliced_L_A = hex(SAE[3])[2:].zfill(8)+hex(SAO[3])[2:].zfill(8)+hex(SAE[4])[2:].zfill(8)+hex(SAO[4])[2:].zfill(8)
    sliced_L_B = hex(SBE[3])[2:].zfill(8)+hex(SBO[3])[2:].zfill(8)+hex(SBE[4])[2:].zfill(8)+hex(SBO[4])[2:].zfill(8)
  #================================================================#
  SAE[3] ^= KAE[1]
  SAO[3] ^= KAO[1]
  SAE[4] ^= KAE[2]
  SAO[4] ^= KAO[2]
  SBE[3] ^= KBE[1]
  SBO[3] ^= KBO[1]
  SBE[4] ^= KBE[2]
  SBO[4] ^= KBO[2]
  #================================================================#
  if find_value:
    sliced_T_A = hex(SAE[3])[2:].zfill(8)+hex(SAO[3])[2:].zfill(8)+hex(SAE[4])[2:].zfill(8)+hex(SAO[4])[2:].zfill(8)
    sliced_T_B = hex(SBE[3])[2:].zfill(8)+hex(SBO[3])[2:].zfill(8)+hex(SBE[4])[2:].zfill(8)+hex(SBO[4])[2:].zfill(8)
  #================================================================#
  T0E = SAE[3]^SBE[3]
  T0O = SAO[3]^SBO[3]
  T1E = SAE[4]^SBE[4]
  T1O = SAO[4]^SBO[4]
  TAG = np.array(np.hstack([Combine(T0E, T0O), Combine(T1E, T1O)]), dtype=np.uint32)
  if find_value:
    return CIPHER, TAG, sliced_K_A, sliced_K_B, sliced_L_A, sliced_L_B, sliced_T_A, sliced_T_B
  return CIPHER, TAG


def My_Enc(key, nonce, plaintext, masks, find_value=False):
  KEY = np.array([hex2int(key[0:8]), hex2int(key[8:16]), hex2int(key[16:24]), hex2int(key[24:32])], dtype=np.uint32)
  NONCE = np.array([hex2int(nonce[0:8]), hex2int(nonce[8:16]), hex2int(nonce[16:24]), hex2int(nonce[24:32])], dtype=np.uint32)
  PLAINTEXT = np.array([hex2int(plaintext[0:8]), hex2int((plaintext[8:14]+'80'))], dtype=np.uint32)
  MASKS = np.zeros((32), dtype=np.uint32)
  for t in range(0, 32):
    MASKS[t] = hex2int(masks[(8*t):(8*t+8)])
  if find_value:
    CIPHER, TAG, sliced_K_A, sliced_K_B, sliced_L_A, sliced_L_B, sliced_T_A, sliced_T_B = ASCON128_masked_Enc(KEY, NONCE, PLAINTEXT, MASKS, True)
  else:
    CIPHER, TAG = ASCON128_masked_Enc(KEY, NONCE, PLAINTEXT, MASKS, False)
  cipher = hex(CIPHER[0])[2:].zfill(8)+(hex(CIPHER[1])[2:].zfill(8))[0:6]
  tag = hex(TAG[0])[2:].zfill(8)+hex(TAG[1])[2:].zfill(8)+hex(TAG[2])[2:].zfill(8)+hex(TAG[3])[2:].zfill(8)
  if find_value:
    return cipher, tag, sliced_K_A, sliced_K_B, sliced_L_A, sliced_L_B, sliced_T_A, sliced_T_B
  return cipher, tag

if __name__=='__main__':
  import ascon_aead
  ENC_128 = ascon_aead.ASCON_AEAD().ASCON_128.Enc
  print("=====================================================")
  print("Count = 232:")
  Key   = "000102030405060708090a0b0c0d0e0f"
  Nonce = "000102030405060708090a0b0c0d0e0f"
  Plaintext  = "00010203040506"
  A_DATA     = ""
  Cipher_Tag = ("BC820DBDF7A463CE9985966C40BC56A9C5180E23F7086C").lower()
  print("++ Enc:")
  C1, T1 = My_Enc(Key, Nonce, Plaintext, ('0'*256))
  C2, T2 = My_Enc(Key, Nonce, Plaintext, ('5'*256))
  CT1 = C1+T1
  CT2 = C2+T2
  Results = ENC_128(Key, Nonce, A_DATA, Plaintext)
  print("++++ CT1 checking:")
  print(CT1 == Cipher_Tag)
  print(CT1)
  print(Cipher_Tag)
  print("++++ CT1 checking:")
  print(CT2 == Cipher_Tag)
  print(CT2)
  print(Cipher_Tag)
  print("=====================================================")
  print("++++ CT1==CT2?", CT1==CT2)
  print("++++ Results==Cipher_Tag?", Results==Cipher_Tag)
  print(Results)
  print(Cipher_Tag)



