import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

dataset = pd.read_csv('new_data_set4.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
categorical_columns = [0, 1, 2]

transformers = [
    ('encoder', OneHotEncoder(sparse=False), categorical_columns),  # Set sparse=False
    ('passthrough', 'passthrough', [i for i in range(len(x[0])) if i not in categorical_columns])
]

ct = ColumnTransformer(transformers=transformers)

x = np.array(ct.fit_transform(x))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

poly = PolynomialFeatures(degree=2)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

poly_regressor = LinearRegression()
poly_regressor.fit(x_train_poly, y_train)

y_pred_poly = poly_regressor.predict(x_test_poly)

print("R2 Score for Polynomial Linear Regression: ", r2_score(y_test, y_pred_poly))

x_new = np.array([["Nike", "Brown", "T-Shirt", 87.11]])

encoded_data = ct.transform(x_new)
x_new_poly = poly.transform(encoded_data)
y_new_pred_poly = poly_regressor.predict(x_new_poly)

print("Predicted value:", y_new_pred_poly[0])
