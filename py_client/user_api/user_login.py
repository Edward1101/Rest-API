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
