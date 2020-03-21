nome=input("Digite seu nome")
idade=int(input("Digite sua idade"))
doenca_contagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
while doenca_contagiosa != "SIM" and doenca_contagiosa != "NAO":
    print("Responda com SIM ou NAO")
    doenca_contagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
# PRIMEIRO PROBLEMA A SER RESOLVIDO
if  doenca_contagiosa=="SIM":
    print("Encaminhe o paciente para a sala AMARELA")
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