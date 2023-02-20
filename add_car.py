import requests

"""
Esse código é uma implementação de uma requisição HTTP POST para cadastrar um veículo. 
A biblioteca "requests" é usada para enviar a requisição HTTP para a URL especificada.

A entrada dos dados "frota" e "placa" são obtidas do usuário através da função "input()". 
Em seguida, o objeto (payload) é criado, contendo os dados ("Frota", "Placa" e "Despesas"), que são enviados na requisição.
Neste código, o (payload) é especificado como um dicionário Python com as chaves "Frota", "Placa" e "Despesas". 
Esse dicionário é "convertido" em uma string "JSON" "antes de ser enviado para o servidor".

A requisição é feita para a URL "http://localhost:8000/veiculo", com o objeto payload como corpo da requisição,
e o cabeçalho "Content-Type" com o valor "application/json", indicando que o corpo da requisição está no formato JSON.

A resposta da requisição é armazenada na variável "response" e é exibida na tela através da função "print(response.json())".
"""

frota = str(input("Frota: ")).upper()
placa = str(input("Placa: ")).upper()

url = "http://localhost:8000/veiculo"

# Os nomes das chaves devem ser semelhantes ao do Model da API ou seja, como a API diz que deve se chamar.
payload = {"Frota": frota, "Placa": placa, "Despesas": []}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
