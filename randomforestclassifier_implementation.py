from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/content/seeds_dataset (2).csv')
print(df.info())

df.drop('Unnamed: 8',inplace=True,axis=1)

df.drop('Unnamed: 9',inplace=True,axis=1)

for i in df.columns:
  print(df[i].nunique())

gp=df.groupby('Class (1, 2, 3)')['Area'].sum()
gp.plot.bar()
plt.show()

x=df.drop('Class (1, 2, 3)', axis=1)
y=df['Class (1, 2, 3)']
x_tr,x_te,y_tr,y_te=train_test_split(x,y,random_state=42)
model=RandomForestClassifier()
model.fit(x_tr,y_tr)
y_pred=model.predict(x_te)
acc=accuracy_score(y_te,y_pred)
print(acc)