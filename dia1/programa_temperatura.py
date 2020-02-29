"""O usuário digita a temperatura em graus
Célsius e o programa exibe o valor em graus Fahrenheit. """
celsius = float(input("digite a temperatura em graus celsius"))
fahre = (celsius * 9/5) + 32
print("Convertendo de celsius para fahrenheit fica ", fahre, "°F")