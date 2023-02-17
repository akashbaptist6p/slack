import os
import requests

# link to files.upload method 
url = "https://slack.com/api/files.upload" 

# Get the Slack API token from an environment variable
token = "xoxb-4842699878208-4843307317424-fWAaH3CjIK3ztYDblSDoC7MG"

# Define the file upload parameters
payload = {
    "channels": "#csv_to_channel",
    "initial_comment": "Here is the requirements.txt file.",
}

# Define the file to upload
with open("requirements.txt", 'rb') as f:
    file_upload = {
        "file": (f.name, f),
    }

# Make the request to upload the file
response = requests.post(url, data=payload, params={"token": token}, files=file_upload)

# Check if the request was successful
if response.ok:
    print("File upload successful.")
else:
    print(f"File upload failed: {response.text}")
