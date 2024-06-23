import numpy as np
import time
import sys
import os
from numpy import linalg as LA
import scipy.stats as ss
from sklearn.linear_model import LinearRegression
import serv_manager as svm
import Bit_Gen
import h5py

Bound = '004'
Dir_ics = './ics_union_'+Bound+'/'
PPC = 10
RESAMPLE_RATE = 5
NEW_LEN = 12000
TAG = 'O'+Bound

alphabet2number = {
    "0":0,  "1":1,  "2":2,  "3":3,
    "4":4,  "5":5,  "6":6,  "7":7,
    "8":8,  "9":9,  "a":10, "b":11,
    "c":12, "d":13, "e":14, "f":15
}

Bits = Bit_Gen.BitGen(8).Bits

class Profiling:
  def __init__(self):
    self.Samples = []
    for set_n in range(0, 400):
      sample_block = []
      fname = '../Samples/Samples_TR_'+str(set_n).zfill(4)+'.hdf5'
      print('Open '+fname)
      FILE = h5py.File(fname, 'r')
      temp = np.matrix(FILE['traces'][()])
      for p in range(0, NEW_LEN):
        resample = temp[:,5*p]+temp[:,(5*p+1)]+temp[:,(5*p+2)]+temp[:,(5*p+3)]+temp[:,(5*p+4)]
        sample_block.append(resample)
      sample_block = np.hstack(sample_block)
      self.Samples.append(sample_block)
      FILE.close()
    self.Samples = np.array(np.vstack(self.Samples))
    print('Shape of Samples:', np.shape(self.Samples))
    return
  
  def load_ics(self, ics_set):
    print('Size of ICS:', len(ics_set))
    Traces = []
    for ic in range(0, len(ics_set)):
      lower = PPC*ics_set[ic]
      upper = lower+PPC
      Traces.append(self.Samples[:, lower:upper])
    return np.hstack(Traces)

  def training(self, lane, group):
    SETnum = 400
    Total_Tnum = SETnum*160
    print("==============")
    print([lane, group])
    icsname = Dir_ics+"ics_"+group+"_L"+str(lane).zfill(2)+".npy"
    ICS = svm.Load(icsname)
    Pnum = PPC*len(ICS)
    print("Loading Resampled Trace Data", time.asctime())
    Re_Traces = self.load_ics(ICS)
    print("Trace shape =", np.shape(Re_Traces), time.asctime())
    for byte in range(8*lane, 8*lane+8):
      print("  ++++++++++")
      print([byte, group])
      ## Get Models ##################
      print("Loading Intermediate Values (in bits)...", time.asctime())
      intername = "./intermediate_values/intermediate_S_"+group+"/"+group+"_s"+str(byte).zfill(3)+".npy"
      print("Loading file "+intername)
      InterBits = svm.Load(intername)[0:Total_Tnum]
      print("Linear Regression", time.asctime())
      reg = LinearRegression().fit(InterBits, Re_Traces)
      Expect = reg.predict(InterBits)
      ## Adding B #########################################
      print("  Adding B", time.asctime())
      sub_inter = Expect-np.matrix(np.ones((Total_Tnum, 1)))*np.matrix(reg.predict(0.5*np.ones((1, 8))))
      Bmat = np.transpose(sub_inter)*sub_inter
      ## Adding W #########################################
      print("  Adding W", time.asctime())
      sub_inner = np.matrix(Re_Traces)-Expect
      Wmat = np.transpose(sub_inner)*sub_inner
      #####################################################
      print("  Finding A", time.asctime())
      AVectors = []
      Target = (Wmat.I)*Bmat
      EigVLs, EigVRs = LA.eig(Target)
      tempEigVLs = abs(EigVLs)
      non_zero = 0
      for VIndx in range(0, len(tempEigVLs)):
        if tempEigVLs[VIndx]>(0.001*sum(tempEigVLs)):
          print(VIndx, tempEigVLs[VIndx])
          non_zero+=1
          AVectors.append(EigVRs[:,VIndx])
      AVectors = np.hstack(AVectors)
      print("("+str(non_zero)+" non-zero vectors)")
      print("Total: ", sum(tempEigVLs))
      print("  Compressing", time.asctime())
      Scov = np.transpose(AVectors)*Wmat*AVectors
      Scov *= 1.0/(float(Total_Tnum-9))
      #######################################################
      fname = "./templateLDA_"+TAG+"/template_"+group+"/template"
      Sname = fname+"_scov_s"+str(byte).zfill(3)+".npy"
      print("Saving file "+Sname)
      svm.Save(Sname, Scov)
      Aname = fname+"_avts_s"+str(byte).zfill(3)+".npy"
      print("Saving file "+Aname)
      svm.Save(Aname, AVectors)
      Expects = np.matrix(reg.predict(np.array(Bits)))*AVectors
      Ename = fname+"_expect_s"+str(byte).zfill(3)+".npy"
      print("Saving file "+Ename)
      svm.Save(Ename, Expects)
      print("  Finished.", time.asctime())
    return
  
  def profile(self, tag, L, U):
    tS = time.time()
    print(time.asctime())
    #e.g. tag = 'I_A00'
    for ints in range(L, U):
      self.training(ints, tag)
      print(time.asctime())
    tE = time.time()
    print("Exe. time = ", tE-tS)
    return

if __name__=='__main__':
  Building = Profiling()
  Building.profile('KEY', 0, 1)


