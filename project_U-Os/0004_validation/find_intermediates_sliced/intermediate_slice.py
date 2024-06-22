import os
import sys
import numpy as np

MASK = 2**np.array([7,6,5,4,3,2,1,0])
SUMUP = np.matrix(MASK)

def combine(byte_array):
  Output = []
  for bit in range(0, 8):
    Output.append(np.array(np.array((byte_array&MASK[bit]), dtype=bool), dtype=np.uint32))
  return np.vstack(Output)

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
      InterValues.append(combine(np.load(Name)))
    InterValues = np.vstack(InterValues)
    ###############################################
    Inter_E = []
    Inter_O = []
    for bit in range(0, 32):
      Inter_O.append(InterValues[(2*bit+0)])
      Inter_E.append(InterValues[(2*bit+1)])
    Inter_E = np.vstack(Inter_E)
    Inter_O = np.vstack(Inter_O)
    for byte in range(0, 4):
      outname_E = out_dir+tag+"_s"+str(8*lane+byte).zfill(3)+".npy"
      print("Saving "+outname_E)
      np.save(outname_E, np.array(SUMUP*np.matrix(Inter_E[(8*byte):(8*byte+8)]))[0])
      outname_O = out_dir+tag+"_s"+str(8*lane+4+byte).zfill(3)+".npy"
      print("Saving "+outname_O)
      np.save(outname_O, np.array(SUMUP*np.matrix(Inter_O[(8*byte):(8*byte+8)]))[0])
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

