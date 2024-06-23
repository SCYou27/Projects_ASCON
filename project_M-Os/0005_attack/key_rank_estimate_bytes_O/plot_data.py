import numpy as np
import sys

lower = int(sys.argv[1])
upper = int(sys.argv[2])

Line = '\\hline\n\\#Traces     '
H_GE = 'Histogram LGE'
for L in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]:
  LGEs = []
  for t in range(lower, upper):
    LGEs.append(np.load('Rank_log/L'+str(L).zfill(4)+'/rank_log_'+str(t).zfill(4)+'.npy')[1])
  LGEs = np.array(LGEs)
  Est_GE = np.mean(LGEs)
  Line += ' & '+str(L).rjust(7)
  H_GE += ' & '+format(Est_GE, '0.4f').rjust(7)

Line += ('\\\\\n\\hline\n'+H_GE+'\\\\\n\\hline\n')
print(Line)

