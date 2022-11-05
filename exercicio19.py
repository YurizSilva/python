valor = float(input("valor do produto: "))
for i in range(1, 51):
    n = valor * i
    n_formatado = "{:.2f}".format(n)
    print("Tabela de preços",i,"- R$",n_formatado)
