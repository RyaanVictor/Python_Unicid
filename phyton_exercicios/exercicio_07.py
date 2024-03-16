#Exercicio 07
eleitores = int(input("Quantos eleitores?"))
brancos = int(input("Quantos em branco?"))
nulos = int(input("Quantos nulos?"))

validos = eleitores - (brancos + nulos)
porcValidos = validos * 100 / eleitores
porcOutros = 100 - porcValidos

print(f"Porcentagem válidos: {porcValidos}%")
print(f"Porcentagem brancos/nulos {porcOutros}%")
