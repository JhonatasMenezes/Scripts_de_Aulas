import requests

response = requests.get('https://youtube.com')

print(response._content)
