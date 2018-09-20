from GongYingLian import readFile
from comment import util
import time
data = readFile.ReadFile.read_goodsale()
first_day= util.Util.dateToday('20170228')
last_day= util.Util.dateToday('20180316')
days_to_train=last_day-first_day+1
print("导入数据完毕")
begin_time=time.time()
last_week_begin= util.Util.dateToday('20180123')
last_week_end= util.Util.dateToday('20180312')
sku=""
sku_num={}
for index in range(len(data)):
    #开始的特殊情况
    if sku=="":
        sku=data[index][2]
        y=0
    #一种商品扫描结束
    if sku!=data[index][2] or index==len(data)-1:
        sku_num[sku]=util.Util.rounding(y/7)
        #初始化
        sku = data[index][2]
        y=0
    #正在扫描一种商品
    day= util.Util.timeToDay(data[index][0])
    if day>=last_week_begin and day<=last_week_end:
        y+=data[index][3]
print("计算输出完毕")

result={}
sortSKU = readFile.ReadFile.getSortedSku()
for sku in sortSKU:
    result[sku]=[sku_num[sku] for i in range(5)]

readFile.ReadFile.writeResult(result)
print("输出写入完毕")

end_time=time.time()
util.Util.printTimeUsed(begin_time,end_time)