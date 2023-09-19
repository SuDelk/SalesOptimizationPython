import pandas as pd
import random
import string

# Create an empty list to store the data
data = []

# Generate 100 sample clothing items
num_samples = 5000

for _ in range(num_samples):
    # get 20 random clothing brands
    brand = random.choice(['H&M', 'Zara', 'Nike', 'Under Armour', 'Adidas', 'Puma', 'Reebok', 'Nike',
                           'Levis', 'Tommy Hilfiger', 'Ralph Lauren', 'Lacoste', 'Calvin Klein',
                           'Gucci', 'Prada', 'Versace', 'Armani', 'Chanel', 'Burberry', 'Dior'])

    # get 10 random clothing colors
    color = random.choice(['Red', 'Blue', 'Green', 'Black',
                          'White', 'Orange', 'Yellow', 'Purple', 'Pink', 'Brown'])

    # get 20 random clothing types
    clothing_type = random.choice(['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket', 'Jeans', 'Shorts', 'Skirt', 'Dress',
                                   'Socks', 'Underwear', 'Bra', 'Shoes', 'Boots', 'Sandals', 'Slippers', 'Hat', 'Gloves', 'Scarf',
                                   'Jewelry'])

    # get a random cost between 10 and 100
    cost = 10

    # get cost differently by the clothing_type for H&M brand
    if brand == 'H&M':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(10, 50)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(20, 70)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(5, 20)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(20, 100)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(5, 30)

    # get cost differently by the clothing_type for Zara brand
    elif brand == 'Zara':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(20, 70)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(30, 100)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(10, 30)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(30, 150)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(10, 50)

    # get cost differently by the clothing_type for Nike brand
    elif brand == 'Nike':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(30, 100)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(50, 150)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(20, 50)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(50, 200)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(20, 70)

    # get cost differently by the clothing_type for Under Armour brand
    elif brand == 'Under Armour':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(40, 120)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(60, 180)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(30, 80)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(60, 240)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(30, 100)

    # get cost differently by the clothing_type for Adidas brand
    elif brand == 'Adidas':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(50, 150)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(70, 210)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(40, 100)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(70, 280)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(40, 140)

    # get cost differently by the clothing_type for Puma brand
    elif brand == 'Puma':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(60, 180)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(80, 240)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(50, 120)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(80, 320)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(50, 160)

    # get cost differently by the clothing_type for Reebok brand
    elif brand == 'Reebok':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(70, 210)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(90, 270)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(60, 140)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(90, 360)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(60, 180)

    # get cost differently by the clothing_type for Levis brand
    elif brand == 'Levis':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(80, 240)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(100, 300)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(70, 160)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(100, 400)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(70, 200)

    # get cost differently by the clothing_type for Tommy Hilfiger brand
    elif brand == 'Tommy Hilfiger':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(90, 270)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(110, 330)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(80, 180)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(110, 440)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(80, 220)

    # get cost differently by the clothing_type for Ralph Lauren brand
    elif brand == 'Ralph Lauren':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(100, 300)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(120, 360)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(90, 200)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(120, 480)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(90, 240)

    # get cost differently by the clothing_type for Lacoste brand
    elif brand == 'Lacoste':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(110, 330)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(130, 390)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(100, 220)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(130, 520)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(100, 260)

    # get cost differently by the clothing_type for Calvin Klein brand
    elif brand == 'Calvin Klein':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(120, 360)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(140, 420)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(110, 240)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(140, 560)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(110, 280)

    # get cost differently by the clothing_type for Gucci brand
    elif brand == 'Gucci':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(130, 390)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(150, 450)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(120, 260)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(150, 600)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(120, 300)

    # get cost differently by the clothing_type for Prada brand
    elif brand == 'Prada':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(140, 420)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(160, 480)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(130, 280)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(160, 640)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(130, 320)

    # get cost differently by the clothing_type for Versace brand
    elif brand == 'Versace':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(150, 450)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(170, 510)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(140, 300)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(170, 680)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(140, 340)

    # get cost differently by the clothing_type for Armani brand
    elif brand == 'Armani':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(160, 480)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(180, 540)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(150, 320)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(180, 720)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(150, 360)

    # get cost differently by the clothing_type for Chanel brand
    elif brand == 'Chanel':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(170, 510)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(190, 570)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(160, 340)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(190, 760)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(160, 380)

    # get cost differently by the clothing_type for Burberry brand
    elif brand == 'Burberry':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(180, 540)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(200, 600)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(170, 360)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(200, 800)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(170, 400)

    # get cost differently by the clothing_type for Dior brand
    elif brand == 'Dior':
        if clothing_type in ['T-Shirt', 'Polo Shirt', 'Sweater', 'Hoodie', 'Jacket']:
            cost = random.uniform(190, 570)
        elif clothing_type in ['Jeans', 'Shorts', 'Skirt', 'Dress']:
            cost = random.uniform(210, 630)
        elif clothing_type in ['Socks', 'Underwear', 'Bra']:
            cost = random.uniform(180, 380)
        elif clothing_type in ['Shoes', 'Boots', 'Sandals', 'Slippers']:
            cost = random.uniform(210, 840)
        elif clothing_type in ['Hat', 'Gloves', 'Scarf', 'Jewelry']:
            cost = random.uniform(180, 420)

    marked_price = random.uniform(cost * 1.2, 200)

    # Append the data as a dictionary to the list
    data.append({
        'brand': brand,
        'color': color,
        'type': clothing_type,
        'cost': cost,
        'marked_price': marked_price
    })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv("dataset_clothing5.csv", index=False)
