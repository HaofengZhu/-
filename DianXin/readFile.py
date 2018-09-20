import csv
from comment import util

def readTrainData():
    try:
        with open('../../DianXin/train/train.csv') as f:
            reader = csv.reader(f, delimiter=',')
            data=[line for line in reader]
    except csv.Error as e:
        print("file open error.")
    label=data[0]
    data=data[1:]
    for line in data:
        # if line[1]=='1':
        #     line[1]=True
        # else:
        #     line[1]=False
        line[2]=int(line[2])
        line[3]=float(line[3])
        line[4] = float(line[4])
        line[5] = float(line[5])
        line[6] = float(line[6])
        line[7] = float(line[7])
        # if line[8]=='1':
        #     line[8]=True
        # else:
        #     line[8]=False
        line[10]=int(line[10])
        # if line[11]=='1':
        #     line[11]=True
        # else:
        #     line[11]=False
        line[13]=int(line[13])
        line[14]=float(line[14])
        line[15] = float(line[15])
        line[16] = float(line[16])
        line[17] = float(line[17])
        line[18] = float(line[18])
        line[19] = float(line[19])
        line[21]=int(line[21])
        line[23] = int(line[23])
        line[24] = float(line[24])
    return data,label

def readTestData():
    try:
        with open('../../DianXin/test/test.csv') as f:
            reader = csv.reader(f, delimiter=',')
            data=[line for line in reader]
    except csv.Error as e:
        print("file open error.")
    label = data[0]
    data=data[1:]
    for line in data:
        # if line[1]=='1':
        #     line[1]=True
        # else:
        #     line[1]=False
        line[2]=int(line[2])
        line[3]=float(line[3])
        line[4] = float(line[4])
        line[5] = float(line[5])
        line[6] = float(line[6])
        line[7] = float(line[7])
        # if line[8]=='1':
        #     line[8]=True
        # else:
        #     line[8]=False
        line[10]=int(line[10])
        # if line[11]=='1':
        #     line[11]=True
        # else:
        #     line[11]=False
        line[13]=int(line[13])
        line[14]=float(line[14])
        line[15] = float(line[15])
        line[16] = float(line[16])
        line[17] = float(line[17])
        line[18] = float(line[18])
        line[19] = float(line[19])
        line[21]=int(line[21])
        line[23] = int(line[23])
        line[24] = float(line[24])
    return data,label

def writeResult(result):
    try:
        with open('../../DianXin/result/result_v' + str(util.Util.getNewVersion('DianXinresult')) + '.csv', 'w', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(['user_id', 'predict'])
            for id in result:
                writer.writerow([id,result[id]])
    except csv.Error as e:
        print("file open error.")