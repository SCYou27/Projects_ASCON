import numpy as np
import serv_manager as svm

# For ASCON AEAD128 encryption.

class TABLE_MLE:
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
  
  def add_new_table(self, T_KEY):
    T_KEY = self.multi_normalize(T_KEY)
    for frag in range(0, self.table_number):
      self.Great_Table[frag][:,1] += T_KEY[frag][:,1]
    return self.multi_normalize(self.Great_Table)


