import requests

url = "http://localhost:8000/veiculo/123"

response = requests.get(url)

print(response.json())