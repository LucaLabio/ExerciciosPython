"""Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão."""
n1 = int(input("Digite um numero inteiro de 0 a 99 "))
while n1 > 99 or n1 < 0:
    n1 = int(input("Digite um numero inteiro de 0 a 99 "))
if n1 >=10:
    conversao = n1/10
    dezena = int(conversao)
    unidade = n1 - (dezena*10)
    print("A casa da dezena é " + str(dezena) + " e a casa da unidade é " + str(unidade))
else:
    print("A casa da dezena é 0 e a casa da unidade é " + str(n1))