"""Faça um programa em Python que:
a) Receba do usuário os dados de um produto específico:
- Preço unitário
- País de origem (1-Brasil, 2-México,3-Outros)
- Meio de Transporte (T-Terrestre, F-Fluvial, A-Aéreo)
- Carga Perigosa (S-Sim, N-Não)
b) O algoritmo deve calcular:
- Valor do Imposto
- Valor do Transporte
- Valor do Seguro
Regras para cálculo:
Valor do Imposto
Preço Unitário
Percentual de Imposto sobre o
preço unitário
Até R$ 100,00 5%
Maior que R$ 100,00 20%
Valor do Transporte
Carga Perigosa País de Origem Valor do Transporte
S 1 R$21,00
 S 2 R$27,00
S 3 R$50,00
N 1 R$21,00
 N 2 R$25,00
N 3 R$40,00
1/2
Desvio Simples e Composto
Valor do Seguro: Os produtos que vem do México e os produtos que utilizam transporte aéreo
pagam metade do valor do seu preço unitário como seguro. Os demais produtos não pagam
seguro.
c) Mostrar na tela: (1.5)
Preço final (preço unitário + impostos + valor do transporte + seguro. """
preco = float(input("Digite o preço unitario do produto: "))
pais = int(input("Digite o numero do páis de origem (1-Brasil, 2- México, 3-Outros): "))
transporte = input("Digite o meio de transporte (T-Terrestre, F-Fluvial, A-Aereo): ")
perigosa = input("A carga é perigosa? (S-Sim, N-Não): ")
#imposto
if preco <= 100:
    imposto = preco * 0.05
else:
    imposto = preco * 0.2
#transporte
if perigosa == "S":
    if pais == 1:
        valorTransporte = 21
    elif pais == 2:
        valorTransporte = 27
    else:
        valorTransporte = 50
else:
    if pais == 1:
        valorTransporte = 21
    elif pais == 2:
        valorTransporte = 25
    else:
        valorTransporte = 40
#Valor do Seguro
if pais == 2 or transporte == "A":
    seguro = preco / 2
else:
    seguro = 0
total = preco + imposto + valorTransporte + seguro
print("O preço total a ser pago é de R$" + str(total))