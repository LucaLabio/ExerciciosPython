"""Utilizando a tabela de valores abaixo, faça um algoritmo para o ESTACIONAMENTO SEMPRE BEM-VINDO
que seja capaz de mostrar na tela, o valor que o cliente deve pagar pelo tempo que seu veículo ficou
estacionado.
Tabela de Valores -Estacionamento SEMPRE BEM-VINDO
Tempo de permanência (em minutos)
até 15 minutos de 16 a 180 minutos acima de 180 minutos
Moto Grátis R$17,00 + 0,10 por minuto adicional
Carro Grátis R$20,00 + 0,15 por minuto adicional
Exemplo: O cliente deixou estacionado sua moto por 204 minutos, então ele deve pagar R$ 19,40 (R$ 17,00
+ R$ 2,40)."""
tempo = int(input("Digite quanto tempo (em minutos) você deixou seu carro estacionado"))
veiculo = input("Digite se você estacionou um carro ou uma moto").upper()
while veiculo != "MOTO" and veiculo != "CARRO":
    veiculo = input("Digite se você estacionou um carro ou uma moto").upper()
if tempo <= 15:
    custo = 0
elif tempo >=16 and tempo <= 180:
    if veiculo == "MOTO":
        custo = 17
    else:
        custo = 20
else:
    extra = tempo - 180
    if veiculo == "MOTO":
        custo = 17 + (extra*0.10)
    else:
        custo = 20 + (extra*0.10)
print("Você deixou seu carro estacionado por " + str(tempo) + " minutos totalizando um custo de R$" + str(custo))