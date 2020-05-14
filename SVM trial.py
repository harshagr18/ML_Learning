import numpy as np
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
df = pd.read_excel('Dataset.xlsx')
x=df.iloc[:,1:4]
y=df.iloc[:,4:5]
print(x)
print(y)
model=SVC()
model.fit(x,y)
model.predict(x)
print(int(accuracy_score(model.predict(x),y)*100),"%")