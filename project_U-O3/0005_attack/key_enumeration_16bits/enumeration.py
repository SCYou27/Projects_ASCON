import numpy as np
import sys
import time
import heapq

#Dummy = np.array([-1.0, -float('inf')])

class Terminal:
  def __init__(self, Table):
    Table = np.hstack([-Table[0][:,1:2], Table[0][:,0:1]])
    self.RankTable = Table[Table[:,0].argsort()]
    self.position = 0
    self.max_size = len(self.RankTable)+1
    self.dummy = [float('inf'), np.array([-1])]
    return
  
  def Next_one(self):
    if self.position==(self.max_size-1):
      return self.dummy
    Element = []
    Element.append(self.RankTable[self.position][0])
    Element.append(np.array([int(self.RankTable[self.position][1])]))
    self.position += 1
    return Element

class Node:
  def __init__(self, Table):
    self.position = 0
    Mid = (len(Table)//2)
    if len(Table[:Mid])==1:
      self.LChild = Terminal(Table[:Mid])
    else:
      self.LChild = Node(Table[:Mid])
    if len(Table[Mid:])==1:
      self.RChild = Terminal(Table[Mid:])
    else:
      self.RChild = Node(Table[Mid:])
    self.max_size = (self.LChild.max_size-1)*(self.RChild.max_size-1)+1
    temp_list = np.hstack([self.LChild.dummy[1], self.RChild.dummy[1]])
    self.dummy = [float('inf')]
    self.dummy.append(temp_list)
    self.Fronts = []
    self.LTable = []
    self.RTable = []
    self.LTable.append(self.LChild.Next_one())
    self.RTable.append(self.RChild.Next_one())
    Prob = self.LTable[0][0]+self.RTable[0][0]
    Indeces = (0,0)
    Bytes = np.hstack([self.LTable[0][1], self.RTable[0][1]])
    Element = []
    Element.append(Prob)
    Element.append(Indeces)
    Element.append(Bytes)
    heapq.heappush(self.Fronts, (Prob, Indeces, Bytes))
    self.Front_ID_L = [True]
    self.Front_ID_R = [True]
    return
  
  def Next_one(self):
    if self.position == (self.max_size-1):
      return self.dummy
    (Next_Prob, (Next_L, Next_R), Next_Bytes) = heapq.heappop(self.Fronts)
    Output = []
    Output.append(Next_Prob)
    Output.append(Next_Bytes)
    self.Front_ID_L[Next_L] = False
    self.Front_ID_R[Next_R] = False
    #==============Table Expanation=================
    if Next_R==0:
      self.LTable.append(self.LChild.Next_one())
      self.Front_ID_L.append(False)
    if Next_L==0:
      self.RTable.append(self.RChild.Next_one())
      self.Front_ID_R.append(False)
    #===============================================
    if (self.Front_ID_L[(Next_L+1)]==False)and(self.Front_ID_R[(Next_R)]==False):
      Prob = self.LTable[Next_L+1][0]+self.RTable[Next_R][0]
      Bytes = np.hstack([self.LTable[Next_L+1][1], self.RTable[Next_R][1]])
      heapq.heappush(self.Fronts, (Prob, (Next_L+1, Next_R), Bytes))
      self.Front_ID_L[Next_L+1] = True
      self.Front_ID_R[Next_R] = True
    if (self.Front_ID_L[(Next_L)]==False)and(self.Front_ID_R[(Next_R+1)]==False):
      Prob = self.LTable[Next_L][0]+self.RTable[Next_R+1][0]
      Bytes = np.hstack([self.LTable[Next_L][1], self.RTable[Next_R+1][1]])
      heapq.heappush(self.Fronts, (Prob, (Next_L, Next_R+1), Bytes))
      self.Front_ID_L[Next_L] = True
      self.Front_ID_R[Next_R+1] = True
    return Output


class Enumerator:
  def __init__(self, GreatTable):
    self.count = 0
    self.INnode = Node(GreatTable) 
    return
  
  def Next_one(self):
    Element = self.INnode.Next_one()
    self.count+=1
    return Element[1], Element[0]
  
