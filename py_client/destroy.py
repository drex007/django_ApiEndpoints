from django import http
import requests

endpoint = "http://localhost:8000/api/",

product_id = input("Input ID:")
newProduct_Id = int(product_id)

if newProduct_Id is not None:
    get_response  = requests.delete(f"http://localhost:8000/api/products/{newProduct_Id}/delete/")
    # print(get_response.text)
    print(get_response.status_code)
    print(get_response.json())
else:
    print("Product Id is Not Valid")




