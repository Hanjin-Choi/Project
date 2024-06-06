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
            '은행명': product['kor_co_nm'],
            '상품명': product['fin_prdt_nm'],
            '단/복리': opt['intr_rate_type_nm'],
            '저축기간': opt['save_trm'],
            '금리': opt['intr_rate'],
            '최대우대금리': opt['intr_rate2']
        }
        combined_data.append(combined_entry)

# Define CSV column headers
headers = ['은행명', '상품명', '단/복리', '저축기간', '금리', '최대우대금리']

# Write to CSV file
csv_file_path = './combined_finance_data2.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(combined_data)

csv_file_path