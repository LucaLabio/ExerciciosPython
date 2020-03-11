"""O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5.
Dica: realize várias divisões e restos de divisões por 10."""
rm = int(input("Digite o rm do aluno: "))
n1 = int(rm/10000)
print(str(n1))
n2 = int((rm / 1000) - (n1 * 10))
print(str(n2))
n3 = int((rm / 100) - (n2 * 10 + n1 *100))
print(str(n3))
n4 = int((rm / 10) - (n3 * 10 + n2 * 100 + n1 *1000))
print(str(n4))
n5 = rm - int((n4 * 10 + n3 * 100 + n2 * 1000 + n1 *10000))
print(str(n5))
soma = n1 + n2 + n3 +n4 + n5
print("A soma de cada digito é: " , n1, " + ", n2, " + ", n3, " + ", n4, " + ", n5, " = ", soma)