import numpy as np
import matplotlib.pyplot as plt
import sys

def plot_32(L, U):
  plt.figure(figsize=(15, 10))
  TAGs = ['KEY', 'K_A', 'K_B', 'L_A', 'L_B', 'T_A', 'T_B']
  for tag in TAGs:
    for int_s in range(0, 4):
      filename = './detect_results_32/'+tag+'_r_squ_i'+str(int_s).zfill(3)+'.npy'
      Rsq = np.load(filename)[L:U]
      plt.plot(Rsq, label=(tag+' '+str(int_s)))
  plt.legend()
  plt.show()
  return

if __name__=='__main__':
  # python3 plot_all.py
  try:
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
  except:
    lower = 0
    upper = 18000
  plot_32(lower, upper)

