#importing basic packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#Loading the data
data0 = pd.read_csv('5.urldata.csv')
data = data0.drop(['Domain'], axis = 1).copy()
data = data.sample(frac=1).reset_index(drop=True)
y = data['Label']
X = data.drop('Label',axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)

#XGBoost Classification model
from xgboost import XGBClassifier

# instantiate the model
xgb = XGBClassifier(learning_rate=0.4,max_depth=7)
#fit the model
xgb.fit(X_train, y_train