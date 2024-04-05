#(5) Associar um número a um dia da semana
    
# Obtenha o número da semana
dia = int(input("Digite um número entre 1 e 7: "))

# Cria uma lista com os dias da semana
diasdasemana = ['Domingo','Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

# Verifica se o número está dentro do intervalo
if 1 <= dia <= 7:
# Imprime o dia da semana correspondente
    print('O dia da semana é:', diasdasemana[dia - 1])
else:
    print('Número inválido')
