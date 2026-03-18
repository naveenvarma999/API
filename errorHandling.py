# import requests

# url = "https://httpbin.org/post"
# payload = {"name": "Naveen"}

# try:
#     response = requests.post(url, json=payload, timeout=10)
#     response.raise_for_status()  # raises error for 4xx/5xx
#     print("Success:", response.json()["json"])
# except requests.exceptions.RequestException as e:
#     print("Request failed:", e)



# Task

import requests
url = "https://httpbin.org/post"
payload= {"name": "Naveen", "city": "Hyderabad", "goal": "Master APIs"}

try:
    response= requests.post(url, json = payload, timeout=10)
    response.raise_for_status()
    print("Success:", response.json()["json"])
except requests.exceptions.RequestException as e:
    print("Request Failed:", e)
