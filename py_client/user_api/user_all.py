import requests

endpoint = "http://localhost:8000/api/user/1/"

# param = {
#     "token": "ecb77f90d87c4d2cb2a1fe30eaa1dd2a"
# }
#
# get_response = requests.get(endpoint, params=param)
# print(get_response.json())


param_super_user = {
    "token": "80b3beb0a2574c73a7c29aa4ebf5373b"
}

get_response = requests.get(endpoint, params=param_super_user)
print(get_response.json())