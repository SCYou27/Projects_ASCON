import numpy as np
import time
import sys
import os
import serv_manager as svm
import marginalization

PPC = 10
BOUND = '004'

class Template:
  def __init__(self, func):
    self.Marginalizer = marginalization.Marginalization(8)
    if func=="KEY":
      self.Size = 2
    else:
      self.Size = 5
    if func=="KEY":
      self.Type = 'b'
    else:
      self.Type = 's'
    self.name = func
    label = "ics_union_"+BOUND+"/ics_"+func+"_L"
    print(("Initializing "+self.name+", Type: "+self.Type))
    self.ICs = []
    fname = "templateLDA_O"+BOUND+"/template_"+func+"/template"
    self.INV = []
    self.EXP = []
    self.AVE = []
    for lane in range(0, self.Size):
      ics_name = label+str(lane).zfill(2)+".npy"
      ics_lane = svm.Load(ics_name)
      self.ICs.append(ics_lane)
    for byte in range(0, (8*self.Size)):
      Sname = fname+"_scov_"+self.Type+str(byte).zfill(3)+".npy"
      Scov = svm.Load(Sname)
      matS = np.matrix(Scov)
      ImatS = matS.I
      self.INV.append(ImatS)
      Aname = fname+"_avts_"+self.Type+str(byte).zfill(3)+".npy"
      Avecs = svm.Load(Aname)
      Amat =  np.matrix(Avecs)
      self.AVE.append(Amat)
      Ename = fname+"_expect_"+self.Type+str(byte).zfill(3)+".npy"
      Tmeans = svm.Load(Ename)
      Emat = np.matrix(Tmeans)
      self.EXP.append(Emat)

  def Guess(self, Trace):
    #print(("Guessing "+self.name))
    Byte_Prob_Table = []
    for lane in range(0, self.Size):
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
        pos = np.exp(-0.5*abs(np.sum(np.array(matX*ImatS)*np.array(matX), axis=1)))
        pos = pos/sum(pos)
        Prob = np.transpose(np.vstack([np.arange(256.0), pos]))
        Byte_Prob_Table.append(Prob)
    if self.Type=='s':
      return marginalization.slice_recover(self.Marginalizer.marginalize(np.array(Byte_Prob_Table)))
    else:
      return self.Marginalizer.marginalize(np.array(Byte_Prob_Table))

class Template_Recovering:
  def __init__(self, Tag='KEY'):
    self.Tag = Tag
    print("Template initalization")
    if (self.Tag=='KEY')or(self.Tag=='INIT')or(self.Tag=='CPA'):
      self.Template_KEY = Template("KEY")
    if (self.Tag=='INIT')or(self.Tag=='CPA'):
      self.Templates_I_A = []
      self.Templates_I_B = []
      for rd in range(0, 12):
        self.Templates_I_A.append(Template(("I_A"+str(rd).zfill(2))))
        self.Templates_I_B.append(Template(("I_B"+str(rd).zfill(2))))
    if self.Tag=='CPA':
      self.Template_F_INP = Template("F_INP")
      self.Templates_F_A = []
      self.Templates_F_B = []
      for rd in range(0, 12):
        self.Templates_F_A.append(Template(("F_A"+str(rd).zfill(2))))
        self.Templates_F_B.append(Template(("F_B"+str(rd).zfill(2))))
    return
  
  def recover(self, trace):
    if (self.Tag=='KEY')or(self.Tag=='INIT')or(self.Tag=='CPA'):
      Guess_KEY = self.Template_KEY.Guess(trace)
    if (self.Tag=='INIT')or(self.Tag=='CPA'):
      Guess_I_A = np.zeros((12, 2, 320))
      Guess_I_B = np.zeros((12, 2, 320))
      for rd in range(0, 12):
        Guess_I_A[rd] = self.Templates_I_A[rd].Guess(trace)
        Guess_I_B[rd] = self.Templates_I_B[rd].Guess(trace)
    if self.Tag=='CPA':
      Guess_F_INP = self.Template_F_INP.Guess(trace)
      Guess_F_A = np.zeros((12, 2, 320))
      Guess_F_B = np.zeros((12, 2, 320))
      for rd in range(0, 12):
        Guess_F_A[rd] = self.Templates_F_A[rd].Guess(trace)
        Guess_F_B[rd] = self.Templates_F_B[rd].Guess(trace)
    if self.Tag=='KEY':
      return Guess_KEY
    if self.Tag=='INIT':
      return Guess_KEY, Guess_I_A, Guess_I_B
    if self.Tag=='CPA':
      return Guess_KEY, Guess_F_INP, Guess_I_A, Guess_I_B, Guess_F_A, Guess_F_B


