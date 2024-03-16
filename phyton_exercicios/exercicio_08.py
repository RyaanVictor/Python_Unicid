#Exercicio 08
horaInicio = int(input("Hora de início:"))
minInicio = int(input("E quantos minutos:"))
horaFim = int(input("Hora de término:"))
minFim= int(input("E quantos minutos:"))

minutosDoInicio = horaInicio * 60 + minInicio
minutosDoFim = horaFim * 60 + minFim
minDuracao = minutosDoFim - minutosDoInicio
horasDuracao = minDuracao // 60
minDuracao = minDuracao - horasDuracao * 60

print(f"A partida levou")
print(f"{horasDuracao}:{minDuracao}")
