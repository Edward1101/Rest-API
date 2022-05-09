import requests

endpoint = "http://localhost:8000/api/products/" 


def create_new(n):
    data = {
        "shape": "triangle",
        "a": n,
        "b": n,
        "c": n + .1,
    }
    get_response = requests.post(endpoint, json=data)
    print(get_response.json())

for n in range(4,13):
    create_new(n)