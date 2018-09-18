import readFile
import util
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
try:
    with open('../dataset/coefficient_v'+str(util.Util.getNewVersion('coefficient'))+'.csv','w',newline='') as f:
        pass
except csv.Error as e:
    print("file open error.")

data = readFile.ReadFile.read_goodsale()
first_day=util.Util.dateToday('20170228')
last_day=util.Util.dateToday('20180316')
days_to_train=last_day-first_day+1
print("导入数据完毕")

last_week_begin=util.Util.dateToday('20180305')
last_week_end=util.Util.dateToday('20180311')
sku=""
sku_num={}
for index in range(len(data)):
    #开始的特殊情况
    if sku=="":
        sku=data[index][2]
        y=0
    #一种商品扫描结束
    if sku!=data[index][2] or index==len(data)-1:
        sku_num[sku]=y
        #初始化
        sku = data[index][2]
        y=0
    #正在扫描一种商品
    day=util.Util.timeToDay(data[index][0])
    if day>=last_week_begin and day<=last_week_end:
        y+=data[index][3]
print("计算输出完毕")
"""
result={}
sortSKU = readFile.ReadFile.getSortedSku()
for sku in sortSKU:
    result[sku]=[sku_num[sku] for i in range(5)]

util.Util.writeResult(result)
print("输出写入完毕")
"""