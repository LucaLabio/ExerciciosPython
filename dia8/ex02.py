def funcao():
    num = int(input('Digite um numero: '))
    seq = []
    for x in range(0,num,1):
        seq.append(num)
        print(seq)
funcao()
def funcao(num):
    seq = []
    for x in range(0,num,1):
        seq.append(num)
        print(seq)
funcao(int(input('Digite um numero: ')))