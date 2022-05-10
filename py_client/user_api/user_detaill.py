import requests

endpoint_single = "http://localhost:8000/api/user/1"
endpoint_all = "http://localhost:8000/api/user/"

param_user_token = {
    "token": "af4c63db5caa451780191a84f9a2a17f"
}

get_response = requests.get(endpoint_single, params=param_user_token)
print(f"get single user detail is {get_response.json()}")

get_response = requests.get(endpoint_all, params=param_user_token)
print(f"get all user detail is {get_response.json()}")