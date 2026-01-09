import requests
response = requests.get('http://20.91.198.208:8081/submit/get')


parameters = {
    "token": "c5fcbc32",
    "ansvar": "1008"
}
response = requests.get(f'http://20.91.198.208:8081/submit/get', params=parameters)

print(response.status_code)
print(response.headers)
print(response.text)
