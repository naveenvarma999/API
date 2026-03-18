import requests

response = requests.get("https://randomuser.me/api/")
print(response)

data = response.json()
print(data)

users = data["results"]

if len(users) > 0:
    user = users[0]
    first_name = user["name"]["first"]
    email = user["email"]

    print(first_name)
    print(email)
else:
    print("No user data received from API")



if response.status_code == 200:
    data = response.json()
    print("Success")
else:
    print("Error:", response.status_code)