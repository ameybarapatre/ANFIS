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

#data['mean'] = data['fare_rate'].mean()

#data[['fare_rate_e','fare_rate' ,'reward','mean']].plot()
#plt.show()


data['ua'] = 1 /(1 + 2.7**(-0.5*((data['active_time'] -data['active_time'].mean())/(data['active_time'].std()))))

data['uc'] = 1 /(1 + 2.7**(-0.5*((data['waiting_time'] -data['waiting_time'].mean())/(data['waiting_time'].std()))))

data['ub'] = 1 /(1 + 2.7**(-0.5*((data['total_fare'] -data['total_fare'].mean())/(data['total_fare'].std()))))

data['ud'] = 1 /(1 + 2.7**(-0.5*((data['fare'] -data['fare'].mean())/(data['fare'].std()))))

data[['ua','ub','uc','ud','reward']].plot()

data[['ua','ub','uc','ud','reward']].to_csv("fuzzyq.csv")
plt.show()



