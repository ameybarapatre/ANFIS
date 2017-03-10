import itertools
import csv
time_fare = [60,60,60,60]
waiting_time = [10,30,60,90]
active_time = [60,120,240,360]
total_fare = [6,12,24,36]
fare = [3,6,9,12]

dataset = open("dataset.csv","w")
wr = csv.writer(dataset ,quoting=csv.QUOTE_ALL)
wr.writerows(list(itertools.product(waiting_time,active_time,total_fare,fare ,time_fare)))
