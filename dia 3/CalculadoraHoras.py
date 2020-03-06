"""Calculadora de horario"""
numero = int(input("Digite a quantidade de horarios que sera calculada "))
hora = []
minuto = []
segundo = []
horas = 0
minutos = 0
segundos = 0
#Fazendo a conta
for i in range (0,numero,1):
    hora.append(int(input("Digite as horas do " + str(i+1) + "° horario a serem somados ")))
    minuto.append(int(input("Digite os minutos do " + str(i+1) + "° horario a serem somados ")))
    segundo.append(int(input("Digite os segundos do " + str(i+1) + "° horario a serem somados ")))
    horas = horas + hora[i]
    minutos = minutos + minuto[i]
    segundos = segundos + segundo[i]
#Convertendo segundos
while segundos >= 60:
    segundos = segundos - 60
    minutos = minutos + 1
#Convertendo minutos
while minutos >= 60:
    minutos = minutos - 60
    horas = horas + 1
print("A soma total de horas foi: " + str(horas))
print("A soma total de minutos foi: " + str(minutos))
print("A soma total de segundos foi: " + str(segundos))
