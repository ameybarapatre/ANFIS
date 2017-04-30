import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv("dataset.csv")

data['time'] = (data['time_fare'] + data['waiting_time'])

data['expected_fare'] = data['fare']

data['total_fare_e'] = data['total_fare'] + data['expected_fare']

data['fare_rate_e'] =  (data['total_fare_e'])/(data['active_time']+data['time'])

data['fare_rate']  = data['total_fare']/data['active_time']

print(data['fare_rate'].mean())

data['reward'] =abs(data['fare_rate'] - data['fare_rate'].mean())- abs(data['fare_rate_e'] - data['fare_rate'].mean())

data['error0'] = data['fare_rate'] - data['fare_rate'].mean()

data['error1'] = data['fare_rate_e'] - data['fare_rate'].mean()



data ['PID1'] =  0.1*data['error1']  + ((data['error1']-data['error0'])/data['time'])*100 +0.1* (data['error1']*data['time'] + 0.1*data['error0']*data['active_time'])

data['PID0'] = 0.1*data['error0'] + (data['error0']/data['active_time'])*100 + data['error0']*data['active_time']*0.1

data['mean'] = data['fare_rate'].mean()

data['Diff'] =  abs(data['PID0']) - abs(data['PID1'])

data['reward'] =data['reward']*10

data[['reward','Diff']].plot()

plt.show()
# active_time_high
data['ua'] = 1 /(1 + 2.7**(-1*((data['active_time'] -data['active_time'].mean())/(data['active_time'].std()))))
# waiting _time_ low
data['uc'] = 1 /(1 + 2.7**(1*((data['waiting_time'] -data['waiting_time'].mean())/(data['waiting_time'].std()))))
#total_fare_low
data['ub'] = 1 /(1 + 2.7**(1*((data['total_fare'] -data['total_fare'].mean())/(data['total_fare'].std()))))
#fare_high
data['ud'] = 1 /(1 + 2.7**(-1*((data['fare'] -data['fare'].mean())/(data['fare'].std()))))
data[['ua','ub','uc','ud','reward']].plot()

data[['ua','ub','uc','ud','Diff']].to_csv("fuzzyq1.csv")



