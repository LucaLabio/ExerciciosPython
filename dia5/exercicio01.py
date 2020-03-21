"""A prefeitura de Recife criou um programa de
empréstimo para seus funcionários com desconto em
folha. O valor da prestação não pode ultrapassar 30%
do salário bruto do funcionário. Faça um programa em
Python que solicite o valor do salário bruto, o valor da
prestação e informe se o empréstimo pode ou não ser
concedido. """
salario = float(input("Digite o valor do seu salário bruto: "))
prestacao = float(input("Digite o valor da prestacao"))
possibilidade = int(prestacao/salario * 100)
print(possibilidade)
if possibilidade > 30:
    print("O valor da prestação é superior a 30% do seu salario bruto, portanto não pode ser concedido, atual porcentagem é: " + str(possibilidade))
else:
    print("o valor da prestação é inferior a 30% do seu salario bruto portanto sera concedido")