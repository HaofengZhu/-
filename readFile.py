# python3
import time
import csv

class ReadFile():

    def __init__(self):
        pass

    # data_date,goods_id,shop_price,promote_price,promote_start_time,promote_end_time
    @staticmethod
    def read_goods_promote_price():
        data = []
        try:
            with open('../dataset/goods_promote_price.csv') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    temp = []
                    temp.append(time.mktime(time.strptime(row[0], "%Y%m%d")))
                    temp.append(row[1])
                    temp.append(float(row[2]))
                    temp.append(float(row[3]))
                    temp.append(time.mktime(time.strptime(row[4], "%Y-%m-%d %H:%M:%S")))
                    temp.append(time.mktime(time.strptime(row[5], "%Y-%m-%d %H:%M:%S")))
                    data.append(temp)
        except csv.Error as e:
            print("file open error.")
        return data

    # sku_id,goods_id
    @staticmethod
    def read_goods_sku_relation():
        data = []
        try:
            with open('../dataset/goods_sku_relation.csv') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    temp = []
                    temp.append(row[0])
                    temp.append(row[1])
                    data.append(temp)
        except csv.Error as e:
            print("file open error.")
        return data

    # data_date,goods_id,sku_id,goods_num,goods_price,orginal_shop_price
    @staticmethod
    def read_goodsale():
        data = []
        try:
            with open('../dataset/goodsaleSortAndCancel.csv') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    temp = []
                    temp.append(time.mktime(time.strptime(row[0], "%Y%m%d")))
                    temp.append(row[1])
                    temp.append(row[2])
                    temp.append(int(row[3]))
                    temp.append(float(row[4]))
                    temp.append(float(row[5]))
                    data.append(temp)
        except csv.Error as e:
            print("file open error.")
        return data

    #data_date, goods_id, goods_click, cart_click, favorites_click, sales_uv, onsale_days
    @staticmethod
    def read_goodsdaily():
        data = []
        try:
            with open('../dataset/goodsdaily.csv') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    temp = []
                    temp.append(time.mktime(time.strptime(row[0], "%Y%m%d")))
                    temp.append(row[1])
                    temp.append(int(row[2]))
                    temp.append(int(row[3]))
                    temp.append(int(row[4]))
                    temp.append(int(row[5]))
                    temp.append(int(row[6]))
                    data.append(temp)
        except csv.Error as e:
            print("file open error.")
        return data

    #goods_id,cat_level1_id,cat_level2_id,cat_level3_id,cat_level4_id,cat_level5_id,cat_level6_id,cat_level7_id,goods_season,brand_id
    @staticmethod
    def read_goodsinfo():
        data = []
        try:
            with open('../dataset/goodsinfo.csv') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    temp = []
                    temp.append(row[0])
                    temp.append(int(row[1]))
                    temp.append(int(row[2]))
                    temp.append(int(row[3]))
                    temp.append(int(row[4]))
                    temp.append(int(row[5]))
                    temp.append(int(row[6]))
                    temp.append(int(row[7]))
                    temp.append(int(row[8]))
                    data.append(temp)
        except csv.Error as e:
            print("file open error.")
        return data

    #data_date,marketing,plan
    @staticmethod
    def read_marketing():
        data = []
        try:
            with open('../dataset/marketing.csv') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    temp = []
                    temp.append(time.mktime(time.strptime(row[0], "%Y%m%d")))
                    temp.append(int(row[1]))
                    temp.append(int(row[2]))
                    data.append(temp)
        except csv.Error as e:
            print("file open error.")
        return data

    @staticmethod
    def getSortedSku():
        sortSKU = []
        try:
            with open('../dataset/submit_example.csv') as f:
                reader = csv.reader(f, delimiter=',')
                rows = [row for row in reader]
        except csv.Error as e:
            print("file open error.")

        for row in rows[1:]:
            sortSKU.append(row[0])
        return sortSKU
