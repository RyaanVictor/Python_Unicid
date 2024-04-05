#6) Determine quantos dias um mês possui:

# Obtenha o mês
mes = int(input("Digite um número entre 1 e 12: "))

# Cria uma lista com a quantidade de dias de cada mês
diasdomes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Verifica se o mês está dentro do intervalo válido
if 1 <= mes <= 12:
    print('O mês tem', diasdomes[mes - 1], 'dias')
else:
    print('Número inválido')
