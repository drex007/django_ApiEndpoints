from django import http
import requests

endpoint1  = "https://httpbin.org/status/200",
endpoint = "http://localhost:8000/api/",

get_response  = requests.post("http://localhost:8000/api/", json={"title": "Nero"})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
