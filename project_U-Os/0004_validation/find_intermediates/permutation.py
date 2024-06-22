#################################################################################################
#
#
#  ASCON permutation by Shih-Chun You (draft)
#
#  TODO:
#    1. Test: >> python3 permuation.py should print out the initial states on
#             page 11 (2.5.1)
#    2. Check how to use this class in the main function.
#
#################################################################################################

class Permutation:
  def __init__(self, Rounds, Out=False):
    # For intermediate outputs
    self.Out = Out
    #Round Constants
    self.Rounds = Rounds
    if self.Rounds==12:
      self.RC = [0xf0, 0xe1, 0xd2, 0xc3, 0xb4, 0xa5, 0x96, 0x87, 0x78, 0x69, 0x5a, 0x4b]
    elif self.Rounds==8:
      self.RC = [0xb4, 0xa5, 0x96, 0x87, 0x78, 0x69, 0x5a, 0x4b]
    elif self.Rounds==6:
      self.RC = [0x96, 0x87, 0x78, 0x69, 0x5a, 0x4b]
    else:
      print("No such round number.")
      exit()
    #Lane Mask 2^64-1
    self.L_Mask = 2**64-1
    return
  
  def find_hex(self, x0, x1, x2, x3, x4):
    h0 = hex(x0)[2:].zfill(16)
    h1 = hex(x1)[2:].zfill(16)
    h2 = hex(x2)[2:].zfill(16)
    h3 = hex(x3)[2:].zfill(16)
    h4 = hex(x4)[2:].zfill(16)
    Output = h0+h1+h2+h3+h4
    return Output
  
  def P_C(self, x2, r):
    return (x2 ^ self.RC[r])
  
  def P_S(self, x0, x1, x2, x3, x4):
    x0 ^= x4
    x4 ^= x3
    x2 ^= x1
    ## From here is the same with Keccak ####
    t0 = x0^((self.L_Mask^x1)&x2)
    t1 = x1^((self.L_Mask^x2)&x3)
    t2 = x2^((self.L_Mask^x3)&x4)
    t3 = x3^((self.L_Mask^x4)&x0)
    t4 = x4^((self.L_Mask^x0)&x1)
    #########################################
    t1 ^= t0
    t0 ^= t4
    t3 ^= t2
    t2 ^= self.L_Mask
    return t0, t1, t2, t3, t4
  
  def P_L(self, x0, x1, x2, x3, x4):
    L0 = x0^(x0*2**64)
    L1 = x1^(x1*2**64)
    L2 = x2^(x2*2**64)
    L3 = x3^(x3*2**64)
    L4 = x4^(x4*2**64)
    S0 = (x0^(L0>>19)^(L0>>28))&self.L_Mask
    S1 = (x1^(L1>>61)^(L1>>39))&self.L_Mask
    S2 = (x2^(L2>>1)^(L2>>6))&self.L_Mask
    S3 = (x3^(L3>>10)^(L3>>17))&self.L_Mask
    S4 = (x4^(L4>>7)^(L4>>41))&self.L_Mask
    return S0, S1, S2, S3, S4

  def permute(self, Sequence):
    # Sequence here: an unsigned 320-bit integer
    # Big endianess, different from Keccak.  
    x0 = self.L_Mask&(Sequence>>256)
    x1 = self.L_Mask&(Sequence>>192)
    x2 = self.L_Mask&(Sequence>>128)
    x3 = self.L_Mask&(Sequence>>64)
    x4 = self.L_Mask&Sequence
    if self.Out:
      Intermediate_Values = []
      Intermediate_Values.append(self.find_hex(x0, x1, x2, x3, x4))
    for R in range(0, self.Rounds):
      x2 = self.P_C(x2, R)
      x0, x1, x2, x3, x4 = self.P_S(x0, x1, x2, x3, x4)
      if self.Out:
        Intermediate_Values.append(self.find_hex(x0, x1, x2, x3, x4))
      x0, x1, x2, x3, x4 = self.P_L(x0, x1, x2, x3, x4)
      if self.Out:
        Intermediate_Values.append(self.find_hex(x0, x1, x2, x3, x4))
    Output = (x0<<256)^(x1<<192)^(x2<<128)^(x3<<64)^(x4)
    if self.Out:
      return Output, Intermediate_Values
    else:
      return Output

if __name__=='__main__':
  print("================================================")
  print("Test 1: Initial State of ASCON-HASH.")
  S_input1 = 0x00400c0000000100*(2**256)
  Pa_Hash = Permutation(12)
  S_output1 = Pa_Hash.permute(S_input1)
  print("  input sequence:")
  print("  0x"+hex(S_input1)[2:].zfill(80))
  print("  output sequence:")
  print("  0x"+hex(S_output1)[2:].zfill(80))
  print("  answer:")
  print("  0xee9398aadb67f03d8bb21831c60f1002b48a92db98d5da6243189921b8f8e3e8348fa5c9d525e140")
  print("================================================")
  print("Test 2: Initial State of ASCON-XOF.")
  S_input2 = 0x00400c0000000000*(2**256)
  Pa_Hash = Permutation(12)
  S_output2 = Pa_Hash.permute(S_input2)
  print("  input sequence:")
  print("  0x"+hex(S_input2)[2:].zfill(80))
  print("  output sequence:")
  print("  0x"+hex(S_output2)[2:].zfill(80))
  print("  answer:")
  print("  0xb57e273b814cd4162b51042562ae242066a3a7768ddf22185aad0a7a8153650c4f3e0e32539493b6")
