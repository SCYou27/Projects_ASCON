import numpy as np

def combine(TAG, frag):
  OutName = 'intermediate_values/intermediate_D_'+TAG+'/'+TAG+'_d'+str(frag).zfill(3)+'.npy'
  H_Name = 'intermediate_values_old/intermediate_B_'+TAG+'/'+TAG+'_b'+str((frag*2  )).zfill(3)+'.npy'
  L_Name = 'intermediate_values_old/intermediate_B_'+TAG+'/'+TAG+'_b'+str((frag*2+1)).zfill(3)+'.npy'
  H_Bytes = np.load(H_Name)
  L_Bytes = np.load(L_Name)
  Combined = H_Bytes*256+L_Bytes
  np.save(OutName, Combined)
  return

if __name__=='__main__':
  for t in range(0, 8):
    combine('KEY', t)
  for t in range(12, 20):
    combine('F_B11', t)

