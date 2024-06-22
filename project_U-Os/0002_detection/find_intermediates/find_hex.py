import numpy as np
import sys

GROUP_SIZE = 160
SET_NUM = 100

def calculate():
  ## KEY ####################################################################
  Keys = []
  for set_n in range(0, SET_NUM):
    set_name = "keys/key_"+str(set_n).zfill(4)+".npy"
    print(set_name)
    set_keys = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      Keys.append(set_keys[t])
  np.save(("intermediate_HEX/KEY_HEX.npy"), Keys)
  ## INITIALIZATION & FINALIZATION ##########################################
  TAG = ['I', 'F']
  in_dir = "intermediate_HEX/intermediate_trace/"
  for tag in TAG:
    Values = []
    for s in range(0, 25):
      Values.append([])
    for set_n in range(0, SET_NUM):
      set_name = in_dir+tag+"_set_"+str(set_n).zfill(4)+".npy"
      print(set_name)
      set_values = np.load(set_name)
      for t in range(0, GROUP_SIZE):
        for s in range(0, 25):
          Values[s].append(set_values[t][s])
    np.save(("intermediate_HEX/"+tag+"_INP_HEX.npy"), Values[0])
    # A & B:
    for rd in range(0, 12):
      Name_A = "intermediate_HEX/"+tag+"_A"+str(rd).zfill(2)+"_HEX.npy"
      idx = 2*rd+1
      print(Name_A, idx)
      np.save(Name_A, Values[idx])
      #################################################################
      Name_B = "intermediate_HEX/"+tag+"_B"+str(rd).zfill(2)+"_HEX.npy"
      idx = 2*rd+2
      print(Name_B, idx)
      np.save(Name_B, Values[idx])
  return

def check():
  ## KEY ##########
  Keys = np.load("intermediate_HEX/KEY_HEX.npy")
  for set_n in range(0, SET_NUM):
    set_name = "keys/key_"+str(set_n).zfill(4)+".npy"
    set_keys = np.load(set_name)
    for t in range(0, GROUP_SIZE):
      check_value = (Keys[(set_n*GROUP_SIZE+t)]==set_keys[t])
      if check_value==False:
        print("Error: set #"+str(set_n).zfill(4)+" trace #"+str(t).zfill(4))
        exit()
  print("Key check complete.")
  TAG = ['I', 'F']
  in_dir = "intermediate_HEX/intermediate_trace/"
  for tag in TAG:
    Values = []
    for set_n in range(0, SET_NUM):
      set_name = in_dir+tag+"_set_"+str(set_n).zfill(4)+".npy"
      set_values = np.load(set_name)
      for t in range(0, GROUP_SIZE):
        Values.append(set_values[t])
    ############################################################################
    HEXs = np.load(("intermediate_HEX/"+tag+"_INP_HEX.npy"))
    for t in range(0, GROUP_SIZE*SET_NUM):
      check_value = (HEXs[t]==Values[t][0])
      if check_value==False:
        print("Error: set #"+str(set_n).zfill(4)+" trace #"+str(t).zfill(4))
        exit()
    print(tag+"_INP check complete.")
    ############################################################################
    for rd in range(0, 12):
      Name_A = "intermediate_HEX/"+tag+"_A"+str(rd).zfill(2)+"_HEX.npy"
      A_HEXs = np.load(Name_A)
      idx = 2*rd+1
      for t in range(0, GROUP_SIZE*SET_NUM):
        check_value = (A_HEXs[t]==Values[t][idx])
        if check_value==False:
          print("Error: set #"+str(set_n).zfill(4)+" trace #"+str(t).zfill(4))
          exit()
      print(tag+"_A"+str(rd).zfill(2)+" check complete.")
      ##########################################################################
      Name_B = "intermediate_HEX/"+tag+"_B"+str(rd).zfill(2)+"_HEX.npy"
      B_HEXs = np.load(Name_B)
      idx = 2*rd+2
      for t in range(0, GROUP_SIZE*SET_NUM):
        check_value = (B_HEXs[t]==Values[t][idx])
        if check_value==False:
          print("Error: set #"+str(set_n).zfill(4)+" trace #"+str(t).zfill(4))
          exit()
      print(tag+"_B"+str(rd).zfill(2)+" check complete.")
  return


if __name__=='__main__':
  Func = sys.argv[1]
  if (Func=='all')or(Func=='cal'):
    calculate()
  if (Func=='all')or(Func=='check'):
    check()
