import numpy as np
import sys
import time
import serv_manager as svm
import table_gen

RC = [ 'f0', 'e1', 'd2', 'c3', 'b4', 'a5',\
       '96', '87', '78', '69', '5a', '4b']

#########################################
Damp = 0.99
Rate = 1.0/(1.0-Damp)-1.0
#########################################

def Norm(ARRAY):
  with np.errstate(divide='ignore', invalid='ignore'):
    T = np.sum(ARRAY, axis=0)
    ARRAY/=np.vstack([T,T])
    ARRAY = np.nan_to_num(ARRAY, copy=True, nan=0.0, posinf=0.0, neginf=0.0)
  return ARRAY

def Damping(OLD, NEW):
  return Norm((Norm(OLD)+Rate*Norm(NEW)))

class B_variable:
  def __init__(self, table=np.ones((2, 320))):
    self.I0 = table
    self.Size = len(table[0])
    self.RL = np.ones((2, self.Size))
    self.RN = np.ones((2, self.Size))
    return
  
  def Output_Q(self):
    QL = self.RN*self.I0
    QN = self.RL*self.I0
    return QL, QN
  
  def Renew_RL(self, R):
    self.RL = Damping(self.RL, R)
    return
  
  def Renew_RN(self, R):
    self.RN = Damping(self.RN, R)
  
  def Zeta(self):
    output = Norm(self.RL*self.RN*self.I0)
    return output

class A_variable:
  def __init__(self, table=np.ones((2, 320))):
    self.I0 = table
    self.Size = len(table[0])
    self.RN = np.ones((2, self.Size))
    self.RL0 = np.ones((2, self.Size))
    self.RL1 = np.ones((2, self.Size))
    self.RL2 = np.ones((2, self.Size))
    return
  
  def Output_Q(self):
    QN = self.RL0*self.RL1*self.RL2*self.I0
    QL0 = self.RN*self.RL1*self.RL2*self.I0
    QL1 = self.RN*self.RL0*self.RL2*self.I0
    QL2 = self.RN*self.RL0*self.RL1*self.I0
    return QN, QL0, QL1, QL2
  
  def Renew_RN(self, R):
    self.RN = Damping(self.RN, R)
    return
  
  def Renew_RL0(self, R):
    self.RL0 = Damping(self.RL0, R)
    return
  
  def Renew_RL1(self, R):
    self.RL1 = Damping(self.RL1, R)
    return
  
  def Renew_RL2(self, R):
    self.RL2 = Damping(self.RL2, R)
    return
  
  def Zeta(self):
    output = Norm(self.RN*self.RL0*self.RL1*self.RL2*self.I0)
    return output  

class K_variable:
  # Four-end variable. It should be the similar with A variable.
  def __init__(self, table=np.ones((2, 128))):
    self.I0 = table
    self.Size = len(table[0])
    self.Extern = np.ones((2, self.Size))
    self.I_Head = np.ones((2, self.Size))
    self.I_Tail = np.ones((2, self.Size))
    self.F_Head = np.ones((2, self.Size))
    self.F_Tail = np.ones((2, self.Size))
    return
  
  def Output_Q(self):
    QEX = self.I_Head*self.I_Tail*self.F_Head*self.F_Tail*self.I0
    QIH = self.Extern*self.I_Tail*self.F_Head*self.F_Tail*self.I0
    QIT = self.Extern*self.I_Head*self.F_Head*self.F_Tail*self.I0
    QFH = self.Extern*self.I_Head*self.I_Tail*self.F_Tail*self.I0
    QFT = self.Extern*self.I_Head*self.I_Tail*self.F_Head*self.I0
    return QEX, QIH, QIT, QFH, QFT
  
  def Renew_REX(self, R):
    self.Extern = Damping(self.Extern, R)
    return
  
  def Renew_RIH(self, R):
    self.I_Head = Damping(self.I_Head, R)
    return
  
  def Renew_RIT(self, R):
    self.I_Tail = Damping(self.I_Tail, R)
    return
  
  def Renew_RFH(self, R):
    self.F_Head = Damping(self.F_Head, R)
    return
  
  def Renew_RFT(self, R):
    self.F_Tail = Damping(self.F_Tail, R)
    return
  
  def Zeta(self):
    output = Norm(self.Extern*self.I_Head*self.I_Tail*self.F_Head*self.F_Tail*self.I0)
    return output

class S_constant:
  # Single-end. For IV, nonce, plaintext, tag.
  def __init__(self, table=np.ones((2, 320))):
    self.I0 = table
    return
  
  def Output_Q(self):
    Q = Norm(self.I0)
    return Q
  
  def Zeta(self):
    return self.Output_Q()

class XOR_factor:
  def __init__(self, Size = 320):
    self.Size = Size
    self.Q0 = np.ones((2, self.Size))
    self.Q1 = np.ones((2, self.Size))
    self.Q2 = np.ones((2, self.Size))
    return
  
  def Output_R(self):
    R0 = np.zeros((2, self.Size))
    R1 = np.zeros((2, self.Size))
    R2 = np.zeros((2, self.Size))
    for t0 in range(0, 2):
      for t1 in range(0, 2):
        t2 = (t0^t1)&0x1
        R0[t0] += self.Q1[t1]*self.Q2[t2]
        R1[t1] += self.Q0[t0]*self.Q2[t2]
        R2[t2] += self.Q0[t0]*self.Q1[t1]
    return R0, R1, R2
  
  def Renew_Q0(self, Q):
    self.Q0 = Damping(self.Q0, Q)
    return
  
  def Renew_Q1(self, Q):
    self.Q1 = Damping(self.Q1, Q)
    return
  
  def Renew_Q2(self, Q):
    self.Q2 = Damping(self.Q2, Q)
    return

class LINEAR_factor:
  def __init__(self):
    self.QA0 = np.ones((2, 320))
    self.QA1 = np.ones((2, 320))
    self.QA2 = np.ones((2, 320))
    self.QB = np.ones((2, 320))
    return
  
  def Output_R(self):
    RA0 = np.zeros((2, 320))
    RA1 = np.zeros((2, 320))
    RA2 = np.zeros((2, 320))
    RB = np.zeros((2, 320))
    for t0 in range(0, 2):
      for t1 in range(0, 2):
        for t2 in range(0, 2):
          tb = (t0^t1^t2)&0x1
          RA0[t0] += self.QA1[t1]*self.QA2[t2]*self.QB[tb]
          RA1[t1] += self.QA0[t0]*self.QA2[t2]*self.QB[tb]
          RA2[t2] += self.QA0[t0]*self.QA1[t1]*self.QB[tb]
          RB[tb] += self.QA0[t0]*self.QA1[t1]*self.QA2[t2]
    # rotation
    O0 = RA1[:,  0: 64]
    O1 = RA1[:, 64:128]
    O2 = RA1[:,128:192]
    O3 = RA1[:,192:256]
    O4 = RA1[:,256:320]
    O0 = np.hstack([O0[:,19:64], O0[:,0:19]])
    O1 = np.hstack([O1[:,61:64], O1[:,0:61]])
    O2 = np.hstack([O2[:, 1:64], O2[:,0: 1]])
    O3 = np.hstack([O3[:,10:64], O3[:,0:10]])
    O4 = np.hstack([O4[:, 7:64], O4[:,0: 7]])
    RA1 = np.hstack([O0, O1, O2, O3, O4])
    #
    O0 = RA2[:,  0: 64]
    O1 = RA2[:, 64:128]
    O2 = RA2[:,128:192]
    O3 = RA2[:,192:256]
    O4 = RA2[:,256:320]
    O0 = np.hstack([O0[:,28:64], O0[:,0:28]])
    O1 = np.hstack([O1[:,39:64], O1[:,0:39]])
    O2 = np.hstack([O2[:, 6:64], O2[:,0: 6]])
    O3 = np.hstack([O3[:,17:64], O3[:,0:17]])
    O4 = np.hstack([O4[:,41:64], O4[:,0:41]])
    RA2 = np.hstack([O0, O1, O2, O3, O4])
    return RA0, RA1, RA2, RB
  
  def Renew_QA0(self, Q):
    self.QA0 = Damping(self.QA0, Q)
    return
  
  def Renew_QA1(self, Q):
    O0 = Q[:, 0:64]
    O1 = Q[:, 64:128]
    O2 = Q[:,128:192]
    O3 = Q[:,192:256]
    O4 = Q[:,256:320]
    O0 = np.hstack([O0[:,(64-19):64], O0[:,0:(64-19)]])
    O1 = np.hstack([O1[:,(64-61):64], O1[:,0:(64-61)]])
    O2 = np.hstack([O2[:,(64- 1):64], O2[:,0:(64- 1)]])
    O3 = np.hstack([O3[:,(64-10):64], O3[:,0:(64-10)]])
    O4 = np.hstack([O4[:,(64- 7):64], O4[:,0:(64- 7)]])
    self.QA1 = Damping(self.QA1, np.hstack([O0, O1, O2, O3, O4]))
    return
  
  def Renew_QA2(self, Q):
    O0 = Q[:,  0: 64]
    O1 = Q[:, 64:128]
    O2 = Q[:,128:192]
    O3 = Q[:,192:256]
    O4 = Q[:,256:320]
    O0 = np.hstack([O0[:,(64-28):64], O0[:,0:(64-28)]])
    O1 = np.hstack([O1[:,(64-39):64], O1[:,0:(64-39)]])
    O2 = np.hstack([O2[:,(64- 6):64], O2[:,0:(64- 6)]])
    O3 = np.hstack([O3[:,(64-17):64], O3[:,0:(64-17)]])
    O4 = np.hstack([O4[:,(64-41):64], O4[:,0:(64-41)]])
    self.QA2 = Damping(self.QA2, np.hstack([O0, O1, O2, O3, O4]))
    return
  
  def Renew_QB(self, Q):
    self.QB = Damping(self.QB, Q)
    return

class NONLIN_factor:
  def __init__(self, RD = 0):
    self.S_Z = table_gen.find_table(RC[RD])
    self.S_O = np.ones((2, 8))-self.S_Z
    self.QA0 = np.ones((2, 64))
    self.QA1 = np.ones((2, 64))
    self.QA2 = np.ones((2, 64))
    self.QA3 = np.ones((2, 64))
    self.QA4 = np.ones((2, 64))
    self.QB0 = np.ones((2, 64))
    self.QB1 = np.ones((2, 64))
    self.QB2 = np.ones((2, 64))
    self.QB3 = np.ones((2, 64))
    self.QB4 = np.ones((2, 64))
    return
  
  def constraint(self, I0, I1, I2, I3, I4):
    x0 = I0^I4
    x4 = I4^I3
    x2 = I2^I1
    x3 = I3
    x1 = I1
    ###############################
    y0 = x0^((0x1^x1)&x2)
    y1 = x1^((0x1^x2)&x3)
    y2 = x2^((0x1^x3)&x4)
    y3 = x3^((0x1^x4)&x0)
    y4 = x4^((0x1^x0)&x1)
    ###############################
    O1 = (y1^y0)&0x1
    O0 = (y0^y4)&0x1
    O3 = (y3^y2)&0x1
    O2 = (y2^0x1)&0x1
    O4 = y4&0x1
    return O0, O1, O2, O3, O4
  
  def Output_R(self):
    RA0 = np.zeros((2, 64))
    RA1 = np.zeros((2, 64))
    RA2 = np.zeros((2, 64))
    RA3 = np.zeros((2, 64))
    RA4 = np.zeros((2, 64))
    RB0 = np.zeros((2, 64))
    RB1 = np.zeros((2, 64))
    RB2 = np.zeros((2, 64))
    RB3 = np.zeros((2, 64))
    RB4 = np.zeros((2, 64))
    for b0 in range(0, 2):
      for b1 in range(0, 2):
        for b2 in range(0, 2):
          for b3 in range(0, 2):
            for b4 in range(0, 2):
              a0, a1, a2, a3, a4 = self.constraint(b0, b1, b2, b3, b4)
              RA0[a0] += self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RA1[a1] += self.QA0[a0]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RA2[a2] += self.QA0[a0]*self.QA1[a1]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RA3[a3] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RA4[a4] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RB0[b0] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RB1[b1] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB2[b2]*self.QB3[b3]*self.QB4[b4]
              RB2[b2] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB3[b3]*self.QB4[b4]
              RB3[b3] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB4[b4]
              RB4[b4] += self.QA0[a0]*self.QA1[a1]*self.QA2[a2]*self.QA3[a3]*self.QA4[a4]*self.QB0[b0]*self.QB1[b1]*self.QB2[b2]*self.QB3[b3]
    BYTE = RB2[:,56:64]
    SWAP_Z = np.sum(BYTE*self.S_Z, axis=0)
    SWAP_O = np.sum(BYTE*self.S_O, axis=0)
    SWAP = np.vstack([SWAP_Z, SWAP_O])
    RB2 = np.hstack([RB2[:,0:56], SWAP])
    RA = np.hstack([RA0, RA1, RA2, RA3, RA4])
    RB = np.hstack([RB0, RB1, RB2, RB3, RB4])
    return RA, RB
  
  def Renew_QA(self, Q):
    self.QA0 = Damping(self.QA0, Q[:,0:64])
    self.QA1 = Damping(self.QA1, Q[:,64:128])
    self.QA2 = Damping(self.QA2, Q[:,128:192])
    self.QA3 = Damping(self.QA3, Q[:,192:256])
    self.QA4 = Damping(self.QA4, Q[:,256:320])
    return
  
  def Renew_QB(self, Q):
    self.QB0 = Damping(self.QB0, Q[:,0:64])
    self.QB1 = Damping(self.QB1, Q[:,64:128])
    BYTE = Q[:,184:192]
    SWAP_Z = np.sum(BYTE*self.S_Z, axis=0)
    SWAP_O = np.sum(BYTE*self.S_O, axis=0)
    SWAP = np.vstack([SWAP_Z, SWAP_O])
    self.QB2 = Damping(self.QB2, np.hstack([Q[:,128:184], SWAP]))
    self.QB3 = Damping(self.QB3, Q[:,192:256])
    self.QB4 = Damping(self.QB4, Q[:,256:320])
    return


class CPA_Graph:
  def __init__(self, I_A, I_B, F_A, F_B, I_INP, F_INP, Plain, Tag):
    self.ER = 12 # We need all the 12 rounds.
    # Initialization ##############################################
    self.I_A_V = []
    self.I_B_V = []
    self.I_NON_F = []
    self.I_LIN_F = []
    # for IV
    self.IV_V = S_constant(I_INP[:,0:64])
    # for Key
    self.KEY_V = K_variable(I_INP[:,64:192])
    # for Nonce
    self.NONCE_V = S_constant(I_INP[:,192:320])
    for rd in range(0, self.ER):
      self.I_A_V.append(A_variable(I_A[rd]))
      self.I_B_V.append(B_variable(I_B[rd]))
      self.I_NON_F.append(NONLIN_factor(rd))
      self.I_LIN_F.append(LINEAR_factor())
    # Middle #######################################################
    self.PLAIN_V = S_constant(Plain)
    self.MID_F = XOR_factor(320)
    # Finalization #################################################
    self.F_A_V = []
    self.F_B_V = []
    self.F_NON_F = []
    self.F_LIN_F = []
    # for input in finalization.
    self.F_IN_V = B_variable(F_INP)
    for rd in range(0, self.ER):
      self.F_A_V.append(A_variable(F_A[rd]))
      self.F_B_V.append(B_variable(F_B[rd]))
      self.F_NON_F.append(NONLIN_factor(rd))
      self.F_LIN_F.append(LINEAR_factor())
    # Tag ##########################################################
    self.TAG_V = S_constant(Tag)
    self.TAG_F = XOR_factor(128)
    return
 
  def R_renew(self, R_ex):
    # Initialization
    self.KEY_V.Renew_REX(R_ex)
    for rd in range(0, self.ER):
      # Non-linear factor outputs.
      NA, NB = self.I_NON_F[rd].Output_R()
      if rd == 0:
        # We do not renew IV variables.
        self.KEY_V.Renew_RIH(NB[:,64:192])
        # We do not renew nonce variables.
      else:
        self.I_B_V[(rd-1)].Renew_RN(NB)
      self.I_A_V[rd].Renew_RN(NA)
      # Linear factor outputs.
      LA0, LA1, LA2, LB = self.I_LIN_F[rd].Output_R()
      self.I_B_V[rd].Renew_RL(LB)
      self.I_A_V[rd].Renew_RL0(LA0)
      self.I_A_V[rd].Renew_RL1(LA1)
      self.I_A_V[rd].Renew_RL2(LA2)
    # Middle (Separator)
    X0, X1, X2 = self.MID_F.Output_R()
    self.I_B_V[(self.ER-1)].Renew_RN(X0)
    temp = X2[0][319]
    X2[0][319] = X2[1][319]
    X2[1][319] = temp
    self.F_IN_V.Renew_RL(X2)
    # We do not renew plaintext variables.
    # XOR the key in the beginning of the finalization stage.
    self.KEY_V.Renew_RFH(X1[:,64:192])
    # XOR the key in the end of the initialization stage.
    self.KEY_V.Renew_RIT(X1[:,192:320])
    # Finalization
    for rd in range(0, self.ER):
      # Non-linear factor outputs.
      NA, NB = self.F_NON_F[rd].Output_R()
      if rd == 0:
        self.F_IN_V.Renew_RN(NB)
      else:
        self.F_B_V[(rd-1)].Renew_RN(NB)
      self.F_A_V[rd].Renew_RN(NA)
      # Linear factor outputs.
      LA0, LA1, LA2, LB = self.F_LIN_F[rd].Output_R()
      self.F_B_V[rd].Renew_RL(LB)
      self.F_A_V[rd].Renew_RL0(LA0)
      self.F_A_V[rd].Renew_RL1(LA1)
      self.F_A_V[rd].Renew_RL2(LA2)
    # Tag
    X0, X1, _ = self.TAG_F.Output_R()
    self.F_B_V[(self.ER-1)].Renew_RN(np.hstack([np.ones((2, 192)), X0]))
    self.KEY_V.Renew_RFT(X1)
    # We do not renew tag variables.
    return
  
  def Q_renew(self):
    # Initialization
    # Input variable outputs.
    # For plaintext
    QPL = self.PLAIN_V.Output_Q()
    # For IV
    Q_IV = self.IV_V.Output_Q()
    # For Key
    QEX, QIH, QIT, QFH, QFT = self.KEY_V.Output_Q()
    self.MID_F.Renew_Q1(np.hstack([QPL, QFH, QIT]))
    self.TAG_F.Renew_Q1(QFT)
    # For Nonce
    Q_NC = self.NONCE_V.Output_Q()
    Q_state = np.hstack([Q_IV, QIH, Q_NC])
    for rd in range(0, self.ER):
      # Q from the last round.
      self.I_NON_F[rd].Renew_QB(Q_state)
      # A variable outputs.
      AN, AL0, AL1, AL2 = self.I_A_V[rd].Output_Q()
      self.I_NON_F[rd].Renew_QA(AN)
      self.I_LIN_F[rd].Renew_QA0(AL0)
      self.I_LIN_F[rd].Renew_QA1(AL1)
      self.I_LIN_F[rd].Renew_QA2(AL2)
      # B variable outputs.
      BL, Q_state = self.I_B_V[rd].Output_Q()
      self.I_LIN_F[rd].Renew_QB(BL)
    # Middle (From initialization)
    self.MID_F.Renew_Q0(Q_state)
    # Finalization
    # Input variable outputs.
    BL, Q_state = self.F_IN_V.Output_Q()
    temp = BL[0][319]
    BL[0][319] = BL[1][319]
    BL[1][319] = temp
    self.MID_F.Renew_Q2(BL)
    for rd in range(0, self.ER):
      # Q from the last round.
      self.F_NON_F[rd].Renew_QB(Q_state)
      # A variable outputs.
      AN, AL0, AL1, AL2 = self.F_A_V[rd].Output_Q()
      self.F_NON_F[rd].Renew_QA(AN)
      self.F_LIN_F[rd].Renew_QA0(AL0)
      self.F_LIN_F[rd].Renew_QA1(AL1)
      self.F_LIN_F[rd].Renew_QA2(AL2)
      # B variable outputs.
      BL, Q_state = self.F_B_V[rd].Output_Q()
      self.F_LIN_F[rd].Renew_QB(BL)
    # Tag
    self.TAG_F.Renew_Q0(Q_state[:,192:320])
    Q_tag = self.TAG_V.Output_Q()
    self.TAG_F.Renew_Q2(Q_tag)
    return QEX
  
  def Zeta_out(self):
    Out = []
    Z_IV = self.IV_V.Zeta()
    Z_KEY = self.KEY_V.Zeta()
    Z_NONCE = self.NONCE_V.Zeta()
    Out.append(np.hstack([Z_IV, Z_KEY, Z_NONCE]))
    for rd in range(0, self.ER):
      Out.append(self.I_A_V[rd].Zeta())
      Out.append(self.I_B_V[rd].Zeta())
    Out.append(self.F_IN_V.Zeta())
    for rd in range(0, self.ER):
      Out.append(self.F_A_V[rd].Zeta())
      Out.append(self.F_B_V[rd].Zeta())
    return np.array(Out)

class Ex_factor:
  def __init__(self, Size):
    self.Size = Size
    self.Q_Norm = 0.5*np.ones((self.Size, 2, 128))
    self.Q_Log = np.zeros((self.Size, 2, 128))
    self.Z_Log = np.zeros((2, 128))
    return
  
  def Norm_log(self, Arr=np.zeros((2, 128))):
    A_max = np.max(Arr, axis=0)
    Arr -= np.vstack([A_max]*2)
    return Arr
    
  def Output_R(self):
    R_Log = np.zeros((self.Size, 2, 128))
    for t in range(0, self.Size):
      R_Log[t] = self.Norm_log((self.Z_Log-self.Q_Log[t]))
    return np.exp(R_Log)
  
  def Renew_Q(self, Q):
    for t in range(0, self.Size):
      Q[t] = Norm(Q[t])
    self.Q_Norm = self.Q_Norm+Rate*Q
    for t in range(0, self.Size):
      self.Q_Norm[t] = Norm(self.Q_Norm[t])
    with np.errstate(divide='ignore', invalid='ignore'):
      self.Q_Log = np.nan_to_num(np.log(self.Q_Norm), copy=True, nan=0.0, posinf=0.0, neginf=-745.134)
    self.Z_Log = np.sum(self.Q_Log, axis=0)
    return
  
  def Zeta(self):
    return self.Norm_log(self.Z_Log)

class SASCA_Procedure:
  def __init__(self, KEY, F_INP, I_A, I_B, F_A, F_B, nonce, plaintext, cipher, tag):
    self.ER = 12
    self.Size = len(KEY)
    self.Leaves = []
    self.Ext_Factor = Ex_factor(self.Size)
    IV = table_gen.find_table('80400c0600000000')
    for t in range(0, self.Size):
      P_t = table_gen.find_table((plaintext[t]+'80'))
      T_t = table_gen.find_table(tag[t])
      NONCE = table_gen.find_table(nonce[t])
      I_t = np.hstack([IV, KEY[t], NONCE])
      C_t = table_gen.find_table(cipher[t])
      F_t = np.hstack([C_t, F_INP[t][:,56:320]])
      self.Leaves.append(CPA_Graph(I_A[t], I_B[t], F_A[t], F_B[t], I_t, F_t, P_t, T_t))
    return
  
  def __predict__(self, Prob_Table):
    table_size = len(Prob_Table[0])
    INT = 0
    for b in range(0, table_size):
      INT<<=1
      if Prob_Table[1][b]>=Prob_Table[0][b]:
        INT+=1
    Str = hex(INT)[2:].zfill((table_size//4))
    return Str

  def calculate(self, IT_Max = 1000):
    Prob = 0.5*np.ones((self.Size, 50, 2, 320))
    Q_ex = 0.5*np.ones((self.Size, 2, 128))
    Summation = np.zeros((self.Size))
    ################################################################################
    for t in range(0, IT_Max):
      R_ex = self.Ext_Factor.Output_R()
      for s in range(0, self.Size):
        self.Leaves[s].R_renew(R_ex[s])
        Q_ex[s] = self.Leaves[s].Q_renew()
        Prob_iteration = self.Leaves[s].Zeta_out()
        Summation[s] = np.sum(np.abs(Prob_iteration-Prob[s]))
        Prob[s] = Prob_iteration
      self.Ext_Factor.Renew_Q(Q_ex)
      S = np.sum(Summation)
      print("Iteration: "+str(t+1).zfill(4)+", "+str(S))
      if S<0.01:
        break
    END = t+1
    print("Ends:", END)
    ################################################################################
    Prediction = self.__predict__(self.Ext_Factor.Zeta())
    return END, Prediction

def testing(Size, key, nonce, plaintext, cipher, tag):
  KEY = np.array([table_gen.find_table(key)]*Size)
  F_INP = 0.5*np.ones((Size, 2, 320))
  I_A = 0.5*np.ones((Size, 12, 2, 320))
  I_B = 0.5*np.ones((Size, 12, 2, 320))
  F_A = 0.5*np.ones((Size, 12, 2, 320))
  F_B = 0.5*np.ones((Size, 12, 2, 320))
  Test = SASCA_Procedure(KEY, F_INP, I_A, I_B, F_A, F_B, nonce, plaintext, cipher, tag)
  end, prediction = Test.calculate(200)
  print("ANS    : 0x"+key)
  print("Predict: 0x"+prediction)
  print("Correct?", key==prediction)
  return end, prediction

if __name__=='__main__':
  INPUTS = [""]*5
  ################################################################################
  INPUTS[0] = [ '27d33d50fdd23f18481d40dca3629f23', \
               ['1601b97a7a555b99c4e231552cb50c46', '9c7a0a1e1f30be34307a47289303a068', \
                '99a495ac221e3c04684be4a856c07edf', 'b5d31e0f485cfe4c91bb8a449ca3803d', \
                'abc62d6835bcf3e48cb5843376a5fc35'], \
               ['d80313935a8b02', '67826919569979', '088d802dc6e500', 'b49608690d0002', 'e6ec76f39616e0'], \
               ['cff62f855e5f8d', '5af853db0c549d', '9ff41a37b9040c', '5917672cb08145', '77826bb4847b32'], \
               ['e6b06941ab54cbceaa1b6297527be3a7', 'bb132e842d45184f931f0ee44d6997e6', \
                '65f72c3381e1094d7d1b11b5ca7a03c4', 'ed8323291d9be9e48c6d00c927d7677a', \
                '8bd3aa25f52b19bab9a2e769facccab9']] # 003
  ################################################################################
  INPUTS[1] = [ 'dcabde2621c5a8d75f94d9671038db36', \
               ['6d4aaa42d465966f13e3609b0c58ec40', 'e8eadb78f33cddaad991ad80b8c4c213', \
                'cc944af5713dda9742e98b119862e59d', 'be2457eff37229182e77a906d6d542cd', \
                '35879aa889b45af13405b844c5fd8299'], \
               ['4d37183961d5b5', '37ba5b70848ee4', '03ba4a39c4e1ec', '9a2c46340662f6', 'eaa354bb904a0a'], \
               ['5996accc4650f2', 'a449736589974c', 'bab9aa88ace13c', '74a190d529fc1f', '4699de381ae778'], \
               ['d4d8e88d0217ebb7e288375b17c0f7e9', 'fd3b6a5c674748d3012188a9aa799a61', \
                'bf36ebcc70630ec17bf83038685b893f', 'ccbaf1e2ed45e54952991be3b68ce36d', \
                'f845caa440243d39ae446be934683db3']] # 774
  ################################################################################
  INPUTS[2] = [ 'dfabde2621c5a8d75f94d9671038db36', \
               ['6d4aaa42d465966f13e3609b0c58ec40', 'e8eadb78f33cddaad991ad80b8c4c213', \
                'cc944af5713dda9742e98b119862e59d', 'be2457eff37229182e77a906d6d542cd', \
                '35879aa889b45af13405b844c5fd8299'], \
               ['4d37183961d5b5', '37ba5b70848ee4', '03ba4a39c4e1ec', '9a2c46340662f6', 'eaa354bb904a0a'], \
               ['5996accc4650f2', 'a449736589974c', 'bab9aa88ace13c', '74a190d529fc1f', '4699de381ae778'], \
               ['d4d8e88d0217ebb7e288375b17c0f7e9', 'fd3b6a5c674748d3012188a9aa799a61', \
                'bf36ebcc70630ec17bf83038685b893f', 'ccbaf1e2ed45e54952991be3b68ce36d', \
                'f845caa440243d39ae446be934683db3']] # 774 Wrong Key
  ################################################################################
  INPUTS[3] = [ 'dcabde2621c5a8d75f94d9671038db36', \
               ['6d4aaa42d465966f13e3609b0c58ec40', 'e8eadb78f33cddaad991ad80b8c4c213', \
                'cc944af5713dda9742e98b119862e59d', 'be2457eff37229182e77a906d6d542cd', \
                '35879aa889b45af13405b844c5fd8299'], \
               ['4d37183961d5b5', '37ba5b70848ee4', '03ba4a3904e1ec', '9a2c46340662f6', 'eaa354bb904a0a'], \
               ['5996accc4650f2', 'a449736589974c', 'bab9aa88ace13c', '74a190d529fc1f', '4699de381ae778'], \
               ['d4d8e88d0217ebb7e288375b17c0f7e9', 'fd3b6a5c674748d3012188a9aa799a61', \
                'bf36ebcc70630ec17bf83038685b893f', 'ccbaf1e2ed45e54952991be3b68ce36d', \
                'f845caa440243d39ae446be934683db3']] # 774 Wrong Plaintext
  ################################################################################
  INPUTS[4] = [ 'dcabde2621c5a8d75f94d9671038db36', \
               ['6d4aaa42d465966f13e3609b0c58ec40', 'e8eadb78f33cddaad991ad80b8c4c213', \
                'cc944af5713dda9742e98b119862e59d', 'be2457eff37229182e77a906d6d542cd', \
                '35879aa889b45af13405b844c5fd8299'], \
               ['4d37183961d5b5', '37ba5b70848ee4', '03ba4a39c4e1ec', '9a2c46340662f6', 'eaa354bb904a0a'], \
               ['5996accc4650f2', 'a449736589974c', 'bab9aa88ace13c', '74a190d529fc1f', '4699de381ae778'], \
               ['d4d8e88d0217ebb7e288375b17c0f7e9', 'fd3b6a5c674748d3012188a9aa799a61', \
                'bf36ebcc70630ec17bf83038685b893f', 'ccbaf1e7ed45e54952991be3b68ce36d', \
                'f845caa440243d39ae446be934683db3']] # 774 Wrong Tag
  ################################################################################
  for t in range(0, len(INPUTS)):
    if INPUTS[t]=="":
      continue
    print("======================================================================")
    print("Test #"+str(t).zfill(2))
    print(testing(5, INPUTS[t][0], INPUTS[t][1], INPUTS[t][2], INPUTS[t][3], INPUTS[t][4]))


