from decouple import config
import PyPDF2
import json
import re

pdf_password = config('PDF_PASSWORD')

pdf_file = open('account_mvt.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_reader.decrypt(pdf_password)

movements = []

date_pattern = r"\d{2}/\d{2}/\d{4}"

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    lines = text.split('\n')
    current_date = None
    movement = None

    for line in lines:
        if re.search(date_pattern, line):
            if movement:
                movements.append(movement)
            parts = line.strip().split()
            current_date = parts[0]
            description = " ".join(parts[1:-2])
            montante = parts[-2]
            natureza = parts[-1]
            movement = {"Date": current_date, "Transaction": description, "Montante": montante, "Natureza": natureza, "Transactions": []}
        else:
            if movement is not None:
                movement["Transactions"].append(line.strip())

if movement:
    movements.append(movement)

pdf_file.close()

data = {
    'text': '',
    'structure': [],
    'movements': movements
}

movements_data = {
    'movements': movements
}

data.update(movements_data)

json_data = json.dumps(data, ensure_ascii=False, indent=4)

with open('output_account.json', 'w') as json_file:
    json_file.write(json_data)

print(json_data)