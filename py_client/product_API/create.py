import requests
import random

endpoint = "http://localhost:8000/api/products/" 

shape = ["triangle", "retangle", "square", "diamond"]

def create_new(n):
    data = {
        "shape": random.choice(shape),
        "a": n,
        "b": n-1,
        "c": n + .1,
    }
    get_response = requests.post(endpoint, json=data)
    print(get_response.json())

for n in range(20,28):
    create_new(n)