from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/locations/2178")

#https://docs.openaq.org/docs/getting-started

import requests

url = "https://api.openaq.org/v3/locations"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)



