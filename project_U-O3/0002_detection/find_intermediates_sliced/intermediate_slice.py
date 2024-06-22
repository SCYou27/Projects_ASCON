import os
import sys
import numpy as np

def intermediate_translate(tag):
  if tag=='KEY':
    LANES = 2
  else:
    LANES = 5
  in_dir = "./intermediate_values_bytes/intermediate_B_"+tag+"/"
  out_dir = "./intermediate_values/intermediate_S_"+tag+"/"
  os.system(("mkdir "+out_dir))
  for lane in range(0, LANES):
    InterValues = []
    for byte in range((8*lane), (8*lane+8)):
      Name = in_dir+tag+"_b"+str(byte).zfill(3)+".npy"
      InterValues.append(np.load(Name))
    InterValues = np.hstack(InterValues)
    ###############################################
    Inter_E = []
    Inter_O = []
    for bit in range(0, 32):
      Inter_O.append(InterValues[:,(2*bit+0):(2*bit+1)])
      Inter_E.append(InterValues[:,(2*bit+1):(2*bit+2)])
    Inter_E = np.hstack(Inter_E)
    Inter_O = np.hstack(Inter_O)
    for byte in range(0, 4):
      outname_E = out_dir+tag+"_s"+str(8*lane+byte).zfill(3)+".npy"
      print("Saving "+outname_E)
      np.save(outname_E, Inter_E[:,(8*byte):(8*byte+8)])
      outname_O = out_dir+tag+"_s"+str(8*lane+4+byte).zfill(3)+".npy"
      print("Saving "+outname_O)
      np.save(outname_O, Inter_O[:,(8*byte):(8*byte+8)])
  return

if __name__=='__main__':
  Tags = ['KEY', 'I_INP', 'F_INP']
  groups = ['I', 'F']
  for g in groups:
    for rd in range(0, 12):
      Tags.append((g+'_A'+str(rd).zfill(2)))
      Tags.append((g+'_B'+str(rd).zfill(2)))
  for tag in Tags:
    intermediate_translate(tag)

