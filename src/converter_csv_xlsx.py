import pandas as pd

df = pd.read_csv('invoice.csv', delimiter=';')

df.to_excel('output.xlsx', index=False)

print("Conversion complete, Data saved in 'output.xlsx'.")
