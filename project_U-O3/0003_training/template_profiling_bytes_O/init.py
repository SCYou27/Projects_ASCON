import os
import sys
Tag = sys.argv[1]
os.system(('mkdir templateLDA_'+Tag+'/template_KEY/'))
os.system(('mkdir templateLDA_'+Tag+'/template_F_INP/'))
for S in ['I', 'F']:
  for G in ['A', 'B']:
    for rd in range(0, 12):
      tag = S+'_'+G+str(rd).zfill(2)
      cmd = 'mkdir templateLDA_'+Tag+'/template_'+tag+'/'
      os.system(cmd)
