import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import serv_manager as svm
import time
import h5py

OUTSIZE = 2560
GROUPSIZE = 160
SETS = 100

class Scatter_Model:
  def __init__(self):
    print('Loading Samples...', time.asctime())
    self.Samples = []
    fname = '../get_samples/Detect_Samples.hdf5'
    FILE = h5py.File(fname, 'r')
    for t in range(0, SETS):
      OutputTag = 'set_DN_'+str(t).zfill(4)
      print('Loading '+OutputTag)
      self.Samples.append(FILE[OutputTag][()])
    FILE.close()
    self.Samples = np.vstack(self.Samples)
    print('Shape of trace samples:', np.shape(self.Samples), time.asctime())
    return
  
  def get_values(self, intermediate_bits):
    Expect = np.matrix(np.zeros(((GROUPSIZE*SETS), OUTSIZE)))
    Scores = []
    for bt in range(0, 4):
      print('Linear Regression '+str(bt), time.asctime())
      reg = LinearRegression().fit(intermediate_bits[bt], self.Samples)
      expect_byte = reg.predict(intermediate_bits[bt])
      Scores.append(r2_score(self.Samples, expect_byte, multioutput='raw_values'))
    print('Finished', time.asctime())
    return np.array(Scores)

def detect(MODEL, TAG, lower, upper):
  for ints in range(lower, upper):
    tS = time.time()
    NAME_TAG = TAG+'_i'+str(ints).zfill(3)
    intermediate_bits = []
    for byte in range(4*ints, 4*ints+4):
      BYTE_TAG = TAG+'_b'+str(byte).zfill(3)
      print(BYTE_TAG)
      intermediate_bits.append(svm.Load('intermediate_values/intermediate_B_'+TAG+'/'+BYTE_TAG+'.npy'))
    Scores = MODEL.get_values(intermediate_bits)
    for bt in range(0, 4):
      byte = ints*4+bt
      fname = './detect_results_08/'+TAG+'_r_squ_b'+str(byte).zfill(3)+'.npy'
      svm.Save(fname, Scores[bt])
    outname = './detect_results_32/'+TAG+'_r_squ_i'+str(ints).zfill(3)+'.npy'
    svm.Save(outname, np.sum(Scores, axis=0))
    tE = time.time()
    print('Exe. time =', (tE-tS))
  return

if __name__=='__main__':
  model = Scatter_Model()
  detect(model, 'KEY', 0, 2)
  detect(model, 'F_B03', 4, 6)


