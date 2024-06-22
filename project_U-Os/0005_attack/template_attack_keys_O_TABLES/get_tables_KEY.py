import numpy as np
import time
import sys
import os
import serv_manager as svm

PPC = 10
BOUND = '004'

class Template:
  def __init__(self, func):
    if func=='KEY':
      lower = 0
      upper = 2
    elif func=='F_B11':
      lower = 3
      upper = 5
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
    for lane in range(lower, upper):
      ics_name = label+str(lane).zfill(2)+'.npy'
      ics_lane = svm.Load(ics_name)
      self.ICs.append(ics_lane)
    for byte in range((8*lower), (8*upper)):
      Sname = fname+'_scov_b'+str(byte).zfill(3)+'.npy'
      Scov = svm.Load(Sname)
      matS = np.matrix(Scov)
      ImatS = matS.I
      self.INV.append(ImatS)
      Aname = fname+'_avts_b'+str(byte).zfill(3)+'.npy'
      Avecs = svm.Load(Aname)
      Amat =  np.matrix(Avecs)
      self.AVE.append(Amat)
      Ename = fname+'_expect_b'+str(byte).zfill(3)+'.npy'
      Tmeans = svm.Load(Ename)
      Emat = np.matrix(Tmeans)
      self.EXP.append(Emat)
  
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
      for byte in range(8*lane, 8*lane+8):
        Xm = ips_mat*self.AVE[byte]
        ImatS = self.INV[byte]
        matX = np.matrix(np.ones((256, 1)))*Xm - self.EXP[byte]
        pos = -0.5*abs(np.sum(np.array(matX*ImatS)*np.array(matX), axis=1))
        Prob = np.transpose(np.vstack([np.arange(256.0), pos]))
        Byte_Prob_Table.append(Prob)
    return np.array(Byte_Prob_Table)

class Template_Recovering:
  def __init__(self):
    print('Template initalization')
    self.Template_KEY = Template('KEY')
    return
  
  def recover(self, trace):
    Guess_KEY = self.Template_KEY.Guess(trace)
    return Guess_KEY
