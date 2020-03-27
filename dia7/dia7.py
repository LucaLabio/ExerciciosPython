"""Criar um programa para implementar o jogo de adivinhação. Um
número será sorteado aleatoriamente entre uma sequência de 0 a
100.
 O usuário digitará números até que o número sorteado seja
informado.
 Durante as tentativas do usuário o computador deverá retornar
“Maior” se o número informado for menor que o sorteado e retornar
“Menor” se o número sorteado for maior que o sorteado.
 Um contador de quantas tentativas foram realizadas deverá ser
exibido a cada tentativa."""
import random
sorteado = random.randint(0,101)
numero = int(input("Digite um numero "))
tentativas = 0
while numero != sorteado:
    if numero > sorteado:
        print("Voce digitou um numero maior que o sorteado")
    else:
        print("Voce digitou um numero menor que o sorteado")
    tentativas = tentativas + 1
    numero= int(input("Digite um numero"))

print("Voce acertou que o numero sorteado era ", numero, " e precisou de ", tentativas, " tentativas")