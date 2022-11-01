lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    lista[i] = str(input("Insira o caractere: "))
print("Lista de caracteres: ", lista)

def conta_consoante(lista):
    soma = 0
    for i in lista:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o'or i == 'u':
                continue
            else:
                soma += 1
    print("Soma de consoantes: ", soma)
    return soma

conta_consoante(lista)
