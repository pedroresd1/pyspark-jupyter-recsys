from fastapi import FastAPI
import uvicorn
from db import mongo

app = FastAPI()
conexao  = mongo.inicia_conexao()

@app.get("/rec/v1")
def rota_padrao():
    return {"Rota Padrão":"Voce acessou o endpoint default."}

@app.get("/rec/v2/{usuario}")
def consulta_rec(usuario: int):
    return {"usuario": usuario, "resultado recomendacao": mongo.consulta_recomendacao(usuario, conexao)}

@app.get("/rec/v3")
def gerar_recomendacao():
# Gerar recomendações para 50 usuários
    usuarios_recomendacoes = mongo.gerar_recomendacoes_para_usuarios(conexao, 50)

# Criar uma lista para armazenar as recomendações
    recomendacoes = []

# Exibir as recomendações para cada usuário
    for usuario_id, recomendacao in usuarios_recomendacoes.items():
        recomendacoes.append(f"Recomendações para o usuário {usuario_id}: {recomendacao}")

    return {f"recomendacoes": recomendacoes}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port="8000")