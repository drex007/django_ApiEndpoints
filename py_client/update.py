from django import http
import requests

endpoint = "http://localhost:8000/api/",

data = {
    "title": "james and Garri updated ",
    "price" : 123.00,
}

get_response  = requests.put("http://localhost:8000/api/products/1/update/", json=data)
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())
