import pandas as pd


# rename this variable to save the file according to the invoice month
month = "2023-09"

# Read the CSV file with the specified delimiter
df = pd.read_csv('invoice.csv', delimiter=';')

# Format the numbers in the DataFrame to use Brazilian standards
df['Valor (em R$)'] = df['Valor (em R$)'].apply(lambda x: f'{x:,.2f}'.replace('.', 'X').replace(',', '.').replace('X', ','))

# Exclude rows with "Inclusao de Pagamento" in the "Descrição" column
df = df[df['Descrição'] != 'Inclusao de Pagamento    ']

# Save the DataFrame to an Excel file with the desired format
df.to_excel(f'/home/ricardo/code/statistic/src/credit_card/xlsx/{month}.xlsx', index=False, float_format="%.2f")

print("Conversion complete, Data saved in 'output.xlsx'.")
