import requests
response = requests.get("https://api.agify.io/?name=naveen")
print(response)

data = response.json()
print(data)

print(response.status_code)

age = data["age"]
print(age)