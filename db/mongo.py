from pymongo import MongoClient
import os

##host = os.getenv("host")
##port = os.getenv("port")

def inicia_conexao():
    client = MongoClient("localhost", 27017)
    db = client['rec']
    col = db['recomendacao']
    return col

##print(list(col.find({"userId": 10})))

def consulta_recomendacao(usuario, conexao):
    
    recomendacoes = list(conexao.find({"userId":usuario}))
    list_rec = []
    for rec in recomendacoes:
        list_rec.append((rec["movieId"], rec["rating"]))
    return {"Recomendacoes": list_rec}

def gerar_recomendacoes_para_usuarios(conexao, num_usuarios=50):
    # Gerar recomendações para os 50 usuários
    todas_recomendacoes = {}
    for usuario_id in range(0, num_usuarios + 1):  # Iterar de 1 a 50 para gerar recomendações para cada um
        recomendacao = consulta_recomendacao(usuario_id, conexao)
        
        if recomendacao["Recomendacoes"]:  # Verificar se há recomendações para esse usuário
            todas_recomendacoes[usuario_id] = recomendacao["Recomendacoes"]
        else:
            todas_recomendacoes[usuario_id] = []  # Caso não haja recomendações, armazena uma lista vazia
    
    return todas_recomendacoes


