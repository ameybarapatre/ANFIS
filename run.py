import anfis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("fuzzyq.csv")
taxis = data[["ua","ub","uc","ud"]].as_matrix()
E = anfis.taxi_eligibility(taxis , alpha= 0.1 ,Gamma = 0.7)
print(E.max())
data['Q'] = E.ravel()
data['Diff'] =data['Diff']*15
data[['Diff' ,'Q']].plot()
plt.show()


