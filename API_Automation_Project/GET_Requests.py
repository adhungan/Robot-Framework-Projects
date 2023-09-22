import requests
import json

# Base URL
base_url = "https://gorest.co.in/"

# Auth Token
auth_token = "Bearer b013e6fd81e30a072c13097ca76f9d87503223970574da8fadeac0370a8d8628"


# Common assertion method
def common_assertion(url, headers):
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() * 1000 < 500
    assert len(response.content) < 4 * 1024
    return response.json()


# GET Methods
def get_all_users():
    url = base_url + "public/v2/users"
    print("Get All Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = json.dumps(common_assertion(url, headers=headers), indent=4)
    print(json_data)
    print("******** All users printed ********")



def get_specific_user():
    url = base_url + "public/v2/users/5188822"
    print("Get Specific Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = json.dumps(common_assertion(url, headers=headers), indent=4)
    print(json_data)
    print("******** Specific users printed ********")



def get_specific_info_all_users():
    url = base_url + "public/v2/users"
    print("Get Specific info of All Users URL : ", url)
    headers = {"Authorization": auth_token}
    json_data = common_assertion(url, headers=headers)
    count = 1
    for user in json_data:
        user_name = user.get("name")
        user_id = user.get("id")
        print(f"User details of user {count} is ==> ", {user_id},{user_name})
        count +=1
    print("******** Specific info of all users printed ********")








# Call Methods
get_all_users()
get_specific_user()
get_specific_info_all_users()
