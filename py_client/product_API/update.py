import requests

# login
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

    return get_response.json()['token']

endpoint = "http://localhost:8000/api/products/3/"
endpoint_update = "http://localhost:8000/api/products/3/update/"

parameter_token ={
    "token": login(),
}
data = {
    "shape": "rectangle",
    "a": 12,
    "b": 23,
    "c": 48,
}

get_response = requests.get(endpoint, params=parameter_token )
print(f"Before update {endpoint} , {get_response}, detail is {get_response.json()}")

get_response = requests.put(endpoint_update, params=parameter_token, json=data)
# print(get_response.json())
print(f"After update {endpoint_update} , {get_response}, detail is {get_response.json()}")