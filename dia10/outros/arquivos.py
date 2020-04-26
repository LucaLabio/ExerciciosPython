basedados = []
with open("iris.data", "r") as arquivos:
    for registro in arquivos.readlines():
        basedados.append(registro.split(","))
print(basedados)
print(float(basedados[0][0]) + float(basedados[0][1]))