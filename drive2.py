import os
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
CLIENT_SECRET_FILE = 'client_secret_200462404523-fanmuul6hgarfq5s3avbs0mlj7tmv6rs.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

def export_csv_file(file_path: str,parents: list=None):
    if not os.path.exists(file_path):
        print(f'(file_path)not found.')
        return
    try:

        file_metadata = {
            'name': os.path.basename(file_path).replace('.csv','.'),
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': parents
            
        }
        media = MediaFileUpload(filename=file_path,mimetype='text/csv')

        response = service.files().create(
            media_body=media,
            body=file_metadata
        ).execute()

        print(response)
        return(response)
    except Exception as e:
        print(e)
        return


csv_files = os.listdir('./pandas1')

for csv_file in csv_files:
    export_csv_file(os.path.join('pandas1',csv_file))
    export_csv_file(os.path.join('pandas1',csv_file),parents=['12RYi3vWvZ4ZuDFrDEVBqaG2oUb2Dggkh'])


