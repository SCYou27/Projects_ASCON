import numpy as np
import time
import sys
import os
import serv_manager as svm
import h5py

PPC = 10
BOUND = '004'

def sortPos(val):
  return val[1]

class Template:
  def __init__(self, func):
    if func=='KEY':
      self.Size = 2
    elif func=='F_INP':
      self.Size = 5
    elif (func[0:3]=='I_A')or(func[0:3]=='I_B')or(func[0:3]=='F_A')or(func[0:3]=='F_B'):
      if (int(func[3:5])>=0)and(int(func[3:5])<12):
        self.Size = 5
      else:
        print(('Class init error: '+func))
        sys.exit()
    else:
       print(('Class init error: '+func))
       sys.exit()
    self.name = func
    label = 'ics_union_'+BOUND+'/ics_'+func+'_L'
    print(('Initializing '+self.name))
    self.ICs = []
    fname = 'templateLDA_O'+BOUND+'/template_'+func+'/template'
    self.INV = []
    self.EXP = []
    self.AVE = []
    for lane in range(0, self.Size):
      ics_name = label+str(lane).zfill(2)+'.npy'
      ics_lane = svm.Load(ics_name)
      self.ICs.append(ics_lane)
    for byte in range(0, (8*self.Size)):
      Sname = fname+'_scov_s'+str(byte).zfill(3)+'.npy'
      Scov = svm.Load(Sname)
      matS = np.matrix(Scov)
      ImatS = matS.I
      self.INV.append(ImatS)
      Aname = fname+'_avts_s'+str(byte).zfill(3)+'.npy'
      Avecs = svm.Load(Aname)
      Amat =  np.matrix(Avecs)
      self.AVE.append(Amat)
      Ename = fname+'_expect_s'+str(byte).zfill(3)+'.npy'
      Tmeans = svm.Load(Ename)
      Emat = np.matrix(Tmeans)
      self.EXP.append(Emat)

  def Guess(self, Trace, ANSWERs, sortbyprob=False):
    #print(('Guessing '+self.name))
    Rank_Table = []
    for lane in range(0, self.Size):
      ips = []
      for ic in range(0, len(self.ICs[lane])):
        for p in range(0, PPC):
          indx = self.ICs[lane][ic]*PPC+p
          ips.append(Trace[indx])
      ips_mat = np.matrix(ips)
      for byte in range(8*lane, 8*lane+8):
        Poss = []
        Xm = ips_mat*self.AVE[byte]
        ImatS = self.INV[byte]
        matX = np.matrix(np.ones((256, 1)))*Xm - self.EXP[byte]
        pos = np.exp(-0.5*abs(np.sum(np.array(matX*ImatS)*np.array(matX), axis=1)))
        for x in range(0, 256):
          tempPoss = []
          tempPoss.append(x)
          tempPoss.append(pos[x])
          Poss.append(tempPoss)
        if sortbyprob:
          Poss.sort(reverse=True, key = sortPos)
        for x in range(0, 256):
          if Poss[x][0]==ANSWERs[byte]:
            Rank_Table.append(x)
    return np.array(Rank_Table)

def main(set_n, trace_number=1000):
  Set_Size = 1000
  Ranks_I_A = []
  Ranks_I_B = []
  Ranks_F_A = []
  Ranks_F_B = []
  for rd in range(0, 12):
    Ranks_I_A.append(np.zeros((0, 40)))
    Ranks_I_B.append(np.zeros((0, 40)))
    Ranks_F_A.append(np.zeros((0, 40)))
    Ranks_F_B.append(np.zeros((0, 40)))
  Rank_F_INP = np.zeros((0, 40))
  Rank_KEY = np.zeros((0, 16))
  ########################################################################
  I_A_ANS = []
  I_B_ANS = []
  F_A_ANS = []
  F_B_ANS = []
  for rd in range(0, 12):
    I_A_ANS.append(np.zeros((0, Set_Size)))
    I_B_ANS.append(np.zeros((0, Set_Size)))
    F_A_ANS.append(np.zeros((0, Set_Size)))
    F_B_ANS.append(np.zeros((0, Set_Size)))
  F_INP_Ans = np.zeros((0, Set_Size))
  KEY_Ans = np.zeros((0, Set_Size))
  ########################################################################
  print('Loading Answers...')
  ########################################################################
  for byte in range(0, 40):
    for rd in range(0, 12):
      temp_Ans = svm.Load(('intermediate_values/intermediate_S_I_A'+str(rd).zfill(2)+'/I_A'+str(rd).zfill(2)+'_s'+str(byte).zfill(3)+'.npy'))
      I_A_ANS[rd] = np.vstack([I_A_ANS[rd], temp_Ans[(set_n*Set_Size):(set_n*Set_Size+Set_Size)]])
      temp_Ans = svm.Load(('intermediate_values/intermediate_S_I_B'+str(rd).zfill(2)+'/I_B'+str(rd).zfill(2)+'_s'+str(byte).zfill(3)+'.npy'))
      I_B_ANS[rd] = np.vstack([I_B_ANS[rd], temp_Ans[(set_n*Set_Size):(set_n*Set_Size+Set_Size)]])
      temp_Ans = svm.Load(('intermediate_values/intermediate_S_F_A'+str(rd).zfill(2)+'/F_A'+str(rd).zfill(2)+'_s'+str(byte).zfill(3)+'.npy'))
      F_A_ANS[rd] = np.vstack([F_A_ANS[rd], temp_Ans[(set_n*Set_Size):(set_n*Set_Size+Set_Size)]])
      temp_Ans = svm.Load(('intermediate_values/intermediate_S_F_B'+str(rd).zfill(2)+'/F_B'+str(rd).zfill(2)+'_s'+str(byte).zfill(3)+'.npy'))
      F_B_ANS[rd] = np.vstack([F_B_ANS[rd], temp_Ans[(set_n*Set_Size):(set_n*Set_Size+Set_Size)]])
    temp_Ans = svm.Load(('intermediate_values/intermediate_S_F_INP/F_INP_s'+str(byte).zfill(3)+'.npy'))
    F_INP_Ans = np.vstack([F_INP_Ans, temp_Ans[(set_n*Set_Size):(set_n*Set_Size+Set_Size)]])
    if byte>=16:
      continue
    temp_Ans = svm.Load(('intermediate_values/intermediate_S_KEY/KEY_s'+str(byte).zfill(3)+'.npy'))
    KEY_Ans = np.vstack([KEY_Ans, temp_Ans[(set_n*Set_Size):(set_n*Set_Size+Set_Size)]])
  ########################################################################
  for rd in range(0, 12):
    I_A_ANS[rd] = np.transpose(I_A_ANS[rd])
    I_B_ANS[rd] = np.transpose(I_B_ANS[rd])
    F_A_ANS[rd] = np.transpose(F_A_ANS[rd])
    F_B_ANS[rd] = np.transpose(F_B_ANS[rd])
  F_INP_Ans = np.transpose(F_INP_Ans)
  KEY_Ans = np.transpose(KEY_Ans)
  ########################################################################
  Templates_I_A = []
  Templates_I_B = []
  Templates_F_A = []
  Templates_F_B = []
  for rd in range(0, 12):
    Templates_I_A.append(Template(('I_A'+str(rd).zfill(2))))
    Templates_I_B.append(Template(('I_B'+str(rd).zfill(2))))
    Templates_F_A.append(Template(('F_A'+str(rd).zfill(2))))
    Templates_F_B.append(Template(('F_B'+str(rd).zfill(2))))
  Template_F_INP = Template('F_INP')
  Template_KEY = Template('KEY')
  ########################################################################
  trace_name = '../Resample_HDF5/part_'+str(set_n).zfill(2)+'.hdf5'
  print('Loading '+trace_name)
  FILE = h5py.File(trace_name, 'r')
  Traces = FILE['Traces'][()]
  FILE.close()
  ########################################################################
  for tr in range(0, trace_number):
    print('====================================================')
    print(time.asctime())
    print(('trace index: '+str(Set_Size*set_n+tr).zfill(4)))
    trace = Traces[tr]
    for rd in range(0, 12):
      Guess = Templates_I_A[rd].Guess(trace, I_A_ANS[rd][tr], True)
      Ranks_I_A[rd] = np.vstack([Ranks_I_A[rd], Guess])
      #
      Guess = Templates_I_B[rd].Guess(trace, I_B_ANS[rd][tr], True)
      Ranks_I_B[rd] = np.vstack([Ranks_I_B[rd], Guess])
      #
      Guess = Templates_F_A[rd].Guess(trace, F_A_ANS[rd][tr], True)
      Ranks_F_A[rd] = np.vstack([Ranks_F_A[rd], Guess])
      #
      Guess = Templates_F_B[rd].Guess(trace, F_B_ANS[rd][tr], True)
      Ranks_F_B[rd] = np.vstack([Ranks_F_B[rd], Guess])
    Guess_F_INP = Template_F_INP.Guess(trace, F_INP_Ans[tr], True)
    Rank_F_INP = np.vstack([Rank_F_INP, Guess_F_INP])
    Guess_KEY = Template_KEY.Guess(trace, KEY_Ans[tr], True)
    Rank_KEY = np.vstack([Rank_KEY, Guess_KEY])
  ########################################################################
  for rd in range(0, 12):
    Ranks_I_A[rd] = np.transpose(Ranks_I_A[rd])
    Ranks_I_B[rd] = np.transpose(Ranks_I_B[rd])
    Ranks_F_A[rd] = np.transpose(Ranks_F_A[rd])
    Ranks_F_B[rd] = np.transpose(Ranks_F_B[rd])
  Rank_F_INP = np.transpose(Rank_F_INP)
  Rank_KEY = np.transpose(Rank_KEY)
  for byte in range(0, 40):
    for rd in range(0, 12):
      rankname_I_A = './Rank_O'+BOUND+'/rank_I_A'+str(rd).zfill(2)+'_b'+str(byte).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
      rankname_I_B = './Rank_O'+BOUND+'/rank_I_B'+str(rd).zfill(2)+'_b'+str(byte).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
      rankname_F_A = './Rank_O'+BOUND+'/rank_F_A'+str(rd).zfill(2)+'_b'+str(byte).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
      rankname_F_B = './Rank_O'+BOUND+'/rank_F_B'+str(rd).zfill(2)+'_b'+str(byte).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
      print('Saving '+rankname_I_A)
      svm.Save(rankname_I_A, Ranks_I_A[rd][byte])
      print('Saving '+rankname_I_B)
      svm.Save(rankname_I_B, Ranks_I_B[rd][byte])
      print('Saving '+rankname_F_A)
      svm.Save(rankname_F_A, Ranks_F_A[rd][byte])
      print('Saving '+rankname_F_B)
      svm.Save(rankname_F_B, Ranks_F_B[rd][byte])
    rankname_F_INP = './Rank_O'+BOUND+'/rank_F_INP_b'+str(byte).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    print('Saving '+rankname_F_INP)
    svm.Save(rankname_F_INP, Rank_F_INP[byte])
    if byte>=16:
      continue
    rankname_KEY = './Rank_O'+BOUND+'/rank_KEY_b'+str(byte).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    print('Saving '+rankname_KEY)
    svm.Save(rankname_KEY, Rank_KEY[byte])
  return

if __name__=='__main__':
  Set_n = 3
  TN = 10
  main(Set_n, TN)
  print('==========================================')
  print('Finished!')
  print(time.asctime())



