
def fibbonacci(meses):
    if meses > 0 and meses < 3:
        return 1
    else:
        return fibbonacci(meses - 1) + fibbonacci(meses-2)


meses = int(input("quantos meses os coelhos vão ficar juntos? "))
for i in range(meses+1):
    casal = fibbonacci(i+1)
    print("O numero total de casais no mês",i + 1,"é: ", casal)
