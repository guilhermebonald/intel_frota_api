from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB, Query
import pandas as pd

app = FastAPI()

# TinyDB set
db = TinyDB("./storage/data.json")
dataQuery = Query()

class Veiculo(BaseModel):
    Frota: str
    Placa: str
    Despesas: list

class Despesa(BaseModel):
    Frota: str
    Nf: str
    Valor: float

"""
- O parâmetro da função [cadastrar_veiculo] é um objeto ("veiculo" do tipo "Veiculo"). Este objeto é definido na (classe Veiculo) e tem três atributos:
"Frota": um inteiro que representa a frota do veículo.
"Placa": uma string que representa a placa do veículo.
"Despesas": uma lista de objetos Despesa, que representam as despesas do veículo.
- Este objeto é passado para a função cadastrar_veiculo quando a função é chamada, e é usado para adicionar um novo veículo ao banco de dados.

- Quando você passa a (classe Veiculo) como tipo de "parâmetro da função" cadastrar_veiculo, 
você está dizendo que o parâmetro (veiculo) espera receber um "objeto" da classe (Veiculo) que tenha atributos (Frota, Placa e Despesas).

"""

# TODO> Cadastrar veículo.
@app.post("/veiculo")
def cadastrar_veiculo(veiculo: Veiculo): # O parametro que recebe a classe com Model substitui o Input padrão.
    validation = db.search(dataQuery.Frota == veiculo.Frota)
    if validation == []:
        db.insert(veiculo.dict())
        return {"message": "Veículo cadastrado com sucesso"}
    else:
        return {"message": "Veículo já está no cadastro"}

# TODO> Adicionar despesa.
@app.post("/despesa")
def adicionar_despesa(despesa: Despesa):
    frota = despesa.Frota
    item = db.search(dataQuery.Frota == frota)
    if len(item) == 0:
        return {"message": "Veículo não cadastrado"}
    else:
        nf = despesa.Nf
        valor = despesa.Valor
        despesa_dict = {"NF": nf, "R$": valor}
        item[0]["Despesas"].append(despesa_dict)
        db.update(item[0], doc_ids=[item[0].doc_id])
        return {"message": "Despesa adicionada com sucesso"}

# TODO> Buscar veículo.
@app.get("/veiculo/{frota}")
def procurar_veiculo(frota: str):
    bloco = db.search(dataQuery.Frota == frota)
    n_nf = []
    v_nf = []
    if bloco == []:
        return {"message": "Veículo não encontrado"}
    else:
        for dict_nf in bloco:
            placa = dict_nf["Placa"]
            for despesas in dict_nf["Despesas"]:
                n_nf.append(despesas["NF"])
                v_nf.append(despesas["R$"])
        table = {"NF": n_nf, "R$": v_nf}
        df = pd.DataFrame(table)
        return {"Placa": placa, "Despesas": df.to_dict()} 