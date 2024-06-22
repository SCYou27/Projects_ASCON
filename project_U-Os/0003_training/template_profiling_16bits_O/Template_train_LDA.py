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
TAG = 'O'+Bound+'_16bit'

alphabet2number = {
    "0":0,  "1":1,  "2":2,  "3":3,
    "4":4,  "5":5,  "6":6,  "7":7,
    "8":8,  "9":9,  "a":10, "b":11,
    "c":12, "d":13, "e":14, "f":15
}

Bits = Bit_Gen.BitGen(16).Bits

class Profiling:
  def __init__(self):
    Trace_Blocks = []
    for pt in range(0, 8):
      fname = '../Resample_HDF5/part_'+str(pt).zfill(2)+'.hdf5'
      print('Loading '+fname)
      FILE = h5py.File(fname, 'r')
      Trace_Blocks.append(FILE['Traces'][()])
      FILE.close()
    self.Trace_Blocks = np.vstack(Trace_Blocks)
    return
  
  def load_ics(self, ics_set):
    print('Size of ICS:', len(ics_set))
    Traces = []
    for ic in range(0, len(ics_set)):
      lower = PPC*ics_set[ic]
      upper = lower+PPC
      Traces.append(self.Trace_Blocks[:, lower:upper])
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
    for frag in range(4*lane, 4*lane+4):
      print("  ++++++++++")
      print([frag, group])
      ## Get Models ##################
      print("Loading Intermediate Values (in bits)...", time.asctime())
      intername = "./intermediate_values/intermediate_D_"+group+"/"+group+"_d"+str(frag).zfill(3)+".npy"
      InterBits = svm.Load(intername)[0:Total_Tnum]
      print("Linear Regression", time.asctime())
      reg = LinearRegression().fit(InterBits, Re_Traces)
      Expect = reg.predict(InterBits)
      ## Adding B #########################################
      print("  Adding B", time.asctime())
      sub_inter = Expect-np.matrix(np.ones((Total_Tnum, 1)))*np.matrix(reg.predict(0.5*np.ones((1, 16))))
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
      Scov *= 1.0/(float(Total_Tnum-17))
      #######################################################
      fname = "./templateLDA_"+TAG+"/template_"+group+"/template"
      Sname = fname+"_scov_d"+str(frag).zfill(3)+".npy"
      svm.Save(Sname, Scov)
      Aname = fname+"_avts_d"+str(frag).zfill(3)+".npy"
      svm.Save(Aname, AVectors)
      Expects = np.matrix(reg.predict(np.array(Bits)))*AVectors
      Ename = fname+"_expect_d"+str(frag).zfill(3)+".npy"
      svm.Save(Ename, Expects)
      print("  Finished.", time.asctime())
    return
  
  def profile(self, tag, L, U):
    tS = time.time()
    print(time.asctime())
    #e.g. tag = 'I_A00'
    for lane in range(L, U):
      self.training(lane, tag)
      print(time.asctime())
    tE = time.time()
    print("Exe. time = ", tE-tS)
    return

if __name__=='__main__':
  Building = Profiling()
  Building.profile('F_B11', 3, 5)

