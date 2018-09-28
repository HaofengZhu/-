from DianXin import readFile
import time
from sklearn import ensemble
from comment import util
import csv
from sklearn.kernel_ridge import KernelRidge
# import graphviz

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

print("读取数据完毕")

clf = KernelRidge(alpha=1.0)
clf.fit(data, target)
result=clf.predict(tData)
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(trainData, y)
# result=clf.predict(testData)
try:
    with open('../../DianXin/result/result_v' + str(util.Util.getNewVersion('DianXinresult')) + '.csv', 'w',
              newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerow(['user_id', 'predict'])
        for index in range(len(result)):
            writer.writerow([userID[index],result[index]])

except csv.Error as e:
    print("file open error.")
#
# tree.export_graphviz(clf,
#     out_file='tree.dot')
end_time=time.time()
util.Util.printTimeUsed(begin_time,end_time)
