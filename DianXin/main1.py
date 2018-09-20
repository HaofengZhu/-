from DianXin import readFile
from DianXin import C4_5
import time
from sklearn import tree
from sklearn import ensemble
from comment import util
import csv
import graphviz

begin_time=time.time()
#读取数据
data,label=readFile.readTrainData()
#data=data[:1000]
for line in data:
    del line[-1]
y=[]
for line in data:
    y.append(line[-1])
for line in data:
    del line[-1]

testData,_=readFile.readTestData()
userID=[]
for line in testData:
    userID.append(line[-1])
    del line[-1]
print("读取数据完毕")

allData=data[:]
allData.extend(testData)
largest={}
for col in range(len(allData[0])):
    if(type(allData[0][col]).__name__=='str'):
        continue
    temp=allData[0][col];
    for row in range(len(allData)):
        if allData[row][col]>temp:
            temp=allData[row][col]
    largest[col]=temp

for k in largest:
    largest[k]=largest[k]**2

#计算距离
result={}
tData=testData[:int(len(testData)/2)]
begin_time=time.time()
for i in range(len(testData)):
    smallestDistance=100;
    smallestIndex=0;
    for j in range(len(data)):
        tempDistance=0
        for k in range(len(data[0])):
            if type(data[j][k]).__name__=='str':
                if data[j][k]!=testData[i][k]:
                    tempDistance+=1
            else:
                tempDistance+=((data[j][k]-testData[i][k])**2)/largest[k]
        if tempDistance<smallestDistance:
            smallestDistance=tempDistance
            smallestIndex=j
    result[userID[i]]=y[smallestIndex]
    print(userID[i]+":"+y[smallestIndex])
    end_time = time.time()
    util.Util.printTimeUsed(begin_time, end_time)

try:
    with open('../../DianXin/result/result_v' + str(util.Util.getNewVersion('DianXinresult')) + '.csv', 'w',
              newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['user_id', 'predict'])
        for k in result:
            writer.writerow([k,result[k]])
except csv.Error as e:
    print("file open error.")
