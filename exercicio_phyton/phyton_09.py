#9) Verificar se um número é múltiplo de outro:

# Obtenha os números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verifica se o primeiro número é múltiplo do segundo
if numero1 % numero2 == 0:
    print('O primeiro número é múltiplo do segundo')
else:
    print('O primeiro número não é múltiplo do segundo')
