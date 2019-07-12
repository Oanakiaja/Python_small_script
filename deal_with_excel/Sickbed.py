#病床类
from datetime import datetime ,date 
import Sickman
import queue

# workingmatrix=[[ 7, 7, 7, 7, 7, 7, 7],  # 第二问矩阵
#                [13,12,12,12,12,13,12],
#                [11,10,10,10,10,11,10],
#                [12,11,10, 9, 8, 6, 5],
#                [ 5, 4, 8, 7, 6, 5, 4]]

workingmatrix=[[ 7, 7, 7, 7, 9, 8, 7],  # 第四问矩阵
               [13,12,12,15,14,13,12],
               [11,10,10,13,12,11,10],
               [12,11,10, 9, 8, 6, 5],
               [ 5, 4, 8, 7, 6, 5, 4]]
names = {
  "外伤" : 0,
  "视网膜疾病" : 1,
  "青光眼" : 2,
  "白内障(双眼)" : 3, 
  "白内障" : 4
}

class Sickbed:
   def __init__(self):
      self.use = False 
      self.left = 0
      
   def __lt__(self, other):
      return self.left < other.left

   # 人每次进去bind一下病床
   def Bind(self,sickman):
      if(self.use!=0):
         self.sickman = sickman
         self.use = True

   def IsUse(self):
      return self.use

   def SetUse(self, use):
      self.use = use 

   # 每天一轮回搞一搞
   def Update(self):
      if(self.use):
         self.left -= 1 #剩余天数少一天
         if(self.left==0):
            self.use = False

   def setLeft(self,left):
      self.left = left
   def getLeft(self):
      return self.left

if __name__ =="__main__" :
   q = queue.PriorityQueue()
   a = Sickbed()
   a.setLeft(1)
   b = Sickbed()
   b.setLeft(4)
   c =Sickbed()
   c.setLeft(2)
   q.put(c)
   q.put(a)
   q.put(b)
   while not q.empty():
      print(q.get().getLeft())
