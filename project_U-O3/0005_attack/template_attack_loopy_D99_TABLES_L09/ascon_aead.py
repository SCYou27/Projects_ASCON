import permutation as ASCON_PER

hexdict = {'0':  0, '1':  1, '2':  2, '3':  3, \
           '4':  4, '5':  5, '6':  6, '7':  7, \
           '8':  8, '9':  9, 'a': 10, 'b': 11, \
           'c': 12, 'd': 13, 'e': 14, 'f': 15}

class AEAD_Base:
  def __init__(self, tag):
    self.tag = tag
    self.P_A = ASCON_PER.Permutation(12).permute
    if tag=='128':
      self.P_B = ASCON_PER.Permutation(6).permute
      self.rate = 64
      self.rate_byte = 8
      self.IV = 0x80400c0600000000
    elif tag=='128a':
      self.P_B = ASCON_PER.Permutation(8).permute
      self.rate = 128
      self.rate_byte = 16
      self.IV = 0x80800c0800000000
    self.cap = 320-self.rate
    self.cap_byte = 40-self.rate_byte
    self.State_Mask = 2**320-1
    self.Rate_Mask = (2**self.rate-1)<<self.cap
    self.Cap_Mask = 2**self.cap-1
    return
  
  def Str2BigNum(self, String):
    BigNumber = 0
    for t in range(0, len(String)):
      BigNumber <<= 4
      BigNumber += hexdict[(String[t])]
    return BigNumber
  
  def Padding(self, Raw):
    # Data length will not be 0.
    # Data are strings, R_Len in bytes.
    Data = Raw
    Data += '80'
    while (len(Data)%(2*self.rate_byte))!=0:
      Data += '00'
    Len_Arr = len(Data)//(2*self.rate_byte)
    Data_Array = []
    for t in range(0, Len_Arr):
      Lower = t*2*self.rate_byte
      Upper = Lower+2*self.rate_byte
      Data_String = Data[Lower:Upper]
      Data_Int = self.Str2BigNum(Data_String) << self.cap
      Data_Array.append(Data_Int)
    return Data_Array
  
  def CTProc(self, CT_str):
    C_str = CT_str[:-32]
    T_str = CT_str[-32:]
    C_arr = self.Padding(C_str)
    return C_arr, T_str    


  def Enc(self, K_str, N_str, A_str, P_str):
    if (len(K_str)!=32)or(len(N_str)!=32):
      raise ValueError("Wrong key or nonce size.")
      exit()
    P_len = len(P_str)
    # Initialization:
    K_int = self.Str2BigNum(K_str)
    N_int = self.Str2BigNum(N_str)
    State = ((self.IV<<256)^(K_int<<128)^N_int)&self.State_Mask
    State = self.P_A(State)
    State = (State^K_int)&self.State_Mask
    # Associated Data:
    if len(A_str)!=0:
      A_arr = self.Padding(A_str)
      for invoc in range(0, len(A_arr)):
        State ^= A_arr[invoc]
        State = self.P_B(State)
    State = (State^0x01)&self.State_Mask
    # Plaintext:
    P_arr = self.Padding(P_str)
    C_str = ""
    for invoc in range(0, len(P_arr)):
      State ^= P_arr[invoc]
      C_int = State>>self.cap
      C_str += hex(C_int)[2:].zfill(2*self.rate_byte)
      if invoc==len(P_arr)-1:
        break
      State = self.P_B(State)
    C_str = C_str[:P_len]
    # Finalization:
    State = (State^(K_int<<(self.cap-128))&self.State_Mask)
    State = self.P_A(State)
    T_int = (State^K_int)&(2**128-1)
    T_str = hex(T_int)[2:].strip('L').zfill(32)
    CT_str = C_str+T_str
    return CT_str
  
  def Dec(self, K_str, N_str, A_str, CT_str):
    if (len(K_str)!=32)or(len(N_str)!=32):
      raise ValueError("Wrong key or nonce size.")
      exit()
    P_len = len(CT_str)-32
    # Initialization:
    K_int = self.Str2BigNum(K_str)
    N_int = self.Str2BigNum(N_str)
    State = ((self.IV<<256)^(K_int<<128)^N_int)&self.State_Mask
    State = self.P_A(State)
    State = (State^K_int)&self.State_Mask
    # Associated Data:
    if len(A_str)!=0:
      A_arr = self.Padding(A_str)
      for invoc in range(0, len(A_arr)):
        State ^= A_arr[invoc]
        State = self.P_B(State)
    State = (State^0x01)&self.State_Mask
    # Ciphertext:
    P_str = ""
    C_arr, T_ans = self.CTProc(CT_str)
    for invoc in range(0, len(C_arr)):
      P_int = (State^C_arr[invoc])>>self.cap
      P_str += hex(P_int)[2:].zfill(2*self.rate_byte)
      if invoc==len(C_arr)-1:
        Tail_Len = (P_len%(2*self.rate_byte))*4
        P_int = P_int>>(self.rate-Tail_Len)
        P_int = P_int<<(320-Tail_Len)
        Pad = 1<<(320-1-Tail_Len)
        State = State^P_int^Pad
        break
      State = (C_arr[invoc]&self.Rate_Mask)^(State&self.Cap_Mask)
      State = self.P_B(State)
    P_str = P_str[:P_len]
    # Finalization:
    State = (State^(K_int<<(self.cap-128))&self.State_Mask)
    State = self.P_A(State)
    T_int = (State^K_int)&(2**128-1)
    T_str = hex(T_int)[2:].strip('L').zfill(32)
    if T_str!=T_ans:
      raise ValueError("Tags do not match.\n\tTag:"+T_str+"\n\tAns:"+T_ans)
      exit()
    return P_str, T_str

class ASCON_AEAD:
  def __init__(self):
    self.ASCON_128 = AEAD_Base('128')
    self.ASCON_128a = AEAD_Base('128a')
    return

if __name__=='__main__':
  template = ASCON_AEAD()
  ENC_128 = template.ASCON_128.Enc
  DEC_128 = template.ASCON_128.Dec
  ENC_128a = template.ASCON_128a.Enc
  DEC_128a = template.ASCON_128a.Dec
  print("=====================================================")
  print("ASCON-128")
  print("=====================================================")
  print("Count = 104:")
  Key   = "000102030405060708090a0b0c0d0e0f"
  Nonce = "000102030405060708090a0b0c0d0e0f"
  Plaintext  = "000102"
  A_DATA     = "00010203"
  Cipher_Tag = "7763f8a2bbfbb05b3b4f54da1576a863b47409"
  print("++ Enc:")
  Results = ENC_128(Key, Nonce, A_DATA, Plaintext)
  print(Cipher_Tag == Results)
  print(Cipher_Tag)
  print(Results)
  print("++ Dec:")
  Results, Tag = DEC_128(Key, Nonce, A_DATA, Cipher_Tag)
  print(Plaintext == Results)
  print(Plaintext)
  print(Results)
  print(Tag == Cipher_Tag[-32:])
  print(Cipher_Tag[-32:])
  print(Tag)
  print("=====================================================")
  print("Count = 11:")
  Key   = "000102030405060708090a0b0c0d0e0f"
  Nonce = "000102030405060708090a0b0c0d0e0f"
  Plaintext  = ""
  A_DATA     = "00010203040506070809"
  Cipher_Tag = "4b006a400b6dfb9777bc3446c2b7dc26"
  print("++ Enc:")
  Results = ENC_128(Key, Nonce, A_DATA, Plaintext)
  print(Cipher_Tag == Results)
  print(Cipher_Tag)
  print(Results)
  print("++ Dec:")
  Results, Tag = DEC_128(Key, Nonce, A_DATA, Cipher_Tag)
  print(Plaintext == Results)
  print(Plaintext)
  print(Results)
  print(Tag == Cipher_Tag[-32:])
  print(Cipher_Tag[-32:])
  print(Tag)
  print("=====================================================")
  print("Count = OFFICIAL:")
  Key   = "2a2ba8a32c17437b0a3477cbcf1cf60a"
  Nonce = "2041accb309ab7e26ebe82975228a258"
  Plaintext  = "6173636f6e"
  A_DATA     = "4153434f4e"
  Cipher_Tag = "e03aacce5eada17f1820b23b58c4e17c5453834dc3"
  print("++ Enc:")
  Results = ENC_128(Key, Nonce, A_DATA, Plaintext)
  print(Cipher_Tag == Results)
  print(Cipher_Tag)
  print(Results)
  print("++ Dec:")
  Results, Tag = DEC_128(Key, Nonce, A_DATA, Cipher_Tag)
  print(Plaintext == Results)
  print(Plaintext)
  print(Results)
  print(Tag == Cipher_Tag[-32:])
  print(Cipher_Tag[-32:])
  print(Tag)
  print("=====================================================")
  print("ASCON-128a")
  print("=====================================================")
  print("Count = 556:")
  Key   = "000102030405060708090a0b0c0d0e0f"
  Nonce = "000102030405060708090a0b0c0d0e0f"
  Plaintext  = "000102030405060708090a0b0c0d0e0f"
  A_DATA     = "000102030405060708090a0b0c0d0e0f101112131415161718191a"
  Cipher_Tag = "345300842a2ab4254006aa0f0a5084ca7c484611ff73d6072bd1caf2ff10c0f2"
  print("++ Enc:")
  Results = ENC_128a(Key, Nonce, A_DATA, Plaintext)
  print(Cipher_Tag == Results)
  print(Cipher_Tag)
  print(Results)
  print("++ Dec:")
  Results, Tag = DEC_128a(Key, Nonce, A_DATA, Cipher_Tag)
  print(Plaintext == Results)
  print(Plaintext)
  print(Results)
  print(Tag == Cipher_Tag[-32:])
  print(Cipher_Tag[-32:])
  print(Tag)
  print("=====================================================")
  print("Count = 417:")
  Key   = "000102030405060708090a0b0c0d0e0f"
  Nonce = "000102030405060708090a0b0c0d0e0f"
  Plaintext  = "000102030405060708090a0b"
  A_DATA     = "000102030405060708090a0b0c0d0e0f10111213"
  Cipher_Tag = "21d5926ca563c1f02c412fa09e20f050c02f79f6a4205cf98ed9034f"
  print("++ Enc:")
  Results = ENC_128a(Key, Nonce, A_DATA, Plaintext)
  print(Cipher_Tag == Results)
  print(Cipher_Tag)
  print(Results)
  print("++ Dec:")
  Results, Tag = DEC_128a(Key, Nonce, A_DATA, Cipher_Tag)
  print(Plaintext == Results)
  print(Plaintext)
  print(Results)
  print(Tag == Cipher_Tag[-32:])
  print(Cipher_Tag[-32:])
  print(Tag)
  print("=====================================================")

