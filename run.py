import anfis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("fuzzyq.csv")
taxis = data[["ua","ub","uc","ud"]].as_matrix()
E = anfis.taxi_eligibility(taxis , alpha= 3 ,Gamma = 0.3)
print(E.max())
data['Q'] = E.ravel()
data['reward'] =data['reward']*10
data[['reward' ,'Q']].plot()
plt.show()


