nome=input("Digite seu nome")
idade=int(input("Digite sua idade"))
doenca_contagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
"""tudo que for digitado na função upper sera convertido para uma string com letras maiúsculas"""
"""Sala branca: pacientes sem risco de doença"""
"""Sala amarela: com risco de doença"""
if idade>=65 and doenca_contagiosa=="SIM":
    print("O paciente " + nome + " Sera direcionado para a sala AMARELA - COM prioridade")
elif idade < 65 and doenca_contagiosa=="SIM":
    print("O paciente " + nome + " Sera direcionado para a sala AMARELA - SEM prioridade")
elif idade >= 65 and (doenca_contagiosa=="NAO" or doenca_contagiosa=="NÃO"):
    print("O paciente " + nome + " sera direcionado para a sala BRANCA - COM prioridade")
elif idade < 65 and (doenca_contagiosa == "NAO" or doenca_contagiosa=="NÃO"):
    print("O paciente " + nome + " sera direcionado para a sala BRANCA - SEM prioridade")
else:
    print("Você digitou alguima das informações incorretamente")


