# python3
import numpy as np
import csv
import matplotlib.pyplot as plt
import time
import readFile
class Util :
    def __init__(self):
        pass

    #计算X,Y的回归参数w,b
    @staticmethod
    def regression(X,Y):
        '''
        m=len(X)
        x=np.matrix(X)
        y=np.matrix(Y)
        dimension=len(X[0])
        w = (x.T * x).I * x.T * y
        sum = np.mat(np.zeros((1,dimension)))
        for i in range(0,m):
            sum += (y[i] - w * x[i])
        b = sum / m
        '''
        m = len(X)
        #如果数据太少，直接预测为0
        if m<10:
            return [[0]],[[0]]
        xavg=a=b=0
        for i in range(m):
            xavg+=X[i][0]
        xavg=xavg/m
        for i in range(m):
            a+=Y[i][0]*(X[i][0]-xavg)
            b+=X[i][0]**2
        w=a/(b-(xavg*m)**2/m)
        c=0
        for i in range(m):
           c+=Y[i][0]-w*X[i][0]
        b=c/m
        w=[[w]]
        b=[[b]]
        return w,b

    #四舍五入取整
    @staticmethod
    def rounding(x):
        if (int(x*10))%10<5:
            return int(x)
        else:
            return int(x)+1

    #获取某一个文件的新版本序号
    @staticmethod
    def getNewVersion(fileName):
        try:
            with open('../dataset/version.csv') as f:
                reader = csv.reader(f, delimiter=',')
                data=[row for row in reader]
        except csv.Error as e:
            print("file open error.")
        get=False
        for line in data:
            if line[0]==fileName:
                v=line[1]=int(line[1])+1
                get=True
                break;
        if not get:
            v=1
            data.append([fileName,v])
        try:
            with open('../dataset/version.csv', 'w', newline='') as f:
                writer=csv.writer(f,dialect='excel')
                for line in data:
                    writer.writerow(line)
        except csv.Error as e:
            print("file open error.")
        return v
    #获取某一文件的当前版本号
    @staticmethod
    def getCurVersion(fileName):
        v=0
        try:
            with open('../dataset/version.csv') as f:
                reader = csv.reader(f, delimiter=',')
                data=[row for row in reader]
        except csv.Error as e:
            print("file open error.")
        for line in data:
            if line[0]==fileName:
                v=int(line[1])
                break;
        return v

    @staticmethod
    def printRegressionDiagram(sku,x,y,w,b):
        X = []
        Y = []
        for i in range(len(x)):
            X.append(x[i][0])
            Y.append(y[i][0])
        x1=[i for i in range(min(X),max(X))]
        y1=[w*i+b for i in range(min(X),max(X))]
        plt.scatter(X,Y)
        plt.plot(x1,y1)
        plt.title(sku)
        plt.show()



    @staticmethod
    def denoising(x,y,w,b):
        xnew=[]
        ynew=[]
        canchabiaozhuncha=0
        canchajunzhi=0
        for i in range(len(x)):
            canchajunzhi+=y[i][0]-w*x[i][0]-b
            canchabiaozhuncha+=(y[i][0]-w*x[i][0]-b)**2
        canchajunzhi/=len(x)
        canchabiaozhuncha=(canchabiaozhuncha/len(x))**0.5
        if canchabiaozhuncha==0:
            return x,y,[[w]],[[b]]
        for i in range(len(x)):
            bianzhunhuacancha=(y[i][0]-w*x[i][0]-b-canchajunzhi)/canchabiaozhuncha
            if bianzhunhuacancha<1.5 and bianzhunhuacancha>-1.5:
                xnew.append(x[i])
                ynew.append(y[i])
        wnew,bnew=Util.regression(xnew,ynew)
        return xnew,ynew,wnew,bnew
    @staticmethod
    def timeToDay(time):
        return int(time/(60*60*24))

    @staticmethod
    def dateToday(date):
        return int(time.mktime(time.strptime(date, "%Y%m%d"))/(60*60*24))

    @staticmethod
    #result是一个字典，key是sku_id,value是预测的5个星期销量的数组
    def writeResult(result):
        sortSKU = readFile.ReadFile.getSortedSku()
        try:
            with open('../dataset/result/result_v' + str(Util.getNewVersion('result')) + '.csv', 'w', newline='') as f:
                writer = csv.writer(f, dialect='excel')
                writer.writerow(['sku_id', 'week1', 'week2', 'week3', 'week4', 'week5'])
                for sku in sortSKU:
                    writer.writerow(
                        [sku, result[sku][0], result[sku][1], result[sku][2], result[sku][3], result[sku][4]])
        except csv.Error as e:
            print("file open error.")
