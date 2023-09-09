import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

dataset = pd.read_csv('clothing_data.csv')

# independent variables (features)
x = dataset.iloc[:, :-1].values  # locate index

# dependent variable
y = dataset.iloc[:, -1].values  # locate index

categorical_columns = [0, 1, 2]

transformers = [('encoder', OneHotEncoder(), categorical_columns), 
                ('passthrough', 'passthrough', 
                 [i for i in range(len(x[0])) if i not in categorical_columns])]
ct = ColumnTransformer(transformers=transformers)
x = np.array(ct.fit_transform(x))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predict test set results
y_pred = regressor.predict(x_test)
print("R2 value: ", r2_score(y_test, y_pred))

# np.set_printoptions(precision=2)
print(np.concatenate([y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)], axis=1))  # reshape(no of rows, no of cols)

x_new = ([["Nike", "Black", "Shirt", 87.11]])
encoded_data = ct.transform(x_new)

print(encoded_data)

# # Predict using the trained model
y_new_pred = regressor.predict(encoded_data)

print(y_new_pred[0])
