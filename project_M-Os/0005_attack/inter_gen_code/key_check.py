import numpy as np
import sys

GROUP_SIZE = 100
SET_NUM = 1000

def check(L, U):
  # Checking =================================================#
  for g in range(L, U):
    set_keys = np.load(("keys/key_"+str(g).zfill(4)+".npy"))
    First = set_keys[0]
    for t in range(0, GROUP_SIZE):
      check = (set_keys[t]==First)
      print("Set #"+str(g).zfill(4)+", Trace #"+str(t).zfill(4)+":", check)
      print(set_keys[t])
      print(First)
      if check==False:
        exit()
  print("ALL passed!")
  return

if __name__=='__main__':
  check(int(sys.argv[1]), int(sys.argv[2]))
