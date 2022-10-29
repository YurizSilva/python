nota1 = float(input("Nota do aluno do primeiro bimestre: "))
if nota1 > 25:
    print("valor invalido")
    exit("cancelando")

nota2 = float(input("Nota do aluno no segundo bimestre: "))
if nota2 > 25:
    print("valor invalido")
    exit("cancelando")

nota3 = float(input("Nota do aluno no terceiro bimestre: "))
if 25 < nota3:
    print("valor invalido")
    exit("cancelando")

nota4 = float(input("Nota do aluno no quarto bimestre: "))
if 25 < nota4:
    print("valor invalido")
    exit("cancelando")

total = nota1 + nota2 + nota3 + nota4
print("total do ano letivo:", total)

if float(60 <= total < 100):
    print("Aprovado")
if float(total <= 40):
    print("Reprovado")
if float(40 < total < 60):
    print("Recuperação")
if float(total > 101):
    print("total invalido")
