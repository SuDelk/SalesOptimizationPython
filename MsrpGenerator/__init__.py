import json
import logging
import random
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

     # Set CORS headers to allow requests from any origin
    headers  = {
        'Access-Control-Allow-Origin': 'http://localhost:5173,*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        'Content-Type': 'application/json'
    }
    if req.method == "OPTIONS":
        # Handle preflight requests (OPTIONS) with a 200 OK response
        return func.HttpResponse(
            status_code=200,
            headers=headers
        )
    else:
        cost = req.params.get('cost')
        brand = req.params.get('brand')
        type_of_clothing = req.params.get('type')
        color = req.params.get('color')

        if not (cost or brand or type_of_clothing or color):
            try:
                req_body = req.get_json()
            except ValueError:
                pass
            else:
                cost = req_body.get('cost')
                brand = req_body.get('brand')
                type_of_clothing = req_body.get('type')
                color = req_body.get('color')

        if (cost and brand and type_of_clothing and color):
            msrp = predict_price(cost=cost, brand=brand, type=type_of_clothing, color=color)
            # Create a dictionary to represent your JSON response
            response_data = {
                'msrp': msrp
            }

            # Serialize the dictionary to a JSON string
            json_response = json.dumps(response_data)

            return func.HttpResponse(json_response, headers=headers)
        else:
            return func.HttpResponse(
                "Didn't recieve item",
                status_code=422
            )
    
def generate_price(cost):
    return (round(float(random.uniform(cost * 1.2, cost * 1.8)) / 10) * 10 ) - 0.01

def predict_price(cost, brand, type, color):
    dataset = pd.read_csv('https://sliitb83e.blob.core.windows.net/clothing-data-for-spm/final_data_set.csv')

    # independent variables (features)
    x = dataset.iloc[:, :-1].values  # locate index

    # dependent variable
    y = dataset.iloc[:, -1].values  # locate index

    categorical_columns = [0, 1, 2]

    transformers = [('encoder', OneHotEncoder(), categorical_columns), 
                    ('passthrough', 'passthrough', 
                    [i for i in range(len(x[0])) if i not in categorical_columns])]
    ct = ColumnTransformer(transformers=transformers)
    x = np.array(ct.fit_transform(x).toarray())

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    # predict test set results
    y_pred = regressor.predict(x_test)
    print("R2 value: ", r2_score(y_test, y_pred))

    # np.set_printoptions(precision=2)
    print(np.concatenate([y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)], axis=1))  # reshape(no of rows, no of cols)

    x_new = ([[brand, color, type, cost]])
    encoded_data = ct.transform(x_new)

    print(encoded_data)

    # Predict using the trained model
    y_new_pred = regressor.predict(encoded_data)

    return y_new_pred[0]