# import requests
# url = "https://httpbin.org/post"

# payload = {
#  "name" : "Naveen",
#  "Course" : "Data Science",
#  "Level" : "Beginner"

# }


# response = requests.post(url, json=payload)
# data = response.json()
# print(data["json"])




import requests

url = "https://httpbin.org/post"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer dummy_token"
}

payload = {
    "email": "naveen@gmail.com",
    "password": "1234"
}

response = requests.post(url, headers=headers, json=payload)

print("Status:", response.status_code)
print(response.json()["headers"])  # shows headers that reached server
print(response.json()["json"])     # shows body that reached server







