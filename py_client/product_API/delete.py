import requests

product_id = input("WHat is the product id you want to use?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
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


    parameter_token = {
        "token": login(),
    }

    endpoint_display = f"http://localhost:8000/api/products/{product_id}/"
    # display data to be delete
    get_response = requests.get(endpoint_display, params=parameter_token)
    print(f"Before delete {endpoint_display} , {get_response}, detail is {get_response.json()}")

    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    # delete
    get_response = requests.delete(endpoint, params=parameter_token)
    print(get_response.status_code, get_response.status_code == 204)

    # show data deleted
    get_response = requests.get(endpoint_display)
    print(f"After delete {endpoint_display} , {get_response}, detail is {get_response.json()}")
