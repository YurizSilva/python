#print {matriz}

M = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]
msg = False
for i in range(5):
    for j in range(5):
        M[i][j] = int(input("digite os numeros para a matriz: "))

num = int(input("digite um numero"))

for i in range(5):
    for j in range(5):
        if M[i][j] == num:
            msg = True
if msg == False:
    print("numero não encontrado")
else:
    print("numero encontrado")
