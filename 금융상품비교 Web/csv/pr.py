import json
import csv

# Load the data from the provided JSON file
with open('./finance.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract finances and options data
finances = [item['fields'] for item in data if item['model'] == 'finances.finance']
options = [item['fields'] for item in data if item['model'] == 'finances.option']

# Separate deposit and saving products
deposit_products = [item for item in finances if item['prdt_category'] == 'deposit']
saving_products = [item for item in finances if item['prdt_category'] == 'saving']

# Combine products and options
combined_data = []

for product in deposit_products + saving_products:
    product_options = [opt for opt in options if opt['fin_prdt_cd'] == product['fin_prdt_cd']]
    for opt in product_options:
        combined_entry = {
            'Product Code': product['fin_prdt_cd'],
            'Company Number': product['fin_co_no'],
            'Company Name': product['kor_co_nm'],
            'Product Name': product['fin_prdt_nm'],
            'Join Way': product['join_way'],
            'Special Conditions': product['spcl_cnd'],
            'Join Deny': product['join_deny'],
            'Join Member': product['join_member'],
            'Max Limit': product['max_limit'],
            'Interest Rate Type': opt['intr_rate_type_nm'],
            'Saving Term (months)': opt['save_trm'],
            'Interest Rate': opt['intr_rate'],
            'Interest Rate (max)': opt['intr_rate2']
        }
        combined_data.append(combined_entry)

# Define CSV column headers
headers = [
    'Product Code', 'Company Number', 'Company Name', 'Product Name',
    'Join Way', 'Special Conditions', 'Join Deny', 'Join Member', 'Max Limit',
    'Interest Rate Type', 'Saving Term (months)', 'Interest Rate', 'Interest Rate (max)'
]

# Write to CSV file
csv_file_path = './combined_finance_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(combined_data)

csv_file_path