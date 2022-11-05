def fatorial(n):
   if n == 1:
       return n
   else:
       return n*fatorial(n-1)


num = int(input("qual numero voce deseja ver o fatorial? "))

if num < 0:
   print("desculpa, fatorial não pode ser mostrado por ser um numero negativo")
elif num == 0:
   print("o fatorial de 0 é 1")
else:
   print("o fatorial de", num, "é", fatorial(num))
