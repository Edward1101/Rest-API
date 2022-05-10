import requests

endpoint = "http://localhost:8000/api/products/1/"
endpoint_update = "http://localhost:8000/api/products/1/update/"

data = {
    "shape": "rectangle",
    "a": 12,
    "b": 23,
    "c": 48,
}
get_response = requests.get(endpoint)
print(f"Before update {endpoint} , {get_response}, detail is {get_response.json()}")

get_response = requests.put(endpoint_update, json=data)
# print(get_response.json())
print(f"After update {endpoint_update} , {get_response}, detail is {get_response.json()}")