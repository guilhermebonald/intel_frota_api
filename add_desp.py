import requests

# Input de valores
frota = str(input("Frota: ")).upper()
nf = str(input("NF: ")).upper()
valor = float(input("R$: "))

# Json para request
# Os nomes das chaves devem ser semelhantes ao do Model da API ou seja, como a API diz que deve se chamar.
payload = {"Frota": frota, "Nf": nf, "Valor": valor}

# Esse header é importante para informar que o tipo de dados enviados é do tipo Json
headers = {"Content-Type": "application/json"}

# url da API
url = "http://localhost:8000/despesa"

response = requests.post(url, json=payload, headers=headers)
print(response.json())