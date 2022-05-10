import requests
import random


def login():
    endpoint = "http://localhost:8000/api/user/"

    parameter = {
        "action": "login",
    }

    data = {
        "user_name": "user_1",
        "user_password": "12345"
    }

    get_response = requests.post(endpoint, params=parameter, json=data)
    print(get_response.json())

    param_user_token = {
        "token": get_response.json()['token']
    }
    print(param_user_token)
    return param_user_token


endpoint = "http://localhost:8000/api/products/"

shape = ["triangle", "rectangle", "square", "diamond"]

param_user_token = login()


def create_new(n):
    data = {
        "shape": random.choice(shape),
        "a": n,
        "b": n - 1,
        "c": n + .1,
    }

    get_response = requests.post(endpoint, params=param_user_token, json=data)
    print(get_response.json())


for n in range(20, 28):
    create_new(n)
