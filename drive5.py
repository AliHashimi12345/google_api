from Google  import Create_Service
CLIENT_SECRET_FILE = 'client_secret_200462404523-fanmuul6hgarfq5s3avbs0mlj7tmv6rs.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

sheet_id = '1YoOnahZOragclYmlGiORPAlAfLmt3zTLmMKiGhv6nIQ'

service.files().export_media(
    fileId=sheet_id,
    mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

).execute()

with open('Budget Template.xlsx','wb') as f:
    f.write(byteData)
    f.close()