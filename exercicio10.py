#notap1 = nota Prova
#notat1 = nota traabalho

notap1 = float(input("Nota da prova do aluno do primeiro bimestre: "))
notat1 = float(input("Nota do trabalho do aluno do primeiro bimestre: "))
total1 = notap1 + notat1
if total1 > 25:
    print("valor invalido")
    exit("cancelando")

notap2 = float(input("Nota da prova do aluno no segundo bimestre: "))
notat2 = float(input("Nota do trabalho do aluno do segundo bimestre: "))
total2 = notap2 + notat2
if total2 > 25:
    print("valor invalido")
    exit("cancelando")

notap3 = float(input("Nota da prova do aluno no terceiro bimestre: "))
notat3 = float(input("Nota do trabalho do aluno do terceiro bimestre: "))
total3 = notap3 + notat3
if total3 > 25:
    print("valor invalido")
    exit("cancelando")

notap4 = float(input("Nota da prova do aluno no quarto bimestre: "))
notat4 = float(input("Nota do trabalho do aluno do quarto bimestre: "))
total4 = notap4 + notat4
if total4 > 25:
    print("valor invalido")
    exit("cancelando")

print("media no primeiro bimestre:", total1/2)
print("media no segundo bimestre:", total2/2)
print("media no terceiro bimestre:", total3/2)
print("media no quarto bimestre:", total4/2)

total = total1 + total2 + total3 + total4

print("total do ano letivo:", total)

if float(60 <= total < 100):
    print("Aprovado")
if float(total <= 40):
    print("Reprovado")
if float(40 < total < 60):
    print("Recuperação")
if float(total > 101):
    print("total invalido")
