# 3) Calcular as raízes de uma equação quadrática
# Obtenha os valores
a = float(input("Digite o valor de a: ")) b = float(input("Digite o valor de b: ")) c = float(input("Digite o valor de c: "))
# Calcula o delta delta = b**2 - 4*a*c
# Verifica se o delta é negativo if delta < 0:
print('Delta negativo.') else:
# Calcula e imprime as raízes
x1 = (-b + (delta ** 0.5)) / (2*a) x2 = (-b - (delta ** 0.5)) / (2*a) print('As raízes são:', x1, 'e', x2)
