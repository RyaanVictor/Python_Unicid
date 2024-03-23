idade = 2024 - int(input("Em que ano você nasceu: "))
print(f" Você tem {idade} anos: ")
if (idade < 16 ):
    print("Você é obrigado a votar")
elif (idade <= 16 < 18 or idade >= 65):
    print("Você tem voto facultativo")
else:print("Você é obrigado as votar")

