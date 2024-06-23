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

  def convolution(self, Table_A, Table_B):
    Table_Out = []
    for key in range(0, self.table_length):
      temp = []
      temp.append(key)
      T = np.array(Table_B)
      T[:,0] = T[:,0].astype('int32')^key
      T = T[T[:,0].argsort()]
      Prob_Array = Table_A[:,1]+T[:,1]
      prob_max = np.max(Prob_Array)
      prob_log = prob_max + np.log(np.sum(np.exp((Prob_Array-prob_max))))
      temp.append(prob_log)
      Table_Out.append(temp)
    Table_Out, _ = self.log_normalize(np.array(Table_Out))
    return Table_Out

  def add_tag(self, Table_F, tag):
    mess = np.array(Table_F)
    mess[:,0] = mess[:,0].astype('int32')^tag
    mess = mess[mess[:,0].argsort()]
    return mess
  
  def propagate_add(self, KEY, K_A, K_B, L_A, L_B, tag):
    KEY = self.multi_normalize(KEY)
    K_A = self.multi_normalize(K_A)
    K_B = self.multi_normalize(K_B)
    L_A = self.multi_normalize(L_A)
    L_B = self.multi_normalize(L_B)
    for frag in range(0, self.table_number):
      K_AB = self.convolution(K_A[frag], K_B[frag])
      L_AB = self.convolution(L_A[frag], L_B[frag])
      L_AB = self.add_tag(L_AB, tag[frag])
      self.Great_Table[frag][:,1] += (KEY[frag][:,1]+K_AB[:,1]+L_AB[:,1])
    return np.array(self.multi_normalize(self.Great_Table))


