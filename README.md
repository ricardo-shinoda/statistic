This is a financial control repository

Note:
credit_card files goes from february 2023 to April 2023, that's because it was asked to change the due date on the invoice, then the bank jumped on invoice, in this case March 2023. But it's all combined on April 2023 invoice.

To run this project first install all the dependencies by running, from the root:

`pip install -r requirements.txt`

To update Account_mvt (all the movemnts from the account)

- First activate .venv 
- Download the file from the app (do it monthly)
- Rename to: account_mvt.pdf
- Move to /home/ricardo/code/statistic
- run: `python3 converter_pdf_json.py (from the src)`
- rename the output to: yyyy-mm.json
- Move file renamed to src/account_mvt/json

To update Credit Card invoices:

- From the C6 App, download the invoice .csv file
- Open the downloaded file with TEXT EDITOR Linux app.
- Save as > rename if needed > Desktop
- Move one copy of the file to /home/ricardo/Downloads/invoice
- Download the latest version of Controle.xsls from G-drive
- Rename Controle file to just Controle.xsls
- run `mv /home/ricardo/Downloads/Controle_<year-month>.xlsx /home/ricardo/code/statistic/src`
- Don´t forget to update variable "month" on control.py -"yyyy-mm" like
- First run `python3 extract.py` - If there are zip file
- Then run `python3 control.py`


Files Breakdown:

Conversion Files (convert various files into .json or .xlsx)

    - converter_csv_json.py
    Reads invoice.csv file from repo and convert to .json and save it as "output.json" on /src/credit_card/json

    - convert_csv_xlsx.py
    Does the same as above, but convert to .xlsx and prepare to use on Controle.xlsx.

Upload Files
    
    - drive_upload_tab.py
    Take especific file from credict_card/xlsx/ folder and save it on /src/Controle.xlsx and upload it to G-drive (Statistic folder)

Download File

    - donwload_repo.py
    Download file from /Downloads/invoice to repo also renaming it.

Search Files

    - search for files with .csv on /Downloads/invoice and convert it to .xlsx
