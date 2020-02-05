import requests # api library
import json # json library

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)
print(response.json())
jprint(response.json())

print("wikipedia")
search = "einstein"
response = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search + "&format=json")
print(response.status_code)
jprint(response.json())