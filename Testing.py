import requests

data = {
    "departure": "WRO",
    "arrival": "WAW"
}
print(requests.post('http://127.0.0.1:5000/flights', data))

