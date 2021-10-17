nome = input("").lower().strip()
numero = int(input(""))
if numero == 1:
    nomes = input("").lower().strip()
    caracteres = len(nome)
    caracter = len(nomes)
    print(caracteres + caracter)
elif numero == 2:
    caracteres = len(nome)
    print(caracteres)
else:
    print("Digite o que se pede")
