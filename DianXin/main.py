from DianXin import readFile
from DianXin import C4_5
import time
from sklearn import tree
from comment import util
import csv
import graphviz

begin_time=time.time()
#读取数据
data,label=readFile.readTrainData()
#data=data[:1000]
for line in data:
    del line[-1]
target=[]
for line in data:
    target.append(line[-1])
for line in data:
    del line[-1]

tData,_=readFile.readTestData()
userID=[]
for line in tData:
    userID.append(line[-1])
    del line[-1]

usedFeature=[2,3,4,5,6,7,11,12,15,16,17,18,19,20,21,22,23,24]
trainData=[]
testData=[]
for line in data:
    temp=[]
    for i in usedFeature:
        temp.append(line[i])
    trainData.append(temp)
for line in tData:
    temp=[]
    for i in usedFeature:
        temp.append(line[i])
    testData.append(temp)
print("读取数据完毕")

clf = tree.DecisionTreeClassifier()
clf = clf.fit(trainData, y)
result=clf.predict(testData)
try:
    with open('../../DianXin/result/result_v' + str(util.Util.getNewVersion('DianXinresult')) + '.csv', 'w',
              newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['user_id', 'predict'])
        for index in range(len(result)):
            writer.writerow([userID[index],result[index]])
except csv.Error as e:
    print("file open error.")

tree.export_graphviz(clf,
    out_file='tree.dot')
end_time=time.time()
util.Util.printTimeUsed(begin_time,end_time)
