nota1 = int(input("Nota do aluno do primeiro bimestre: "))
if nota1 > 25:
    print("valor invalido")

nota2 = int(input("Nota do aluno no segundo bimestre: "))
if nota2 > 25:
    print("valor invalido")

nota3 = int(input("Nota do aluno no terceiro bimestre: "))
if 25 < nota3:
    print("valor invalido")

nota4 = int(input("Nota do aluno no quarto bimestre: "))
if 25 < nota4:
    print("valor invalido")

total = nota1 + nota2 + nota3 + nota4
print("total do ano letivo:", total)

if int(60 <= total < 100):
    print("Aprovado")
if int(total <= 40):
    print("Reprovado")
if int(40 < total < 60):
    print("Recuperação")
if int(total > 101):
    print("total invalido")
