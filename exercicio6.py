turno = input("Digite qual o Turno em que você estuda - (M)matutino, (V)vespertino ou (N)noturno: ").upper()

match turno:
    case"M":
        print ("bom dia estudante!")
    case"V":
        print ("boa tarde estudante!")
    case"N":
        print ("boa noite estudante!")
    case _:
        print ("turno invalido")