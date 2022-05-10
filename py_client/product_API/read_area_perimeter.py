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


base_endpoint = "http://localhost:8000/api/products/"

token = login()
parameter_get = {
    "token": token,
}


def check_detail(n):
    endpoint = base_endpoint + str(n)
    get_response = requests.get(endpoint, params=parameter_get)
    print(f"{endpoint} , {get_response}, detail is {get_response.json()}")


def check_action(n, action):
    endpoint = base_endpoint + str(n)
    parameter = {
        "token": token,
        "action": action,
    }
    get_response = requests.get(endpoint, params=parameter)
    print(f"{endpoint} , {get_response}, detail is {get_response.json()}")


check_detail(10)
check_action(10, 'perimeter')
check_action(10, 'area')

for n in range(1, 15):
    check_action(n, 'area')
    check_action(n, 'perimeter')


