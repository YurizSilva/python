valor = float(input("digite o valor de horas trabalhadas: "))
horas = float(input("digite o numero de horas trabalhadas no mês: "))

salarioBruto = valor * horas
inss = salarioBruto * 0.08
inpostorenda = salarioBruto * 0.11
sindicato = salarioBruto * 0.05
salarioliquido = salarioBruto - inss - inpostorenda - sindicato

print("seu salario bruto é: ", salarioBruto)
print("desconto inss: ", inss)
print("desconto impostode renda: ", inpostorenda)
print("desconto sindicato: ", sindicato)
print("salario liquido: ", salarioliquido)
