import numpy as np
import sys

Max = 24

Name = sys.argv[1]
Results = np.load(Name+'.npy')
Line = Name+'\n'
Line += '\\hline\n\\#Traces & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 20 & 50 & 100\\\\\n\\hline\n'
H_GE = 'Histogram LGE'
H_SR = 'Histogram $2^{'+str(Max)+'}$ SR  '
E_SR = 'Enumeration $2^{'+str(Max)+'}$ SR'
for t in range(0, 13):
  Tables = Results[:,t,:]
  Histogram = Tables[:,2]
  Enumeration = Tables[:,3]
  Est_GE = np.mean(np.log2(Histogram))
  H_GE += ' & '+format(Est_GE, '0.4f')
  Est_SR = np.count_nonzero((Histogram<=2**Max)&(Histogram>0))/len(Histogram)
  Act_SR = np.count_nonzero((Enumeration<=2**Max)&(Enumeration>0))/len(Enumeration)
  H_SR += ' & '+format(Est_SR, '0.3f')
  E_SR += ' & '+format(Act_SR, '0.3f')
Line += (H_GE+'\\\\\n\\hline\n'+H_SR+'\\\\\n\\hline\n'+E_SR+'\\\\\n\\hline\n\n')
print(Line)

