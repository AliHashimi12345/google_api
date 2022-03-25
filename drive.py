from Google import Create_Service
from googleapiclient.http import MediaFileUpload
CLIENT_SECRET_FILE = 'client_secret_200462404523-fanmuul6hgarfq5s3avbs0mlj7tmv6rs.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

folder_id = '1W4nOP4bkCAVQvpYm9Fs3IMO6vEPboWBp'
file_names = ['ali.jpg']
mime_types = ['image/jpeg']
for file_name,mime_type in zip(file_names,mime_types):

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]

    }

    media = MediaFileUpload('./114APPLE/{0}'.format(file_name),mimetype=mime_type)
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
        

    
