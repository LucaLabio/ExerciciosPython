import json
# with open("bd.json", "r") as arq_json:
#     dic = json.load(arq_json)
#     for chave,dados in dic.items():
#         print(chave + " " + str(dados))
dicionario = {
  "CHAVES": ["CHAVES DO 8","14/04/2020","RECEP01"],
  "QUICO" : ["QUICO FLORES", "17/09/2020", "FINANC03"],
  "FLORINDA":["DONA FLORINDA", "21/02/2020", "ESCRI07"]
}
with open("bd1.json", "w") as json_file:
    json.dump(dicionario,json_file)