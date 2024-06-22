import numpy as np
import sys
import os
def ICS_Detect(Dir, tag, bnd):
  if tag=='KEY':
    Size = 4
  else:
    Size = 10
  print('Tag = '+tag+', Bound = '+str(bnd))
  for N in range(0, Size):
    ics_name = Dir+'ics_'+tag+'_i'+str(N).zfill(2)+'.npy'
    ICS = []
    name = 'detect_results_32/'+tag+'_r_squ_i'+str(N).zfill(3)+'.npy'
    T = np.load(name)
    Count = 0
    for t in range(0, 2560):
      if T[t]>bnd:
        Count+=1
        ICS.append(t)
    print('  Reg #'+str(N).zfill(2)+', Count = '+str(Count))
    np.save(ics_name, ICS)
  return

if __name__=='__main__':
  BND = float(sys.argv[1])
  dirname = 'ics_sliced_'+str(int(BND*1000)).zfill(3)+'/'
  zipname = dirname[:-1]+'.zip'
  os.system(('mkdir '+dirname))
  ICS_Detect(dirname, 'KEY', BND)
  ICS_Detect(dirname, 'F_INP', BND)
  for g in ['I_A', 'I_B', 'F_A', 'F_B']:
    for rd in range(0, 12):
      tag = g+str(rd).zfill(2)
      ICS_Detect(dirname, tag, BND)
  os.system(('zip -qq '+zipname+' -r '+dirname))
  os.system(('rm -r '+dirname))
