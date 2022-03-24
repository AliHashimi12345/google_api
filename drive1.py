import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

from googleapiclient.http import MediaFileUpload
CLIENT_SECRET_FILE = 'client_secret_200462404523-fanmuul6hgarfq5s3avbs0mlj7tmv6rs.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

file_ids = ['1cb4ytcxm3QPTc2GzKaXjOqS2LsGKpdkl']
file_names = ['ali.jpeg']

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh,request=request)

    done = False

    while not done:
        status,done = downloader.next_chunk()
        print('Download progress {0}',format(status.progress()*100))

    fh.seek(0)

    with open(os.path.join('./114APPLE',file_name),'wb') as f:
        f.write(fh.read())
        f.close()
            

    