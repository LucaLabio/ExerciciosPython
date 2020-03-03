nome=input("Digite seu nome")
idade=int(input("Digite sua idade"))
doenca_contagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
"""Sala branca: pacientes sem risco de doença"""
"""Sala amarela: com risco de doença"""
"""DIVIDINDO O PROBLEMA EM DOIS PEDAÇOS"""
# PRIMEIRO PROBLEMA A SER RESOLVIDO
if  doenca_contagiosa=="SIM":
    print("Encaminhe o paciente para a sala AMARELA")
elif doenca_contagiosa=="NAO" or doenca_contagiosa=="NÃO":
    print("Encaminhe o paciente para a sala BRANCA")
else:
    print("Você digitou alguma das informações incorretamente")

#SEGUNDO PROBLEMA A SER RESOLVIDO
"""CONSIDERANDO A PRIORIDADE DA GRAVIDEZ"""
if  idade>= 65:
    print("Paciente COM PRIORIDADE")
else:
    genero=input("Digite o gênero do paciente (Utilizando apenas [F]eminino ou [M]asculino): ").upper()
    if genero=="" and idade > 10:
        gravidez=input("A paciente esta gravida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")