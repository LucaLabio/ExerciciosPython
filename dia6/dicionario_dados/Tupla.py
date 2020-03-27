ips={}
resp="S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois ultimos octetos: "))]=input("Nome da maquina: ")
    resp=input("Digite <S> para continuar: ").upper()
print("exibindo ips")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])
print("Exibindo maquinas com mesmo endereco")
pesquisa = input("Digite os dois ultimos octetos")
for ip,nome in ips.items():
    print("MAquinas no mesmo endereco (redes diferentes")
    if(ip[1] == pesquisa):
        print(nome)
print("Exibindo maquinas que compoem a mesma rede")
rede = input("Digite os dois primeiros octetos")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)