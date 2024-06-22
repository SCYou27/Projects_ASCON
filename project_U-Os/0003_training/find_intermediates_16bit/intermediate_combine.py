import os
import sys
import numpy as np

def intermediate_translate(tag):
  if tag=='KEY':
    Size = 8
  elif (tag[0]=='I')or(tag[0]=='F'):
    Size = 20
  else:
    print("Error: wrong tag.")
    return
  in_dir = "./intermediate_values_bytes/intermediate_B_"+tag+"/"
  out_dir = "./intermediate_values/intermediate_D_"+tag+"/"
  os.system(("mkdir "+out_dir))
  for f in range(0, Size):
    Name_H = in_dir+tag+"_b"+str((2*f+0)).zfill(3)+".npy"
    Name_L = in_dir+tag+"_b"+str((2*f+1)).zfill(3)+".npy"
    Fragment = np.hstack([np.load(Name_H), np.load(Name_L)])
    outname = out_dir+tag+"_d"+str(f).zfill(3)+".npy"
    print("Saving "+outname)
    np.save(outname, Fragment)
  return

if __name__=='__main__':
  Tags = ['KEY']
  groups = ['I', 'F']
  for g in groups:
    Tags.append((g+'_INP'))
    for rd in range(0, 12):
      Tags.append((g+'_A'+str(rd).zfill(2)))
      Tags.append((g+'_B'+str(rd).zfill(2)))
  for tag in Tags:
    intermediate_translate(tag)

