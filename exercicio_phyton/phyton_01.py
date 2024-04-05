#1) triangulos 

def calculararea(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def verificartriangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("É um triangulo equilatero.")
        elif a == b or a == c or b == c:
            print("É um triangulo isosceles.")
        else:
            print("É um triangulo escaleno")
        area = calculararea(a, b, c)
        print("A area do triangulo é:", area)
    else:
        print("Os valores näo formam um  triangulo.")

#obtendo os valores dos lados

a = int(input("Digite o valor do primeiro lado do triangulo: "))
b = int(input("Digite o valor do segundo lado do triangulo: "))
c = int(input("Digite o valor do terceiro lado do triangulo: "))

#verificando
verificartriangulo(a, b, c)

