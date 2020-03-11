"""Usain Bolt é o recordista mundial dos 100 metros rasos com o tempo de 9,58 segundos.
Escreva um algoritmo que calcula a velocidade média em m/s e em km/h de um corredor,
seu algoritmo recebe como dados de entrada a distância em metros e o tempo em segundos."""
metros = float(input("Digite a distancia percorrida em metros"))
tempo = float(input("Digite o tempo percorrido em segundos"))
mediaMS = metros/tempo
print("A media de m/s é " + str(mediaMS))
mediaKMH = mediaMS * 3.6
print("A media de KM/H é " + str(mediaKMH))