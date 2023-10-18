import pandas as pd
import json

df = pd.read_csv('invoice.csv', delimiter=';')

data = df.to_dict(orient='records')

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("Conversion complete. Data saved on 'output.json'.")

