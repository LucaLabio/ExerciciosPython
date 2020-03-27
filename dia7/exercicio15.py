""" Faça um algoritmo em Python para ler o nome, as três notas e o número de
faltas de um aluno e escrever qual a sua situação final: Aprovado, Reprovado
por Falta ou Reprovado por Média.
A média para aprovação é 7,0 e o limite de faltas é 25% do total de aulas. O
número de aulas ministradas no semestre foi 80. A reprovação por falta
sobrepõe a reprovação por Média."""
laboratorio = float(input("Digite sua nota de trabalho de laboratorio"))
avaliacao = float(input("Digite sua nota de avaliacao"))
exame = float(input("Digite sua nota de exame"))
faltas = int(input("Digite sua quantidade de faltas"))
porcentagemfaltas = (100 * faltas) / 80
media = ((laboratorio * 2) + (avaliacao * 3) + (exame * 5))/10
if media >= 7:
    if porcentagemfaltas <= 25:
        print("Aprovado")
    else:
        print("Reprovado por falta")
else:
    (print("Reprovado por media"))