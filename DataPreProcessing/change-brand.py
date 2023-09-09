import csv

# Define a dictionary to map the old brand names to the new ones
brand_mapping = {
    "Brand A": "Nike",
    "Brand B": "Adidas",
    "Brand C": "Puma"
}

# Input and output file paths
input_file = "clothing_data.csv"
output_file = "output.csv"

# Create an empty list to store the modified data
modified_data = []

# Read data from the input CSV file
with open(input_file, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        old_brand = row[0]
        new_brand = brand_mapping.get(old_brand, old_brand)  # Use the mapping or keep the original if not found
        modified_row = [new_brand] + row[1:]
        modified_data.append(modified_row)

# Write the modified data to the output CSV file
with open(output_file, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(modified_data)

print("Data has been modified and saved to", output_file)
