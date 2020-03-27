"""Usando o “for”,tente montar um código que exiba a tabuada de um valor que será    digitado    pelo    usuário    final"""
numero = int(input("digite um número no qual você gostaria de ver a tabuada"))
for i in range (1,11,1):
    tabuada = numero * i
    print("\t" + str(numero) + " Multiplicado por " + str(i) + " é igual a " + str(tabuada))