import anfis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
output =  pd.read_csv('dataset.csv')
data = pd.read_csv("fuzzyq.csv")
taxis = data[["ua","ub","uc","ud"]].as_matrix()
taxis_y = data[["ub","ud"]].as_matrix()
E = anfis.taxi_eligibility(taxis ,taxis_y=taxis_y ,alpha= 0.1 ,Gamma = 0.7)
print(E.max())
data['Q'] = E.ravel()
data['Diff'] = data['Diff']*15
output['Q'] =  E.ravel()
output = output.sort(columns=['Q'] , ascending=False)
print(output)
output.to_csv('output.csv')
data[['Diff' ,'Q']].plot()
plt.show()


