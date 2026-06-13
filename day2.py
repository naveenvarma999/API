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




# day 2

#http methods

GET --- reads the data

POST -- create the data

PUT  --- update the data

PATCH  --- updates the data partially based on our requirement

DELETE  -- delete the data from the server


# Status codes

200  --- ok success

201  ---- created


401  --- autorization required

403  --- forbidden

404  --- user not found


429 --- too many requests

500 -- internal server error

506 --- service unavaialbe
