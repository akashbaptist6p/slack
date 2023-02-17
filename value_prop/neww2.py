import requests 
# link to files.upload method 
url = "https://slack.com/api/files.upload" 
# this is where you add your query string. Please chage token value 
querystring = {"token":"xoxb-4842699878208-4843307317424-fWAaH3CjIK3ztYDblSDoC7MG"} 
# this is where you define who do you want to send it to. Change channels to your target one 
payload = { "channels":"#csv_to_channel"} 
with open("requirements.txt", 'rb') as fp:
    file_upload = { 
        "file": ("requirements.txt", fp, 'text/plain') 
    }
    response = requests.post(url, data=payload, params=querystring, files=file_upload)
    print (response.content)
