# 初始化读取excel数据
import xlrd
from datetime import date,datetime
from Sickman import Sickman

def read_excel_init(file, name,startlist, endlist):
   wb = xlrd.open_workbook(filename=file)
   sheet = wb.sheet_by_index(0)  #获得索引表格
   #    rows = sheet1.row_values(2)#获取行内容
   #    cols = sheet1.col_values(3)#获取列内容
   names = sheet.col_values(1) #病名称 
   del(names[0])  #删除列名称
   # for i in name :
   #    print(i)
   n_rows = sheet.nrows
   print(n_rows)
   for i in range(1,n_rows):
      x=xlrd.xldate_as_datetime(sheet.cell(i,2).value,0)  
      startlist.append(x) #就诊时间
   # for i in startlist:
   #    print(i)
   for i in range(1,n_rows):
      x=xlrd.xldate_as_datetime(sheet.cell(i,6).value,0)
      endlist.append(x)  #出院时间
   # print('endlist')
   # for i in endlist:
   #    print(i)

def read_excel_to_bind(file):
   manlist=[]
   wb = xlrd.open_workbook(filename=file)
   sheet = wb.sheet_by_index(0)  #获得索引表格
   n_rows = sheet.nrows
   indexs = sheet.col_values(0)  #获得number
   del(indexs[0])
   names = sheet.col_values(1)   #获得病名
   del(names[0])
   startlist = []
   for i in range(1,n_rows):     #就诊时间院时间
      x=xlrd.xldate_as_datetime(sheet.cell(i,2).value,0)  
      startlist.append(x) 
   # 造一个病人list 存这些数据到内存里面
   for i in range(0,n_rows-1):
      x = Sickman(indexs[i],names[i],startlist[i])
      manlist.append(x)
   # print(str(manlist[0].getNum())+
   # str(manlist[0].getName())+
   # str(manlist[0].getStarttime())+
   # str(manlist[1].getNum())+
   # str(manlist[1].getName())+
   #  str(manlist[1].getStarttime()))
   return manlist
   
if __name__ == "__main__":
   file = 'init.xlsx'
   manlist = read_excel_to_bind(file)



 