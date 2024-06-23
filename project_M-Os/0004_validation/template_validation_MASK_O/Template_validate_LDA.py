import numpy as np
import time
import sys
import os
import serv_manager as svm
import h5py

TAG = '004'
PPC = 10

def sortPos(val):
  return val[1]

class Template:
  def __init__(self, func):
    self.Size = 2
    self.name = func
    print(('Initializing '+self.name))
    fname = 'templateLDA_O'+TAG+'/template_'+func+'/template'
    self.INV = []
    self.EXP = []
    self.AVE = []
    self.ICs = []
    label = 'ics_union_'+TAG+'/ics_'+func+'_L'
    for lane in range(0, self.Size):
      ics_name = label+str(lane).zfill(2)+'.npy'
      ics_lane = svm.Load(ics_name)
      self.ICs.append(ics_lane)
    for frag in range(0, (8*self.Size)):
      Sname = fname+'_scov_b'+str(frag).zfill(3)+'.npy'
      Scov = svm.Load(Sname)
      matS = np.matrix(Scov)
      ImatS = matS.I
      self.INV.append(ImatS)
      Aname = fname+'_avts_b'+str(frag).zfill(3)+'.npy'
      Avecs = svm.Load(Aname)
      Amat =  np.matrix(Avecs)
      self.AVE.append(Amat)
      Ename = fname+'_expect_b'+str(frag).zfill(3)+'.npy'
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
      for frag in range(8*lane, 8*lane+8):
        Poss = []
        Xm = ips_mat*self.AVE[frag]
        ImatS = self.INV[frag]
        matX = np.matrix(np.ones((256, 1)))*Xm - self.EXP[frag]
        pos = np.exp(-0.5*abs(np.sum(np.array(matX*ImatS)*np.array(matX), axis=1)))
        for x in range(0, 256):
          tempPoss = []
          tempPoss.append(x)
          tempPoss.append(pos[x])
          Poss.append(tempPoss)
        if sortbyprob:
          Poss.sort(reverse=True, key = sortPos)
        for x in range(0, 256):
          if Poss[x][0]==ANSWERs[frag]:
            Rank_Table.append(x)
    return np.array(Rank_Table)

def resample_5(trace):
  New_Trace = []
  New_Len = len(trace)//5
  for t in range(0, New_Len):
    New_Trace.append(sum(trace[(5*t):(5*t+5)]))
  return np.array(New_Trace)

def main(set_n, trace_number=100):
  Set_Size = 100
  Rank_KEY = np.zeros((0, 16))
  Rank_K_A = np.zeros((0, 16))
  Rank_K_B = np.zeros((0, 16))
  Rank_L_A = np.zeros((0, 16))
  Rank_L_B = np.zeros((0, 16))
  Rank_T_A = np.zeros((0, 16))
  Rank_T_B = np.zeros((0, 16))
  KEY_Ans = []
  K_A_Ans = []
  K_B_Ans = []
  L_A_Ans = []
  L_B_Ans = []
  T_A_Ans = []
  T_B_Ans = []
  print('Loading Answers...')
  for frag in range(0, 16):
    KEY_Ans.append(svm.Load(('intermediate_values/intermediate_B_KEY/KEY_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
    K_A_Ans.append(svm.Load(('intermediate_values/intermediate_B_K_A/K_A_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
    K_B_Ans.append(svm.Load(('intermediate_values/intermediate_B_K_B/K_B_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
    L_A_Ans.append(svm.Load(('intermediate_values/intermediate_B_L_A/L_A_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
    L_B_Ans.append(svm.Load(('intermediate_values/intermediate_B_L_B/L_B_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
    T_A_Ans.append(svm.Load(('intermediate_values/intermediate_B_T_A/T_A_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
    T_B_Ans.append(svm.Load(('intermediate_values/intermediate_B_T_B/T_B_b'+str(frag).zfill(3)+'.npy'))[(set_n*Set_Size):(set_n*Set_Size+Set_Size)])
  KEY_Ans = np.transpose(np.vstack(KEY_Ans))
  K_A_Ans = np.transpose(np.vstack(K_A_Ans))
  K_B_Ans = np.transpose(np.vstack(K_B_Ans))
  L_A_Ans = np.transpose(np.vstack(L_A_Ans))
  L_B_Ans = np.transpose(np.vstack(L_B_Ans))
  T_A_Ans = np.transpose(np.vstack(T_A_Ans))
  T_B_Ans = np.transpose(np.vstack(T_B_Ans))
  Template_KEY = Template('KEY')
  Template_K_A = Template('K_A')
  Template_K_B = Template('K_B')
  Template_L_A = Template('L_A')
  Template_L_B = Template('L_B')
  Template_T_A = Template('T_A')
  Template_T_B = Template('T_B')
  ########################################################################
  hdf5_name = '../Samples/Samples_VA_'+str(set_n).zfill(4)+'.hdf5'
  FILE = h5py.File(hdf5_name, 'r')
  for tr in range(0, trace_number):
    print('====================================================')
    print(time.asctime())
    print(('trace index: '+str(Set_Size*set_n+tr).zfill(4)))
    temp = FILE['traces'][tr,:]
    trace = resample_5(temp)
    Guess_KEY = Template_KEY.Guess(trace, KEY_Ans[tr], True)
    Guess_K_A = Template_K_A.Guess(trace, K_A_Ans[tr], True)
    Guess_K_B = Template_K_B.Guess(trace, K_B_Ans[tr], True)
    Guess_L_A = Template_L_A.Guess(trace, L_A_Ans[tr], True)
    Guess_L_B = Template_L_B.Guess(trace, L_B_Ans[tr], True)
    Guess_T_A = Template_T_A.Guess(trace, T_A_Ans[tr], True)
    Guess_T_B = Template_T_B.Guess(trace, T_B_Ans[tr], True)
    Rank_KEY = np.vstack([Rank_KEY, Guess_KEY])
    Rank_K_A = np.vstack([Rank_K_A, Guess_K_A])
    Rank_K_B = np.vstack([Rank_K_B, Guess_K_B])
    Rank_L_A = np.vstack([Rank_L_A, Guess_L_A])
    Rank_L_B = np.vstack([Rank_L_B, Guess_L_B])
    Rank_T_A = np.vstack([Rank_T_A, Guess_T_A])
    Rank_T_B = np.vstack([Rank_T_B, Guess_T_B])
  Rank_KEY = np.transpose(Rank_KEY)
  Rank_K_A = np.transpose(Rank_K_A)
  Rank_K_B = np.transpose(Rank_K_B)
  Rank_L_A = np.transpose(Rank_L_A)
  Rank_L_B = np.transpose(Rank_L_B)
  Rank_T_A = np.transpose(Rank_T_A)
  Rank_T_B = np.transpose(Rank_T_B)
  for frag in range(0, 16):
    rankname_KEY = './Rank_O'+TAG+'/rank_KEY_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_K_A = './Rank_O'+TAG+'/rank_K_A_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_K_B = './Rank_O'+TAG+'/rank_K_B_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_L_A = './Rank_O'+TAG+'/rank_L_A_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_L_B = './Rank_O'+TAG+'/rank_L_B_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_T_A = './Rank_O'+TAG+'/rank_T_A_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_T_B = './Rank_O'+TAG+'/rank_T_B_b'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    print('Saving '+rankname_KEY)
    svm.Save(rankname_KEY, Rank_KEY[frag])
    print('Saving '+rankname_K_A)
    svm.Save(rankname_K_A, Rank_K_A[frag])
    print('Saving '+rankname_K_B)
    svm.Save(rankname_K_B, Rank_K_B[frag])
    print('Saving '+rankname_L_A)
    svm.Save(rankname_L_A, Rank_L_A[frag])
    print('Saving '+rankname_L_B)
    svm.Save(rankname_L_B, Rank_L_B[frag])
    print('Saving '+rankname_T_A)
    svm.Save(rankname_T_A, Rank_T_A[frag])
    print('Saving '+rankname_T_B)
    svm.Save(rankname_T_B, Rank_T_B[frag])
  return

if __name__=='__main__':
  Set_n = 37
  TN = 10
  main(Set_n, TN)
  print('==========================================')
  print('Finished!')
  print(time.asctime())



