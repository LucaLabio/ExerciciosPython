"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."""
letras = []
consoantes = 0
help = 0
vogal = ["A","E","I","O","U"]
for i in range(0,10,1):
    letras.append(input("Digite uma letra").upper())
    print(letras[i])
    while len(letras[i]) >= 2:
        letras[i] = input("Digite somento UMA letra sua anta").upper()
        print(letras[i])
    for x in range(0,4,1):
        print(vogal[x])
        if letras[i] != vogal[x]:
            help = help + 1
            print(help)
            if help == 4:
                print(letras[i])
    help = 0