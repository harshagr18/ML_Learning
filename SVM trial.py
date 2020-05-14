import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import pandas as pd
model=SVC()

df = pd.read_excel('C:/Users/subhashis sengupta/Desktop/ML/Dataset.xlsx')

#print(df)
#df=df.iloc[1:,:]
#print(df)
x=df.iloc[:,1:4]
print(x)
y=np.array([df.iloc[:,4:5]])
print(y)
model.fit(x,y)
#Training