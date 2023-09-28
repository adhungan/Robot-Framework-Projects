import string

import requests
import sys
import json
import random


# Function to create new email
def create_random_email():
    domain = "@example.com"
    email_length = 10
    random_string = "".join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + domain
    return email


# Data for POST Request

data = {
    "name": "Ankit" + " ".join(random.choice(string.digits)),
    "email": create_random_email(),
    "gender": "male",
    "status": "active"
}

# Base URL
base_url = "https://gorest.co.in/"

# Auth Token
auth_token = "Bearer b013e6fd81e30a072c13097ca76f9d87503223970574da8fadeac0370a8d8628"

def common_assertion(url, headers):
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    assert response.elapsed.total_seconds() * 1000 < 500
    assert len(response.content) < 4 * 1024
    print("\n******** ALL ASSERTIONS PASSED ********")
    return response.json()



# POST Requests

def create_user():
    url = base_url + "public/v2/users"
    print("\nCreate a new User URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = json.dumps(common_assertion(url, headers=headers), indent=4)
    print(json_data)
    print("\n******** POST Requsst Completed ********")



# Call Methods

create_user()