import numpy as np
import sys

GROUP_SIZE = 100
REPEAT_SIZE = 10
SET_NUM = 100

def check(L, U):
  # Loading ==================================================#
  Key_List = []
  for g in range(0, REPEAT_SIZE):
    set_keys = np.load(("keys/key_"+str(g).zfill(4)+".npy"))
    Key_List.append(set_keys)
  # Checking =================================================#
  for g in range(L, U):
    set_keys = np.load(("keys/key_"+str(g).zfill(4)+".npy"))
    for t in range(0, GROUP_SIZE):
      check = (set_keys[t]==Key_List[(g%REPEAT_SIZE)][t])
      print("Set #"+str(g).zfill(4)+", Trace #"+str(t).zfill(4)+":", check)
      print(set_keys[t])
      print(Key_List[(g%REPEAT_SIZE)][t])
      if check==False:
        exit()
  print("ALL passed!")
  return

if __name__=='__main__':
  check(int(sys.argv[1]), int(sys.argv[2]))
