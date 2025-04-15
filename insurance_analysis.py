# insurance_analysis.py

import csv

# Load insurance.csv
def load_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Test
data = load_data('insurance.csv')
print("Dataset Overview:")
print(f"Rows: {len(data)}")
print(f"Columns: {list(data[0].keys())}")
print(f"Sample row: {data[0]}")