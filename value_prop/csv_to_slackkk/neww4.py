import os
import requests
from dotenv import load_dotenv
import os

load_dotenv()

slack_token = os.getenv('SLACK_API_TOKEN')
slack_channel= os.getenv('SLACK_API_CHANNEL')


# set up file path and name
file_path = "data.csv"
file_name = "data.csv"

# open the file and read its contents
with open(file_path, "rb") as f:
    file_data = f.read()


# set up the Slack API endpoint for file uploads
url = "https://slack.com/api/files.upload"

# set up the request headers and data
headers = {
    "Authorization": f"Bearer {slack_token}",
    #"Content-type": "multipart/form-data",
}
data = {
    "channels": slack_channel,
    "filename": file_name,
}
files = {
    "file": (file_name, file_data, "text/csv"),
}

# send the file to the Slack channel
response = requests.post(url, headers=headers, data=data, files=files)
print(response)
print(response.content)

# check the response for errors
if not response.ok:
    raise ValueError(f"Failed to upload file: {response.text}")
