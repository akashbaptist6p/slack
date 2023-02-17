import requests 
# link to files.upload method 
url = "https://slack.com/api/files.upload" 
# this is where you add your query string. Please chage token value 
querystring = {"token":"xoxb-4842699878208-4843307317424-fWAaH3CjIK3ztYDblSDoC7MG"} 
# this is where you define who do you want to send it to. Change channels to your target one 
payload = { "channels":"#csv_to_channel"} 
file_upload = { 
"file":("requirements.txt", 
open("requirements.txt", 'rb'), 'text/plain') 
} 
headers = { "Content-Type": "multipart/form-data", } 
response = requests.post(url, data=payload, params=querystring, files=file_upload)

