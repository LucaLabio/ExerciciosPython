"""A nota final de um estudante é calculada a partir de três notas atribuídas,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a
um exame final. A média das três notas mencionadas obedece aos pesos a
seguir:
Trabalho de Laboratório - peso 2
Avaliação Semestral - peso 3
Exame final - peso 5
Faça um programa em Python que receba as três notas, calcule e mostre a
média ponderada e o conceito conforme tabela:
Média Ponderada
de 8,0 a 10,0 - Conceito A
de 7,0 a 7,9 - Conceito B
de 6,0 a 6,9 - Conceito C
de 5,0 a 5,9 - Conceito D
de 0,0 a 4,9 - Conceito E"""

laboratorio = int(input("Digite sua nota de trabalho de laboratorio"))
avaliacao = int(input("Digite sua nota de avaliacao"))
exame = int(input("Digite sua nota de exame"))
media = ((laboratorio * 2) + (avaliacao * 3) + (exame * 5))/10
if media >= 8:
    print("Conceito A ",media )
elif media >= 7 and media <= 7.9:
    print("Conceito B ",media)
elif media >= 6 and media <= 6.9:
    print("Conceito C ",media)
elif media >= 5 and media <= 5.9:
    print("Conceito D ",media)
else:
    print("Conceito E ",media)