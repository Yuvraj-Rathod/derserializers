import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : 'me',
    'roll' : 101,
    'city' : 'Ranchi'
}
#dump use to convert python to JSON
#loads use to convert JSON to python
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)