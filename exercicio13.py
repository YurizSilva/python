lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(20):
    lista[i] = str(input("Insira os nomes dos estudantes inscritos na prova do ENEM: "))

lista.sort()
print("Lista de nomes em ordem: ", lista)
