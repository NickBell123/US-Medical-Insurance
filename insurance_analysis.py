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


# Function to calculate the average age of individuals in the dataset
def calculate_average_age(data):
    ages = [int(row['age']) for row in data if row['age']]
    average_age = sum(ages) / len(ages) if ages else 0
    return average_age

# Test
average_age = calculate_average_age(data)
print(f"Average Age of individuls is: {average_age:.1f}")

def calculate_average_cost(data):
    costs = [float(row['charges']) for row in data if row['charges']]
    average_cost = sum(costs) / len(costs) 
    return average_cost

# Test
average_cost = calculate_average_cost(data)
print(f"Average Cost of insurance is: {average_cost:.2f}")

def calculate_average_bmi(data):
    bmis = [float(row['bmi']) for row in data if row['bmi']]
    average_bmi = sum(bmis) / len(bmis) 
    return average_bmi

# Test
average_bmi = calculate_average_bmi(data)
print(f"Average BMI of individuals is: {average_bmi:.2f}")

# Function to compare costs between smokers and non-smokers
def compare_smoker_costs(data):
    smoker_costs = {'yes': [], 'no': []}
    for row in data:
        if row['smoker'] == 'yes':
            smoker_costs['yes'].append(float(row['charges']))
        elif row['smoker'] == 'no':
            smoker_costs['no'].append(float(row['charges']))
    average_smoker_cost = sum(smoker_costs['yes']) / len(smoker_costs['yes'])
    average_non_smoker_cost = sum(smoker_costs['no']) / len(smoker_costs['no'])

    return average_smoker_cost, average_non_smoker_cost

# Test
average_smoker_cost, average_non_smoker_cost = compare_smoker_costs(data)
print(f"Average Cost for Smokers: {average_smoker_cost:.2f}")
print(f"Average Cost for Non-Smokers: {average_non_smoker_cost:.2f}")