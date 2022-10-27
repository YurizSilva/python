iphone = int(2980)
samsung = int(2540)
tablet = int(1950)
ps5 = int(2100)
notebook = int(2350)

Qtde1 = int(input("coloque quantos iphone você deseja: ",))
valor1 = Qtde1 * iphone
print ("valor total dos iphone: ", valor1)

Qtde2 = int(input("coloque quantos samsungs você deseja: ",))
valor2 = Qtde2 * samsung
print ("valor total dos samsungs: ", valor2)

Qtde3 = int(input("coloque quantos tablet você deseja: ",))
valor3 = Qtde3 * tablet
print ("valor total dos tablet: ", valor3)

Qtde4 = int(input("coloque quantos ps5 você deseja: ",))
valor4 = Qtde4 * ps5
print ("valor total dos ps5: ", valor4)

Qtde5 = int(input("coloque quantos notebook você deseja: ",))
valor5 = Qtde5 * notebook
print ("valor total dos notebook: ", valor5)

total = valor1 + valor2 + valor3 + valor4 + valor5
print ("total da compra", total)

parcela = total / 3
print ("Total da compra parcelada em 3X sem juros: ", parcela)

parcela2 = (total / 6) + (0.05 * total)
print ("valor da parcela dividido em 6X com acréscimo de 5%: ", parcela2)

Desconto = total * 0.1
print ("valor com 10% de desconto para pagamento à vista: ", Desconto - total)
