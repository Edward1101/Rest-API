import requests

product_id = input("WHat is the product id you want to use?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')

if product_id:
    endpoint_display = f"http://localhost:8000/api/products/{product_id}/"
    # display data to be delete
    get_response = requests.get(endpoint_display)
    print(f"Before delete {endpoint_display} , {get_response}, detail is {get_response.json()}")


    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    # delete
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)

    # show data deleted
    get_response = requests.get(endpoint_display)
    print(f"After delete {endpoint_display} , {get_response}, detail is {get_response.json()}")
