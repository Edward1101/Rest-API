import requests

endpoint = "http://localhost:8000/api/products/1/update/" 

data = {
    "shape": "rectangle",
    "a": 12,
    "b": 23,
    "c": 48,
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())