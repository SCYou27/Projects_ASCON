import numpy as np
import serv_manager as svm

# For ASCON AEAD128 encryption.

class TREE_BP:
  def __init__(self, Size=8):
    self.table_length = 2**Size
    self.table_number = 128//Size
    self.Great_Table = []
    for p in range(0, self.table_number):
      self.Great_Table.append(np.transpose(np.vstack([np.arange(0, self.table_length), np.zeros((self.table_length))])))
    self.Great_Table = np.array(self.Great_Table)
    return
  
  def log_normalize(self, Table):
    Prob_Max = np.max(Table[:,1])
    Table[:,1] = Table[:,1]-Prob_Max
    return Table, Prob_Max
  
  def multi_normalize(self, GT):
    for t in range(len(GT)):
      GT[t], _ = self.log_normalize(GT[t])
    return GT
  
  def propagate_add(self, T_KEY, T_F_B11, Tag_Bytes):
    T_KEY = self.multi_normalize(T_KEY)
    T_F_B11 = self.multi_normalize(T_F_B11)
    for frag in range(0, self.table_number):
      tag_byte = Tag_Bytes[frag]
      T = np.array(T_F_B11[frag])
      T[:,0] = (T[:,0].astype('int32')^tag_byte)
      T = T[T[:,0].argsort()]
      self.Great_Table[frag][:,1] += (T_KEY[frag][:,1] + T[:,1])
    return self.multi_normalize(self.Great_Table)


