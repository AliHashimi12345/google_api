from Google  import Create_Service
CLIENT_SECRET_FILE = 'client_secret_200462404523-fanmuul6hgarfq5s3avbs0mlj7tmv6rs.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']
service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

source_folder_id  = '1W4nOP4bkCAVQvpYm9Fs3IMO6vEPboWBp'
target_folder_id = '12RYi3vWvZ4ZuDFrDEVBqaG2oUb2Dggkh'
query = f"parents = '{source_folder_id}'"

response = service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query,pageToken=nextPageToken)
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

for f in files:
    if f['mimeType'] != 'application/vnd.google-apps.folder':
        service.files().update(
            fileId=f.get('id'),
            addParents=target_folder_id,
            removeParents=source_folder_id
        ).execute()   