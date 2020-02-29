"""O usuário informa o valor do seu
salário e suas despesas mensais. O programa calcula o valor que
sobra e diz quanto tempo (em anos) será necessário poupar para
se tornar milionário."""
salario = float(input("informe seu salario"))
despesas = float(input("digite o total de suas despesas mensais"))
sobra = salario - despesas
anos = 1000000 / sobra
print("você ira demorar um total de ", anos, "para se tornar milionario")