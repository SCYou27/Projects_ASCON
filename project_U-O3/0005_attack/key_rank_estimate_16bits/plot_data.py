import numpy as np
import sys

Line = '\\hline\n\\#Traces     '
H_GE = 'Histogram LGE'
for L in range(1, 11):
  LGEs = []
  for t in range(0, 1000):
    LGEs.append(np.load('Rank_log/L'+str(L).zfill(2)+'/rank_log_'+str(t).zfill(4)+'.npy')[1])
  LGEs = np.array(LGEs)
  Est_GE = np.mean(LGEs)
  Line += ' & '+str(L).rjust(6)
  H_GE += ' & '+format(Est_GE, '0.4f')

Line += ('\\\\\n\\hline\n'+H_GE+'\\\\\n\\hline\n')
print(Line)

