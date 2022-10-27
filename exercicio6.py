turno = input("Digite qual o Turno em que você estuda - matutino, vespertino ou noturno: ")

match turno:
    case"matutino":
        print ("bom dia estudante!")
    case"vespertino":
        print ("boa tarde estudante!")
    case"noturno":
        print ("boa noite estudante!")
    case _:
        print ("turno invalido")