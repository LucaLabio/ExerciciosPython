nome=input("Digite seu nome")
idade=int(input("Digite sua idade"))
doenca_contagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
"""Sala branca: pacientes sem risco de doença"""
"""Sala amarela: com risco de doença"""
if idade>=65:
    print("O paciente " + nome + " POSSUI prioridade")
    if doenca_contagiosa=="SIM":
        print("O encaminhe para a sala AMARELA")
    elif doenca_contagiosa=="NAO" or doenca_contagiosa=="NÃO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Você digitou alguma das informações incorretamente")
else:
    print("Paciente sem prioridade")
    if doenca_contagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca_contagiosa=="NAO" or doenca_contagiosa=="NÃO" :
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Você digitou alguma das informações incorretamente")