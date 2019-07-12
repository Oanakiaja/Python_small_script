#主程序
import xlrd
from datetime import date,datetime,timedelta
import queue
from init import read_excel_to_bind 
from Sickbed import Sickbed
from Sickman import Sickman
import openpyxl
# 产生79病床 dict dict号对应一个病床
# 病床队列  空闲病床队列 、 优先队列病床 ： 每次空闲病床出队给优先队列病床（按照时间优先，如果出队 更新EXCEL表格，产生出院日期记录）
# 病人队列  门诊后排队队列
# 进入队列按照高响应比调度算法-绑定病床

file = 'init.xlsx'
workbook = openpyxl.load_workbook(file)

currenttime = datetime(2008,7,14)

freeBeds = queue.Queue(maxsize = 79)
occpyBeds = queue.PriorityQueue(maxsize = 79)
waitMans = queue.PriorityQueue()
n_freeBeds = 79 # 空床位
manlist =read_excel_to_bind(file) # 存了所有的人的数据
#用日期对应dict索引，每dict表示每一天
everydayman = dict()
for man in manlist:
   if man.getStarttime() in everydayman.keys():
      everydayman[man.getStarttime()].append(man) 
   else:
      everydayman[man.getStarttime()] = []
      everydayman[man.getStarttime()].append(man)

for i in range(0,79): #造79个空闲病房
   x = Sickbed()
   freeBeds.put(x)

for date in everydayman.keys(): #日期为键，作为每一天
   currentlist = everydayman[date]
   tempqueue = queue.Queue()
   
   #释放今天病房空了的
   while not occpyBeds.empty():
      x = occpyBeds.get()
      if(x.IsUse()):
         x.Update()
         tempqueue.put(x)#发现第一个非空得就放进去，每个病房都更新一下left天数
      else:
         freeBeds.put(x)
   while not tempqueue.empty():
      occpyBeds.put(tempqueue.get()) #把放出去的收回来
   
   #加入病人门诊后的队列，按优先级排序，先计算优先级
   
   for i in currentlist:
      i.update_priority(currenttime) # 计算优先级
   for i in currentlist:
      waitMans.put(i)    #按照优先级丢到排队队列
   
   #通过病人优先级队列，看是否有空床位，空床位给病人绑定，绑定后的床位加入到occupiedBeds中

   while not freeBeds.empty(): # 有新床位
      if not waitMans.empty():  #有病人
         man = waitMans.get()
         man.Update(currenttime,workbook,file)
         bed = freeBeds.get() #取得空床
         bed.Bind(man)
         occpyBeds.put(bed)  #放入占用床位
      else:
         break
   #这一天结束，加一天
   currenttime +=timedelta(days=1)