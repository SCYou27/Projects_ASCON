import Template_validate_LDA as template
import sys
L = int(sys.argv[1])
U = int(sys.argv[2])
PPC = 10
for tSet in range(L, U):
  template.main(tSet)
  print("++++++++++++++++++++++++++++++++++++++++++++++++++")
