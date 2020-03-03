"""o seu módulo solicitaráo nível de acesso de uma pessoa que pode ser: ADM, USR ouGUEST e o gênero dessa pessoa, caso o"""
"""nível seja  ADM,  ele  deverá  exibir  “Olá  administrador”  para  os  homens  ou  “Olá administradora” para as"""
"""mulheres. Se o nível for USR, deverá exibir “Olá usuário” para  os  homens  ou  “Olá  usuária”  para  as  mulheres."""
"""Se o  nível  for  GUEST,a mensagem deverá ser “Olá visitante”. E se  o  nível  digitado  for  diferente  de  ADM, USR"""
"""ou GUEST  deverá  exibir  a  mensagem  “Olá  desconhecido(a)”. Considere apenas os gêneros masculino e feminino"""
nivelacesso = input("Digite o seu nível de acesso (ADM para administrador - USR para usuario - GUEST para convidado:").upper()
sexo = input("Digite o seu sexo (Utilize [F] para feminino e [M] para masculino ").upper()
if nivelacesso == "ADM":
    if sexo == "M":
        print("Ola administrador")
    elif sexo == "F":
        print("Ola administradora")
    else:
        print("Você digitou algum valor incorretamente")
elif nivelacesso == "USR":
    if sexo == "M":
        print("Ola administrador")
    elif sexo == "F":
        print("Ola administradora")
    else:
        print("Você digitou algum valor incorretamente")
elif nivelacesso == "GUEST":
    if sexo == "M":
        print("Ola administrador")
    elif sexo == "F":
        print("Ola administradora")
    else:
        print("Você digitou algum valor incorretamente")
else:
    print("Você digitou algum valor incorretamente")