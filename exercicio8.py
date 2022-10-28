final = "S"
while final == "S":

    num1 = float(input("Digite o primeiro numero inteiro: "))
    num2 = float(input("Digite o segundo numero inteiro: "))

    resultado1 = num1 + num2
    print("resultado da soma dos dois numeros é: ", resultado1)

    resultado2 = num1 - num2
    print("resultado da subtratação dois numeros é: ", resultado2)

    resultado3 = num1 / num2
    print("resultado da divisão dois numeros é: ", resultado3)

    resultado4 = num1 % num2
    print("resto da divisão dos dois numeros é: ", resultado4)

    resultado5 = num1 ** num2
    print("resultado da potencia dos dois numeros é: ", resultado5)

    resultado = num1 * num2
    print("resultado da multiplicação dos dois numeros é: ", resultado)

    final = input("se quiser continuar digite S se não quiser digite N: ",).upper()
