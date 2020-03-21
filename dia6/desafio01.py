"""Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""
lista = []
achar = int(input("Digite um numero"))
adicionar = input("Deseja adicionar um numero no array? S ou N").upper()
preencher = 0
while adicionar != "N" and adicionar != "S":
    adicionar = input("Deseja adicionar um numero no array? S ou N").upper()
while adicionar == "S":
    lista.append(int(input("Digite o numero que quer adicinar")))
    adicionar = input("Deseja adicionar um numero no array? S ou N").upper()
    while adicionar != "N" and adicionar != "S":
        adicionar = input("Deseja adicionar um numero no array? S ou N").upper()
for numero in range(len(lista)):
    for i in range(len(lista)):
        resultado = lista[numero] + lista[i]
        if resultado == achar:
            final = lista[numero], " + ", lista[i], " = ", resultado
            preencher = 1
            break
    if preencher == 1:
        break
if preencher == 1:
    print("Encontramos dois numeros que somados resultam no seu numero citado")
    print("o calculo deles e " + str(final))
if preencher == 0:
    print("Nao encontrei dois numeros no qual sua soma resulta no seu numero citado")