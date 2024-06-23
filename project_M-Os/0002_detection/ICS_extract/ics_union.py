import numpy as np
import sys
import os
def ICS_Detect(Dir_u_s, Dir_u_o, Dir_new, tag, bnd):
  Size = 2
  print('Tag = '+tag+', Bound = '+str(bnd))
  for L in range(0, Size):
    ics_name_uni = Dir_new+'ics_'+tag+'_L'+str(L).zfill(2)+'.npy'
    ICS_H = np.load((Dir_u_o+'ics_'+tag+'_i'+str(2*L  ).zfill(2)+'.npy'))
    ICS_L = np.load((Dir_u_o+'ics_'+tag+'_i'+str(2*L+1).zfill(2)+'.npy'))
    ICS_E = np.load((Dir_u_s+'ics_'+tag+'_i'+str(2*L  ).zfill(2)+'.npy'))
    ICS_O = np.load((Dir_u_s+'ics_'+tag+'_i'+str(2*L+1).zfill(2)+'.npy'))
    ICS = np.union1d(np.union1d(ICS_H, ICS_L), np.union1d(ICS_E, ICS_O)) 
    print('  Lane #'+str(L).zfill(2)+', Count = '+str(len(ICS)))
    np.save(ics_name_uni, ICS)
  return

if __name__=='__main__':
  BND = float(sys.argv[1])
  dirname_u_s = 'ics_sliced_'+str(int(BND*1000)).zfill(3)+'/'
  dirname_u_o = 'ics_original_'+str(int(BND*1000)).zfill(3)+'/'
  dirname_new = 'ics_union_'+str(int(BND*1000)).zfill(3)+'/'
  zipname_u_s = dirname_u_s[:-1]+'.zip'
  zipname_u_o = dirname_u_o[:-1]+'.zip'
  zipname_new = dirname_new[:-1]+'.zip'
  os.system(('unzip '+zipname_u_s))
  os.system(('unzip '+zipname_u_o))
  os.system(('mkdir '+dirname_new))
  for tag in ['KEY', 'K_A', 'K_B', 'L_A', 'L_B', 'T_A', 'T_B', 'TAG']:
    ICS_Detect(dirname_u_s, dirname_u_o, dirname_new, tag, BND)
  os.system(('zip -qq '+zipname_new+' -r '+dirname_new))
  os.system(('rm -r '+dirname_u_s+' '+dirname_u_o+' '+dirname_new))
