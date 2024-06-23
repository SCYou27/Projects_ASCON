import numpy as np

hex2int = {'0': 0, '1': 1, '2': 2, '3': 3,\
           '4': 4, '5': 5, '6': 6, '7': 7,\
           '8': 8, '9': 9, 'a':10, 'b':11,\
           'c':12, 'd':13, 'e':14, 'f':15}

def WordLeftRotate(Uint32, Digit):
  B = Uint32<<Digit
  C = B&(2**32-1)|B>>32
  return C&(2**32-1)

def QuarterRound(a, b, c, d):
  a = (a+b)&(2**32-1)
  d = (d^a)&(2**32-1)
  d = WordLeftRotate(d, 16)
  ####
  c = (c+d)&(2**32-1)
  b = (b^c)&(2**32-1)
  b = WordLeftRotate(b, 12)
  ####
  a = (a+b)&(2**32-1)
  d = (d^a)&(2**32-1)
  d = WordLeftRotate(d, 8)
  ####
  c = (c+d)&(2**32-1)
  b = (b^c)&(2**32-1)
  b = WordLeftRotate(b, 7)
  ####
  return a, b, c, d

def hex2arr(Hex_str):
  Arr = np.zeros((16), dtype='uint32')
  for t in range(0, 16):
    fragment = Hex_str[(t*8):(t*8+8)]
    Num = 0
    for b in range(0, 8):
      Num <<= 4
      Num += hex2int[fragment[b]]
    Arr[t] = Num&(2**32-1)
  return Arr

def arr2hex(Arr):
  Hex_str = ''
  for t in range(0, 16):
    Hex_str += (hex(Arr[t])[2:].zfill(8))
  return Hex_str.lower()

def ChaCha20(hex_str):
  if len(hex_str)!=96:
    print('Error: input size does not match')
    exit()
  Constant = '617078653320646e79622d326b206574'
  Arr = hex2arr((Constant+hex_str).lower())
  Original = hex2arr((Constant+hex_str).lower())
  for X in range(0, 10):
    # Column round
    Arr[0], Arr[4], Arr[8],  Arr[12] = QuarterRound(Arr[0], Arr[4], Arr[8],  Arr[12])
    Arr[1], Arr[5], Arr[9],  Arr[13] = QuarterRound(Arr[1], Arr[5], Arr[9],  Arr[13])
    Arr[2], Arr[6], Arr[10], Arr[14] = QuarterRound(Arr[2], Arr[6], Arr[10], Arr[14])
    Arr[3], Arr[7], Arr[11], Arr[15] = QuarterRound(Arr[3], Arr[7], Arr[11], Arr[15])
    #Diagonal round
    Arr[0], Arr[5], Arr[10], Arr[15] = QuarterRound(Arr[0], Arr[5], Arr[10], Arr[15])
    Arr[1], Arr[6], Arr[11], Arr[12] = QuarterRound(Arr[1], Arr[6], Arr[11], Arr[12])
    Arr[2], Arr[7], Arr[8],  Arr[13] = QuarterRound(Arr[2], Arr[7], Arr[8],  Arr[13])
    Arr[3], Arr[4], Arr[9],  Arr[14] = QuarterRound(Arr[3], Arr[4], Arr[9],  Arr[14])
  for w in range(0, 16):
    Arr[w] = (Arr[w]+Original[w])&(2**32-1)
  return arr2hex(Arr)


if __name__=='__main__':
  Str = ''
  Str += '00000000'
  Str += '11111111'
  Str += '22222222'
  Str += '33333333'
  Str += '44444444'
  Str += '55555555'
  Str += '66666666'
  Str += '77777777'
  Str += '88888888'
  Str += '99999999'
  Str += 'aaaaaaaa'
  Str += 'bbbbbbbb'
  print(ChaCha20(Str))


