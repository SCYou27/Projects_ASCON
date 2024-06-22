import numpy as np
class BitGen:
  def __init__(self, Size):
    _A = np.transpose(np.matrix(np.arange(0, 2**Size)))\
        *np.ones((1, Size), dtype=np.int32)
    _B = np.ones((2**Size, 1), dtype=np.int32)\
        *np.matrix(2**((Size-1)-np.arange(0, Size)))
    self.Bits = ((_A&_B)/_B)*1.0
    return

if __name__=='__main__':
  TEMP = BitGen(4)
  print(TEMP.Bits)

