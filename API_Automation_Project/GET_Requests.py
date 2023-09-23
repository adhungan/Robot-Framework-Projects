import requests
import json
import sys

# Base URL
base_url = "https://gorest.co.in/"

# Auth Token
auth_token = "Bearer b013e6fd81e30a072c13097ca76f9d87503223970574da8fadeac0370a8d8628"

# Save All GET Requests output in a separate file

sys.stdout = open("GET_Request_Output.txt", "w")

# Common assertion method
def common_assertion(url, headers):
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() * 1000 < 500
    assert len(response.content) < 4 * 1024
    print("\n******** ALL ASSERTIONS PASSED ********")
    return response.json()


# GET Methods
def get_all_users():
    url = base_url + "public/v2/users"
    print("\nGet All Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = json.dumps(common_assertion(url, headers=headers), indent=4)
    print(json_data)
    print("\n******** All users printed ********")




def get_specific_user():

    url = base_url + "public/v2/users/5188757"
    print("\nGet Specific Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = json.dumps(common_assertion(url, headers=headers), indent=4)
    print(json_data)
    print("\n******** Specific users printed ********")




def get_specific_info_all_users():

    url = base_url + "public/v2/users"
    print("\nGet Specific info of All Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = common_assertion(url, headers=headers)
    count = 1
    for user in json_data:
        user_name = user.get("name")
        user_id = user.get("id")
        print(f"User details of user {count} is ==> ", {user_id},{user_name})
        count +=1
    print("\n******** Specific info of all users printed ********")




def get_specific_info_specific_user(user_name):
    url = base_url + "public/v2/users"
    print("\nGet Specific Info of Specific Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = common_assertion(url, headers=headers)
    user_found = False
    for user in json_data:
        if user.get("name") == user_name:
            user_details = {key : user[key] for key in ["id", "name", "email"]}
            print(f"\nBasic info of {user_name} is : \n {json.dumps(user_details, indent=4)}")
            print(f"\n******** Specific info of {user_name} printed ********")
            user_found = True
    if user_found == False:
        print(f"{user_name} not found in the Database")




# All Call Methods

get_all_users()
get_specific_user()
get_specific_info_all_users()
get_specific_info_specific_user("Bhadran Johar")


# Restore the Print Statement
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n******************** Checkout the output of all GET Requests printed in GET_Request_Output.txt file "
      "********************\n")

