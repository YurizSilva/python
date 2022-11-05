import itertools

vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    vetor1.append(int(input("insira numeros inteiros para preencher a primeira lista: ")))
for i in range(10):
    vetor2.append(int(input("insira numeros inteiros para preencher a segunda lista: ")))

vetor3 = list(itertools.chain(*zip(vetor1, vetor2)))

print("primeira lista", vetor1)
print("segunda lista", vetor2)
print("terceira lista", vetor3)
