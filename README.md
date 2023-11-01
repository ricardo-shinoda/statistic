This is a statistic repository

Note:
credit_card files goes from february 2023 to April 2023, that's because it wasasked to change the due date on the invoice, then the bank jumped on invoice, in this case March 2023. But it's all combined on April 2023 invoice.

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
