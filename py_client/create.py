from django import http
import requests

endpointq = "http://localhost:8000/api/products/1",
endpoint = "http://localhost:8000/api/",

data = {
    "title": "Temi and Garri",
    "price" : 200.00,
}

get_response  = requests.post("http://localhost:8000/api/products/create/", json=data)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
