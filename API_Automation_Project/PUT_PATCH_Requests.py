from POST_Requests import create_random_email
from GET_Requests import common_assertion
import requests
import json


# Base URL
base_url = "https://gorest.co.in/"

# Auth Token
auth_token = "Bearer b013e6fd81e30a072c13097ca76f9d87503223970574da8fadeac0370a8d8628"


# PUT Request

def put_method():
    url = base_url + "public/v2/users"
    print("\nUpdate Specific User URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = common_assertion[1]
    json_data["name"] = "Ankit D"
    json_data["id"] = 5678904
    json_data["email"] = "ankit.d@gmail.com"
    print(json.dumps(json_data, indent=4))


# Call Method

put_method()
