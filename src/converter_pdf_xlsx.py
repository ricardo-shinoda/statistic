from decouple import config
import PyPDF2
import json
import re
import pandas as pd

pdf_password = config('PDF_PASSWORD')

pdf_file = open('account_mvt.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_reader.decrypt(pdf_password)

movements = []
date_pattern = r"^\d{2}/\d{2}/\d{4}"  # Matches lines starting with a date

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    lines = text.split('\n')

    current_transaction = None

    for line in lines:
        if re.search(date_pattern, line):
            if current_transaction:
                if "SALDO" not in current_transaction["Transaction"]:
                    movements.append(current_transaction)

            parts = line.strip().split()
            current_date = parts[0]
            description = " ".join(parts[1:-2])
            montante = parts[-2]
            natureza = parts[-1]
            current_transaction = {
                "Date": current_date,
                "Transaction": description,
                "Montante": montante,
                "Natureza": natureza,
            }
        else:
            if current_transaction:
                current_transaction["Transaction"] += "\n" + line.strip()

    if current_transaction:
        if "SALDO" not in current_transaction["Transaction"] and "TOTAL" not in current_transaction["Transaction"]:
            movements.append(current_transaction)


pdf_file.close()

df = pd.DataFrame(movements)

df.to_excel('output_account.xlsx', index=False)

print("Data saved to output_account.xlsx")
