import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

dataset = pd.read_csv('dataset_clothing4.csv') #change dataset as needed

x = dataset.iloc[:, :-1].values  # locate index
y = dataset.iloc[:, -1].values  # locate index

categorical_columns = [0, 1, 2]

transformers = [('encoder', OneHotEncoder(), categorical_columns), 
                ('passthrough', 'passthrough', 
                 [i for i in range(len(x[0])) if i not in categorical_columns])]
ct = ColumnTransformer(transformers=transformers)
x = np.array(ct.fit_transform(x).toarray())

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print("R2 Score for Multiple Linear Regression Model: ", r2_score(y_test, y_pred))

np.set_printoptions(precision=2)

x_new = ([["Nike", "Brown", "T-Shirt", 87.11]])
encoded_data = ct.transform(x_new)

y_new_pred = regressor.predict(encoded_data)

print(y_new_pred[0])