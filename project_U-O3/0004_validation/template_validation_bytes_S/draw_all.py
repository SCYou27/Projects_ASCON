import os
import sys
def process(N_group):
  Tag = ['KEY', 'F_INP']
  for head in ['I_A', 'I_B', 'F_A', 'F_B']:
    for rd in range(0, 12):
      Tag.append((head+str(rd).zfill(2)))
  print(Tag)
  TB = ['SR', 'GE']
  for G in range(0, N_group):
    for T in Tag:
      for N in TB:
        cmd = "python3 draw_table_"+N+".py "+T+" "+str(G)
        print(cmd)
        os.system(cmd)
  return

if __name__=='__main__':
  process(int(sys.argv[1]))


