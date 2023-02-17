import requests 
my_file = {
  'file' : ('day.csv', open('day.csv', 'rb'), 'csv')
}

payload={
  "filename":"day.csv", 
  "token":"xoxb-4842699878208-4843307317424-fWAaH3CjIK3ztYDblSDoC7MG",
  "channels":['#random']
}

r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)