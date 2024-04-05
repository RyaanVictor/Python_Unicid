
#(7) Verificar se um número é um quadrado perfeito:
# Obtenha o número
n = int(input("Digite um número: "))

# Calcula a raiz quadrada do número
raiz = n ** 0.5

# Verifica se a raiz é um número inteiro
if raiz == int(raiz):
    print('O número é um quadrado perfeito')
else:
    print('O número não é um quadrado perfeito')
