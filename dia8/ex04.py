"""A empresa WYZ decidiu dar uma gratificação de Natal a seus funcionários, baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho. O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:h = número de horas extras - (2/3*(número de horas extras - número de horas que o funcionário faltou))"""
trabalhadas = int(input("Digite a quantidade de horas trabalhadas"))
extras = int(input("Digite a quantidade de horas extras trabalhadas"))
falta = int(input("Digite a quantidade de horas trabalhadas nas quais voce faltou"))
h = extras - (2/3*(extras - falta))
h = h * 60
premio = 0
if h > 2400:
    premio = 1500
elif h >= 1800 or h <= 2399:
    premio = 1000
elif h >= 1200 or h <= 1799:
    premio = 890
else:
    premio = 500
print("O seu valor de premio eh R$", premio , " parabens")