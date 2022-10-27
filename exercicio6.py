turno = input("Digite qual o Turno em que você estuda - Matutino, Vespertino ou noturno: ")

match turno:
    case"matutino":
        print ("bom dia estudante!")
    case"verpertino":
        print ("boa tarde estudante!")
    case"noturno":
        print ("boa noite estudante!")
    case (others):
        print ("turno invalido")