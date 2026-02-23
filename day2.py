import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Naveen",
    "course": "API learning",
    "level": "beginner"
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print(response.json())