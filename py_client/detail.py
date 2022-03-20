from django import http
import requests

endpointq = "http://localhost:8000/api/products/1",
endpoint = "http://localhost:8000/api/",

get_response  = requests.get("http://localhost:8000/api/products/1", json={"title": "Nero"})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
