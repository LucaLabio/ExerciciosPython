# import platform
import getpass
# from datetime import datetime

# print("Nome maquina:...............", platform.node())
# print("Arquitetura:................", platform.architecture())
# print("Sistema Operacional:........", platform.system())
# print("Versao do SO:...............", platform.release())
# print("Processador:................", platform.processor())
# print("Versao do python:...........", platform.python_version())
#
#
# print(datetime.now().year)
usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == "lucal" and senha == "hello":
    print("bem vindo")
else:
    print("Voce n tem acesso")