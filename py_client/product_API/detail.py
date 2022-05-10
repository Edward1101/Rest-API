import requests

base_endpoint = "http://localhost:8000/api/products/"


for n in range(9,18):
    endpoint = base_endpoint + str(n)
    # print(endpoint)
    get_response = requests.get(endpoint)
    print(f"{endpoint} , {get_response}, detail is {get_response.json()}")
    # print(get_response.json())