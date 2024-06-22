import os
import sys
def process(N_group):
  Tag = ['KEY', 'XOR']
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


