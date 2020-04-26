"""6) Faça um programa em Python que leia 50 idades e mostre na tela a media simples das idades digitadas. Observações: -Não aceitar idade < 0-Necessariamente precisa ter 50 idades válidas"""
total = 0
for i in range(0,50,1):
    idade = int(input("Digite uma idade"))
    while idade < 0:
        idade = int(input("Digite uma idade valida"))
    total += idade
print("a media de idade eh:", total/50)