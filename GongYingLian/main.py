from GongYingLian import readFile
from comment import util
import time
import numpy as np
from collections import defaultdict
import csv

data = readFile.ReadFile.read_goodsale()
result_data = defaultdict(list)
try:
    with open('../../GongYingLian/result/result_v26_test.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            result_data[row[0]].append(int(row[1]))
            result_data[row[0]].append(int(row[2]))
            result_data[row[0]].append(int(row[3]))
            result_data[row[0]].append(int(row[4]))
            result_data[row[0]].append(int(row[5]))
except csv.Error as e:
    print("file open error.")
# first_day= '20170228'
# last_day= '20180316'
# days_to_train=last_day-first_day+1
print("导入数据完毕")
begin_time=time.time()
last_week_begin= '20180306'
last_week_end= '20180312'
sku=""
sku_num={}
# smallest_date = '20180313'
for index in range(len(data)):
    #开始的特殊情况
    if sku=="":
        sku=data[index][2]
        y=0
    #一种商品扫描结束
    if sku!=data[index][2] or index==len(data)-1:
        if result_data[sku][0] > 10:
            for i in range(len(result_data[sku])):
                result_data[sku][i] = y
        #初始化
        sku = data[index][2]
        y=0
    if result_data[sku][0] > 10:
        #正在扫描一种商品
        day = data[index][0]
        if day>=last_week_begin and day<=last_week_end:
            y+=data[index][3]
print("计算输出完毕")

result={}
sortSKU = readFile.ReadFile.getSortedSku()
for sku in sortSKU:
    result[sku]=[result_data[sku][0] for i in range(5)]

print(result)

readFile.ReadFile.writeResult(result)
print("输出写入完毕")

end_time=time.time()
util.Util.printTimeUsed(begin_time,end_time)