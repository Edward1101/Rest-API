import requests

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

param_super_user = {
    "token": get_response.json()['token']
}
print(param_super_user)



endpoint_1 = "http://localhost:8000/api/user/1"

get_response = requests.get(endpoint, params=param_super_user)
print(get_response.json())