""" todos os equipamentos “impressora” receberão uma depreciação (desvalorização após certo período) de 10%. Monte o código que seria responsável por alterar o valor de todos os equipamentos “impressora”.
 todos os equipamentos “impressora” receberão uma depreciação (desvalorização após certo período) de 10%. Monte o código que seria responsável por alterar o valor de todos os equipamentos “impressora”.
"""
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

depreciacao = input("\nDigite o nome do equipamento que sera depreciado: ")
for i in range(0,len(equipamentos)):
    if depreciacao == equipamentos[i]:
        print("O valor antigo era R$", valores[i])
        valores[i] = valores[i] * 0.9
        print("Novo valor é R$", valores[i])