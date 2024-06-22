import os
import sys
import numpy as np
Set_Number = 400
GROUP_SIZE = 160

Tr_Mat = np.matrix([[128],[64],[32],[16],[8],[4],[2],[1]])

str2num = {'0': 0, '1': 1, '2': 2, '3': 3,\
           '4': 4, '5': 5, '6': 6, '7': 7,\
           '8': 8, '9': 9, 'a':10, 'b':11,\
           'c':12, 'd':13, 'e':14, 'f':15 }

def intermediate_translate(tag):
  if tag=='KEY':
    Size = 16
  elif (tag[0]=='I')or(tag[0]=='F'):
    Size = 40
  else:
    print("Error: wrong tag.")
    return
  InterBits = []
  for b in range(0, Size):
    InterBits.append([])
  hex_name = "intermediate_HEX/"+tag+"_HEX.npy"
  HEXs = np.load(hex_name)
  out_dir = "./intermediate_values/intermediate_B_"+tag+"/"
  os.system(("mkdir "+out_dir))
  for t in range(0, (Set_Number*GROUP_SIZE)):
    print("Processing trace #"+str(t))
    in_str = HEXs[t]
    for b in range(0, Size):
      bits = [-1.0]*8
      byte = str2num[(in_str[(2*b)])]*16+str2num[(in_str[(2*b+1)])]
      bit_str = bin(byte)[2:].zfill(8)
      for bt in range(0, 8):
        bits[bt] = float(bit_str[bt])
      InterBits[b].append(bits)
  for b in range(0, Size):
    outname = out_dir+tag+"_b"+str(b).zfill(3)+".npy"
    print("Saving "+outname)
    np.save(outname, InterBits[b])
  return

def checking(tag):
  if tag=='KEY':
    Size = 16
  elif (tag[0]=='I')or(tag[0]=='F'):
    Size = 40
  else:
    print("Error: wrong tag.")
    return
  byte_dir = "./intermediate_values/intermediate_B_"+tag+"/"
  hex_name = "intermediate_HEX/"+tag+"_HEX.npy"
  Str_hex = np.load(hex_name)
  for b in range(0, Size):
    byte_name = byte_dir+tag+"_b"+str(b).zfill(3)+".npy"
    X_byte = np.load(byte_name)
    ANS = X_byte*Tr_Mat
    for t in range(0, (Set_Number*GROUP_SIZE)):
      x_hex = Str_hex[t][(2*b):(2*b+2)]
      x_byte = hex(int(ANS.item(t)))[2:].zfill(2)
      #print(b, t, x_hex, x_byte)
      if x_hex!=x_byte:
        print(tag+" Error:", b, t)
        return
  print(tag+": All passed!")
  return
        
if __name__=='__main__':
  Func = sys.argv[1]
  Tags = ['KEY']
  groups = ['I', 'F']
  for g in groups:
    Tags.append((g+'_INP'))
    for rd in range(0, 12):
      Tags.append((g+'_A'+str(rd).zfill(2)))
      Tags.append((g+'_B'+str(rd).zfill(2)))
  if Func=='cal':
    for tag in Tags:
      intermediate_translate(tag)
  elif Func=='check':
    for tag in Tags:
      checking(tag)

