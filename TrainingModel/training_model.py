import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data from the CSV file
data = pd.read_csv('clothing_data2.csv')

# Split the data into features (X) and target (y)
X = data.drop(columns=['marked_price'])
y = data['marked_price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Root Mean Squared Error: {rmse}")

# Predict the marked price for a new item (replace 'new_item_details' with actual data)
new_item_details = pd.DataFrame({'brand': ['BrandX'], 'type': ['Shirt'], 'material': ['Cotton'], 'size': ['M']})
predicted_marked_price = model.predict(new_item_details)
print(f"Predicted Marked Price for New Item: {predicted_marked_price[0]}")
