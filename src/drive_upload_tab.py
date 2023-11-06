import openpyxl
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

file_name = "2023-08"

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'service.account.json'
PARENT_FOLDER_ID = "1qyMZb6P7H5oaq2zxoaqs17VJWSnHNgnG"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': f'{file_name}.xlsx',
        'parents': [PARENT_FOLDER_ID]
    }

    try:
        # Upload the file to Google Drive
        media = MediaFileUpload(file_path, resumable=True)
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        # Get the file ID of the uploaded file
        uploaded_file_id = file.get('id')

        # Specify the source file and sheet names
        source_file = '/home/ricardo/code/statistic/src/credit_card/xlsx/2023-09.xlsx'  # Source file path
        source_sheet_name = 'Sheet1'  # Source sheet name

        # Open the source workbook
        source_workbook = openpyxl.load_workbook(source_file, data_only=True)

        # Get the source worksheet
        source_sheet = source_workbook[source_sheet_name]

        # Specify the target file and sheet names
        target_file_path = '/home/ricardo/code/statistic/src/Controle.xlsx'  # Target file path
        target_sheet_name = 'new'  # Target sheet name

        # Open the target workbook
        target_workbook = openpyxl.load_workbook(target_file_path, data_only=True)

        # Get the target worksheet
        target_sheet = target_workbook[target_sheet_name]

        # Copy the contents of the source worksheet to the target worksheet
        for row in source_sheet.iter_rows(values_only=True):
            target_sheet.append(row)

        # Save the changes to the target workbook
        target_workbook.save(target_file_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

upload_file(f'/home/ricardo/code/statistic/src/credit_card/xlsx/{file_name}.xlsx')
