# This is going to be the file to search for an invoice on Downloads page on My computer
# and move it to this repository
import os
import shutil
import pandas as pd
import json

source_directory = "/home/ricardo/Downloads/invoice"

# Rename it as needed
month = "2023-00"

target_extension = ".csv"

destination_directory = "/home/ricardo/code/statistic/src"

for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith(target_extension):
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_directory, file)
            shutil.move(source_file_path, destination_file_path)
            break

df = pd.read_csv(destination_file_path, delimiter=';')

data = df.to_dict(orient='records')

with open(f'/home/ricardo/code/statistic/src/credit_card/json/{month}.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

# Format the numbers in the DataFrame to use Brazilian standards
df['Valor (em R$)'] = df['Valor (em R$)'].apply(lambda x: f'{x:,.2f}'.replace('.', 'X').replace(',', '.').replace('X', ','))

# Exclude rows with "Inclusao de Pagamento" in the "Descrição" column
df = df[df['Descrição'] != 'Inclusao de Pagamento    ']

# Save the DataFrame to an Excel file with the desired format
df.to_excel(f'/home/ricardo/code/statistic/src/credit_card/xlsx/{month}.xlsx', index=False, float_format="%.2f")

print(f'Invoice {month} has been moved and converted to .csv and .xlsx files')