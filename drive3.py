import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service
CLIENT_SECRET_FILE = 'client_secret_200462404523-fanmuul6hgarfq5s3avbs0mlj7tmv6rs.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

file_id = '1Dj2qZ7XdfnO4QAz2MM6tKqxDQ3kGrcaqThWR9OAYw6Y'

byteData = service.files().export_media(
    fileId=file_id,
    mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
).execute()

with open('Project Proposal.docx','wb') as f:
    f.write(byteData)
    f.close()