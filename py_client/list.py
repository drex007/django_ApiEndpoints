from django import http
import requests
from getpass import getpass
endpointq = "http://localhost:8000/api/products",
endpoint = "http://localhost:8000/api/",

username = input("Enter Username: ")
password = getpass()

auth_token  = requests.post("http://localhost:8000/api/auth/", json= {
    "username":username, "password":password,
})
print(auth_token.json())
if auth_token.status_code == 200:
    token = auth_token.json()['token']
    headers = {
        "Authorization": token
    }
    get_response  = requests.get("http://localhost:8000/api/products", headers=headers)
    # print(get_response.text)
    # print(get_response.status_code)
    print(get_response.json())


# # print(get_response.status_code)
# print(get_response.json())

# get_response  = requests.get("http://localhost:8000/api/products")
# # print(get_response.text)
# # print(get_response.status_code)
# print(get_response.json())
