"""Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. Seu
algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o m
de 2020. Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu
programa deverá imprimir:
Fulano de tal tem (ou terá) 34 anos"""

nome = input("Digite seu nome: ")
ano = int(input("Digite o ano de seu nascimento: "))
idade = 2020 - ano
print("Seu nome é " + nome + " e você tera " + str(idade) + " anos até o final do ano")