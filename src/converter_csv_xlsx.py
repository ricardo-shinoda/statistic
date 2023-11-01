# import pandas as pd

# df = pd.read_csv('invoice.csv', delimiter=';')

# df.to_excel('output.xlsx', index=False)

# print("Conversion complete, Data saved in 'output.xlsx'.")


import pandas as pd

# Read the CSV file with the specified delimiter
df = pd.read_csv('invoice.csv', delimiter=';')

# Format the numbers in the DataFrame to use Brazilian standards
df['Valor (em R$)'] = df['Valor (em R$)'].apply(lambda x: f'{x:,.2f}'.replace('.', 'X').replace(',', '.').replace('X', ','))

# Save the DataFrame to an Excel file with the desired format
df.to_excel('output.xlsx', index=False, float_format="%.2f")

print("Conversion complete, Data saved in 'output.xlsx'.")
