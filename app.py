import streamlit as st
import pickle
import numpy as np
import pandas as pd
# import seaborn as sn
import matplotlib.pyplot as plt

data=pd.read_csv("kc_house_data[1].csv")

x=data.drop(['date','id','price','zipcode'],axis=1)
y=data['price']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=20)

from sklearn.ensemble import RandomForestRegressor
reg=RandomForestRegressor(n_estimators=100,random_state=0)
reg.fit(x_train,y_train)
pred=reg.predict(x_test)
# print(pred)

pickle.dump(reg,open('reg_model.pkl','wb'))
from sklearn import metrics
print("r_2 score is:",metrics.r2_score(y_test,pred))
print("Mean Absolute Error:", metrics.mean_absolute_error( y_test,pred)) 
print("Mean Squared Error:", metrics.mean_squared_error(y_test,pred)) 
print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(y_test,pred)))

# print(reg.predict([[3.00000e+00,  1.75000e+00,  2.45000e+03,  2.69100e+03,
#         2.00000e+00,  0.00000e+00,  0.00000e+00,  3.00000e+00,
#         8.00000e+00,  1.75000e+03,  7.00000e+02,  1.91500e+03,
#         0.00000e+00,  4.76386e+01, -1.22360e+02,  1.76000e+03,
#         3.57300e+03]]))

# print(x.iloc[26].values)
print(reg.predict([x.iloc[26].values]))


    