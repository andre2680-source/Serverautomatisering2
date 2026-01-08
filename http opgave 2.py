import requests
response = requests.get('https://httpbin.org/headers')

print(response.headers)
print(response.text)