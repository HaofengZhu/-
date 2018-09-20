import readFile
import util
import csv
from collections import defaultdict

data = defaultdict(list)
try:
    with open('../dianxin/train.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data[row[25]].append(row)
except csv.Error as e:
    print("file open error.")
for key in data[1:]:
    try:
        with open('../dianxin/result/' + str(key) + '.csv', 'w', newline='') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(['service_type','is_mix_service','online_time','1_total_fee','2_total_fee','3_total_fee','4_total_fee','month_traffic','many_over_bill','contract_type','contract_time','is_promise_low_consume','net_service','pay_times','pay_num','last_month_traffic','local_trafffic_month','local_caller_time','service1_caller_time','service2_caller_time','gender','age','complaint_level','former_complaint_num','former_complaint_fee','current_service','user_id'])
            for index, item in enumerate(data[key]):
                writer.writerow(item)
    except csv.Error as e:
        print("file open error.")