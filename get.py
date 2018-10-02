import requests
payload = {'key1': 'value1', 'key2': 'value2'}
html = requests.get('http://httpbin.org/get', params=payload)
print(html.url)