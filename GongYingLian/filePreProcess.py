# python3
import csv

#把商品按商品sku_id排序
try:
    with open('../../GongYingLian/goodsale.csv') as f:
        reader = csv.reader(f, delimiter=',')
        data=[row for row in reader]
except csv.Error as e:
    print("file open error.")
#data.sort(key=lambda x:x[2])
#按时间戳排序
NewData=[]
sku=""
for index in range(len(data)):
    #开始的特殊情况
    if sku=="":
        sku=data[index][2]
        ASkuData = []
    #一种商品扫描结束
    if sku!=data[index][2] or index==len(data)-1:
        ASkuData.sort(key=lambda x:x[0])
        for line in ASkuData:
            NewData.append(line)
        #初始化,进入下一个商品
        sku = data[index][2]
        ASkuData = []
    #正在扫描一种商品
    ASkuData.append(data[index])

data=NewData
#将不需要预测的商品删除
sortSKU=[]
try:
    with open('../../GongYingLian/submit_example.csv') as f:
        reader = csv.reader(f, delimiter=',')
        skus=[row for row in reader]
except csv.Error as e:
    print("file open error.")
for row in skus[1:]:
    sortSKU.append(row[0])

sku=''
iswrite=False
try:
    with open('../../GongYingLian/goodsaleSort.csv','w',newline="") as f:
        writer = csv.writer(f, dialect=('excel'))
        for line in data:
            if line[2]!=sku:
                if line[2] in sortSKU:
                    iswrite=True
                else:
                    iswrite=False
                sku=line[2]
            if iswrite:
                writer.writerow(line)
except csv.Error as e:
    print("file open error.")
