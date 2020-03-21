""" Uma instituição bancária utiliza um dígito verificador
para validar o número da conta (com 3 dígitos) de seus
clientes. Faça um programa em Python que solicite o
número da conta e calcule o dígito verificador. Os
passos para calcular o dígito verificador são:
Ex: Número da conta = 235.
1) somar o número da conta com o seu inverso. Ex: 235 + 532 = 767
2) Multiplicar cada digito do número obtido no passo anterior pela sua
ordem posicional e somar esses resultados. O último digito do número
obtido é o dígito verificador.
– Ex: 7 x 1 + 6 x 2 + 7 x 3 = 40 (dígito verificador ! 0).
• PS: Use o operador % e a divisão inteira para obter o dígito verificador. """
nconta = int(input("Digite o numero da conta: "))
n1 = int(nconta / 100)
n2 = int((nconta - (n1*100))/10)
n3 = int(nconta - (n1*100 + n2*10))
inverso = int((n3*100) + (n2*10) + n1)
soma = nconta + inverso
multiplicacao = n1 * 1 + n2 * 2 + n3 * 3
verificador = int(multiplicacao / 10)
verificador = multiplicacao - verificador*10
print("O seu Digito verificador e: " + str(verificador))
print(n1)
print(n2)
print(n3)
print(inverso)
print(soma)
print(multiplicacao)
print(verificador)