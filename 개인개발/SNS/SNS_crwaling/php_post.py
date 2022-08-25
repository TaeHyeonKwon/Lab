import requests

r = requests.get('http://127.0.0.1/nuguna/insight.php').text
print(r)
