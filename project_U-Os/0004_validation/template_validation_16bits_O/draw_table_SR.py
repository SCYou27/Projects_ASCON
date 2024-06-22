import numpy as np
import sys

BOUND = '004'
Dir_Name = "./Rank_O"+BOUND+"/"

def Draw(func, outname, L, U):
  Ranks = []
  Tnum = 1000.0*(U-L)
  for f in range(0, 8):
    Ranks.append([])
  for f in range(0, 8):
    print(("Fragment #"+str(f).zfill(3)))
    frag_head = Dir_Name+"rank_"+func+"_d"+str(f).zfill(3)
    for sets in range(L, U):
      filename = frag_head+"_s"+str(sets).zfill(3)+".npy" 
      res = np.load(filename)
      for t in range(0, len(res)):
        Ranks[f].append(res[t])
  Output_str = "\\begin{tabular}{|c|*{8}{r|}}\n\\hline\n\\Fragment "
  for f in range(0, 8):
    Output_str += ("&\n\\multicolumn{1}{c|}{"+str(f)+"}")
  Output_str += "\\\\\n\\hline\n"
  lan_str = "SR "
  for f in range(0, 8):
    num = Ranks[f].count(0)
    num = num/Tnum
    temp = (format(num, '0.3f')).zfill(7)
    lan_str += (" & "+temp)
  lan_str += "\\\\\n\\hline\n"
  Output_str += lan_str
  Output_str += "\\end{tabular}"
  print(Output_str)
  ofile = open(outname, "w")
  ofile.write(Output_str)
  ofile.close()

if __name__=='__main__':
  Func = sys.argv[1]
  Group = int(sys.argv[2])
  Otn = "Result_Tables/SR_table_"+Func+"_G"+str(Group)+".txt"
  Lower = Group
  Upper = Group+1
  Draw(Func, Otn, Lower, Upper)

