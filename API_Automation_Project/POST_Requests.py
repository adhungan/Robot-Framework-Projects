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

data =

# PUT Request
