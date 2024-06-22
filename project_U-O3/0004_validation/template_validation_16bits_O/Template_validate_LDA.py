import os
ncore = "1"
os.environ["OMP_NUM_THREADS"] = ncore
os.environ["OPENBLAS_NUM_THREADS"] = ncore
os.environ["MKL_NUM_THREADS"] = ncore
os.environ["VECLIB_MAXIMUM_THREADS"] = ncore
os.environ["NUMEXPR_NUM_THREADS"] = ncore
import numpy as np
import time
import sys
import serv_manager as svm
import h5py

PPC = 10
BOUND = '004'
TAG_TEMPLATE = 'O'+BOUND+'_16bit'

def sortPos(val):
  return val[1]

class Template:
  def __init__(self, func):
    if func=='KEY':
      self.Size = 2
      self.Offset = 0
    elif func=='F_B11':
      self.Size = 2
      self.Offset = 3
    else:
       print(('Class init error: '+func))
       sys.exit()
    self.name = func
    label = 'ics_union_'+BOUND+'/ics_'+func+'_L'
    print(('Initializing '+self.name))
    self.ICs = []
    fname = 'templateLDA_'+TAG_TEMPLATE+'/template_'+func+'/template'
    self.INV = []
    self.EXP = []
    self.AVE = []
    for lane in range(self.Offset, self.Offset+self.Size):
      ics_name = label+str(lane).zfill(2)+'.npy'
      ics_lane = svm.Load(ics_name)
      self.ICs.append(ics_lane)
    for frag in range((4*self.Offset), (4*(self.Offset+self.Size))):
      Sname = fname+'_scov_d'+str(frag).zfill(3)+'.npy'
      Scov = svm.Load(Sname)
      matS = np.matrix(Scov)
      ImatS = matS.I
      self.INV.append(ImatS)
      Aname = fname+'_avts_d'+str(frag).zfill(3)+'.npy'
      Avecs = svm.Load(Aname)
      Amat =  np.matrix(Avecs)
      self.AVE.append(Amat)
      Ename = fname+'_expect_d'+str(frag).zfill(3)+'.npy'
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
      for frag in range(4*lane, 4*lane+4):
        Poss = []
        Xm = ips_mat*self.AVE[frag]
        ImatS = self.INV[frag]
        matX = np.matrix(np.ones((2**16, 1)))*Xm - self.EXP[frag]
        pos = np.exp(-0.5*abs(np.sum(np.array(matX*ImatS)*np.array(matX), axis=1)))
        for x in range(0, 2**16):
          tempPoss = []
          tempPoss.append(x)
          tempPoss.append(pos[x])
          Poss.append(tempPoss)
        if sortbyprob:
          Poss.sort(reverse=True, key = sortPos)
        for x in range(0, 2**16):
          if Poss[x][0]==ANSWERs[frag]:
            Rank_Table.append(x)
    return np.array(Rank_Table)

def main(set_n, trace_number=1000):
  Set_Size = 1000
  Rank_KEY = []
  Rank_F_B11 = []
  ########################################################################
  KEY_Ans = []
  F_B11_Ans = []
  ########################################################################
  print('Loading Answers...')
  ########################################################################
  for frag in range(0, 8):
    KEY_Ans.append(svm.Load(('intermediate_values/intermediate_D_KEY/KEY_d'+str(frag).zfill(3)+'.npy')))
    F_B11_Ans.append(svm.Load(('intermediate_values/intermediate_D_F_B11/F_B11_d'+str((12+frag)).zfill(3)+'.npy')))
  ########################################################################
  KEY_Ans   = np.transpose(np.vstack(KEY_Ans))[(Set_Size*set_n):(Set_Size*set_n+Set_Size)]
  F_B11_Ans = np.transpose(np.vstack(F_B11_Ans))[(Set_Size*set_n):(Set_Size*set_n+Set_Size)]
  ########################################################################
  Template_KEY   = Template('KEY')
  Template_F_B11 = Template('F_B11')
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
    Guess_KEY = Template_KEY.Guess(trace, KEY_Ans[tr], True)
    Guess_F_B11 = Template_F_B11.Guess(trace, F_B11_Ans[tr], True)
    Rank_KEY.append(Guess_KEY)
    Rank_F_B11.append(Guess_F_B11)
    print('KEY:  ', Guess_KEY)
    print('F_B11:', Guess_F_B11)
  ########################################################################
  Rank_KEY = np.transpose(Rank_KEY)
  Rank_F_B11 = np.transpose(Rank_F_B11)
  for frag in range(0, 8):
    rankname_KEY =   './Rank_O'+BOUND+'/rank_KEY_d'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    rankname_XOR = './Rank_O'+BOUND+'/rank_XOR_d'+str(frag).zfill(3)+'_s'+str(set_n).zfill(3)+'.npy'
    print('Saving '+rankname_KEY)
    svm.Save(rankname_KEY, Rank_KEY[frag])
    print('Saving '+rankname_XOR)
    svm.Save(rankname_XOR, Rank_F_B11[frag])
  return

if __name__=='__main__':
  Set_n = 3
  TN = 10
  main(Set_n, TN)
  print('==========================================')
  print('Finished!')
  print(time.asctime())



