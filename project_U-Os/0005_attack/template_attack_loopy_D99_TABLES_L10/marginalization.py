import numpy as np
class Marginalization:
  def __init__(self, bit_size, ver = False):
    tmp = np.arange((2**bit_size))
    self.Bits_O = np.zeros((0, 2**bit_size))
    for t in range(0, bit_size):
      mask = 2**t
      self.Bits_O = np.vstack([(mask&tmp)//mask , self.Bits_O])
    self.Bits_O = np.matrix(self.Bits_O)
    self.Bits_Z = np.matrix(np.ones((bit_size, 2**bit_size)))-self.Bits_O
    if ver:
      print(self.Bits_O)
      print(self.Bits_Z)
    return
  
  def marginalize(self, Prob_Table):
    BitTable = np.zeros((0, 2))
    for frag in range(0, len(Prob_Table)):
      Prob = np.matrix(Prob_Table[frag])[:,1]
      Prob_marginal = np.hstack([(self.Bits_Z*Prob), (self.Bits_O*Prob)])
      BitTable = np.vstack([BitTable, Prob_marginal])
    return np.transpose(np.array(BitTable))

def slice_recover(Bit_Tables):
  (D1, D2) = np.shape(Bit_Tables)
  Out_Tables = np.zeros((2, 0))
  for lane in range(0, (D2//64)):
    Table_E = Bit_Tables[:,(64*lane   ):(64*lane+32)]
    Table_O = Bit_Tables[:,(64*lane+32):(64*lane+64)]
    Lane_Table = np.zeros((2, 64))
    for it in range(0, 32):
      Lane_Table[:,(2*it  )] = Table_O[:,it]
      Lane_Table[:,(2*it+1)] = Table_E[:,it]
    Out_Tables = np.hstack([Out_Tables, Lane_Table])
  return Out_Tables

if __name__=='__main__':
  Marginalization(4, True)
