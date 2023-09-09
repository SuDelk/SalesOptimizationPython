import pandas as pd
import random
import string

# Create an empty list to store the data
data = []

# Generate 100 sample clothing items
num_samples = 100

for _ in range(num_samples):
    name = ''.join(random.choice(string.ascii_letters) for _ in range(10))  # Random name
    barcode = ''.join(random.choice(string.digits) for _ in range(10))  # Random barcode
    description = ' '.join(random.choice(string.ascii_letters) for _ in range(20))  # Random description
    brand = random.choice(['Brand A', 'Brand B', 'Brand C'])  # Random brand
    color = random.choice(['Red', 'Blue', 'Green', 'Black'])  # Random color
    clothing_type = random.choice(['Shirt', 'Pants', 'Dress', 'Shoes'])  # Random type
    cost = random.uniform(10, 100)  # Random cost between 10 and 100
    hsrp = random.uniform(cost, 150)  # Random humanly suggested price between 20 and 150
    marked_price = random.uniform(cost, 150)
    sold_price = random.uniform(cost, marked_price)
    discount = marked_price - sold_price
    # Append the data as a dictionary to the list
    data.append({
        'name': name,
        'barcode': barcode,
        'description': description,
        'brand': brand,
        'color': color,
        'type': clothing_type,
        'cost': cost,
        'hsrp': hsrp,
        'marked_price': marked_price,
        'discount' : discount,
        'sold_price':sold_price
    })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv("clothing_data2.csv", index=False)
