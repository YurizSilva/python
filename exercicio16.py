def repetição():
    for i in range(n - 1, nlinha):
        i += 1
        print(str(i) * i)


n = int(input("Digite um numero para começar: "))
nlinha = int(input("ate quanto o numero deve ir: "))
repetição()
