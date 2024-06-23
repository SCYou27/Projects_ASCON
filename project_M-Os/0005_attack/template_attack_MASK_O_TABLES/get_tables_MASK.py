import numpy as np
import time
import sys
import os
import serv_manager as svm

TAG = '004'
PPC = 10

class Template:
  def __init__(self, func):
    lower = 0
    upper = 2
    self.name = func
    print(('Initializing '+self.name))
    self.ICs = []
    fname = 'templateLDA_O'+TAG+'/template_'+func+'/template'
    self.INV = []
    self.EXP = []
    self.AVE = []
    label = 'ics_union_'+TAG+'/ics_'+func+'_L'
    for lane in range(lower, upper):
      ics_name = label+str(lane).zfill(2)+'.npy'
      ics_lane = svm.Load(ics_name)
      self.ICs.append(ics_lane)
    for frag in range((8*lower), (8*upper)):
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
    return
  
  def Guess(self, Trace):
    #print(('Guessing '+self.name))
    Byte_Prob_Table = []
    for lane in range(0, 2):
      ips = []
      for ic in range(0, len(self.ICs[lane])):
        for p in range(0, PPC):
          indx = self.ICs[lane][ic]*PPC+p
          ips.append(Trace[indx])
      ips_mat = np.matrix(ips)
      for frag in range(8*lane, 8*lane+8):
        Xm = ips_mat*self.AVE[frag]
        ImatS = self.INV[frag]
        matX = np.matrix(np.ones((256, 1)))*Xm - self.EXP[frag]
        pos = -0.5*abs(np.sum(np.array(matX*ImatS)*np.array(matX), axis=1))
        Prob = np.transpose(np.vstack([np.arange(256.0), pos]))
        Byte_Prob_Table.append(Prob)
    return np.array(Byte_Prob_Table)

class Template_Recovering:
  def __init__(self):
    print('Template initalization')
    self.Template_KEY = Template('KEY')
    self.Template_K_A = Template('K_A')
    self.Template_K_B = Template('K_B')
    self.Template_L_A = Template('L_A')
    self.Template_L_B = Template('L_B')
    return
  
  def recover(self, trace):
    Guess_KEY = self.Template_KEY.Guess(trace)
    Guess_K_A = self.Template_K_A.Guess(trace)
    Guess_K_B = self.Template_K_B.Guess(trace)
    Guess_L_A = self.Template_L_A.Guess(trace)
    Guess_L_B = self.Template_L_B.Guess(trace)
    return Guess_KEY, Guess_K_A, Guess_K_B, Guess_L_A, Guess_L_B


