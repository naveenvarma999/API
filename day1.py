
# Your FIRST API Call (GET)
# We’ll use a free public API for learning.
# ✅ Example: Get a random user

import requests   # Imports the library that sends HTTP requests

response = requests.get("https://randomuser.me/api/")   #Sends a GET request to the API
print(response.status_code)    # 200   --> success


# Read the Actual Data (JSON)
data = response.json()
print(data)


user = data["results"][0]
first_name = user["name"]["first"]
email = user["email"]

print(first_name)
print(email)


# Handle Errors Properly
if response.status_code == 200:
    data = response.json()
    print("success")
else:
    print("Error:",response.status_code)