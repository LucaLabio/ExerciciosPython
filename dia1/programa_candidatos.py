"""Pergunte a quantidade de votos de 3 candidatos, dos votos brancos e nulos, mostre o total de votos e o percentual de votos
em cada um"""
candiA = int(input("Digite quantas pessoas votaram no candidato A"))
candiB = int(input("Digite quantas pessoas votaram no candidato B"))
candiC = int(input("Digite quantas pessoas votaram no candidato C"))
branco = int(input("Digite quantas pessoas votaram em branco"))
nulo = int(input("Digite quantas pessoas votaram nulo"))
total = candiA+candiB+candiC+branco+nulo
percentualA = round(100*candiA/total,2)
percentualB = round(100*candiB/total,2)
percentualC = round(100*candiC/total,2)
percentualBR = round(100*branco/total,2)
percentualN = round(100*nulo/total,2)
print("o total de votos foi ", total, "sendo ", percentualA, "% no candidato A, ", percentualB, "% no candidato B, ", percentualC, "% no candidato C, ", percentualBR, "% votaram em branco e ", percentualN, "% votaram nulo")