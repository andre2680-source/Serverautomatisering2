import requests
response = requests.get('https://httpbin.org/get')

parameters = {
    "navn": "Andre",
    "alder": "34"
}
response = requests.get('https://httpbin.org/get', params=parameters)

print(response.url)