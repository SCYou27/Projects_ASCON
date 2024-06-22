import numpy as np
import time
import sys
import math

PLUS = 0

def table2bins(Table, bin_size, Trunc_Size):
  table_size = len(Table)
  NegLogPs = -np.around(Table[:,1]/bin_size)
  Freqs = []
  for T in range(0, Trunc_Size):
    Freqs.append(np.count_nonzero(NegLogPs==T))
  return np.array(Freqs, dtype=np.uint64)

def conv_recursive(Histograms, Trunc_Size):
  if len(Histograms)==1:
    return Histograms[0]
  else:
    Mid = len(Histograms)//2
    first  = conv_recursive(Histograms[:Mid], Trunc_Size)
    second = conv_recursive(Histograms[Mid:], Trunc_Size)
    return np.convolve(first, second)[:Trunc_Size]

def Estimate_GE(ANSWERs, Tables, bin_size):
  NegRightLogPs = 0
  Bin_init = []
  Mid = len(Tables)//2
  for t in range(0, len(Tables)):
    NegRightLogPs += (-Tables[t][ANSWERs[t]][1])
  Correct_bin = int(np.around(NegRightLogPs/bin_size))
  Trunc_Size = Correct_bin+1+PLUS
  for t in range(0, len(Tables)):
    Bin_init.append(table2bins(Tables[t], bin_size, Trunc_Size))
  print('  Correct answer lies in bin #'+str(Correct_bin))
  first  = np.array(conv_recursive(Bin_init[:Mid], Trunc_Size), dtype='object')
  second = np.array(conv_recursive(Bin_init[Mid:], Trunc_Size), dtype='object')
  Final_Histograms = np.convolve(first, second)
  if Correct_bin<=PLUS:
    lower = 1
  else:
    lower = np.sum(Final_Histograms[:(Correct_bin-PLUS)])
  upper = np.sum(Final_Histograms[:Trunc_Size])
  return lower, upper, math.log2(lower), math.log2(upper)

