# Premier traitement

# print(names)
# print(type(names))
# print(len(names))
import re

F_FIRST = "firstname"
F_LAST = "lastname"
F_MIDDLE = "middlename"
F_FULL = "fullname"
F_ERROR = "error"


def manage_input():
    in_fullname = input("Quel est votre nom et prénom ? ")
    print(in_fullname)
    validate_display(in_fullname)


def validate_display(fullname):
    """ 
    validation et affichage d'une string 
    selon format Prénom <Milieu> Nom 
    """

    names = fullname.split()
    len_listnames = len(names)
    print(len_listnames)

    # if len_listnames == 2:
    #     print("Nom : " + names[0] + " prénom : " + names[1])
    # elif len_listnames == 3:
    #     print(f"Nom : {names[0]}, Milieu : {names[1]}, Prénom : {names[2]}")
    # elif len_listnames == 1:
    #     print("Nom : " + names[0])
    # else:
    #     print(f"Nom : {names[0]}, Milieu : {names[1]}, Prénom : {names[2]}")
    #     print("Format : Nom <Milieu> Prénom")
    #     print("Que faire de : " + " ".join(names[3:]))
    d = {}
    if len_listnames == 2:
        d = {F_FIRST: names[0], F_LAST: names[1]}
        return d
    elif len_listnames == 3:
        d = {F_FIRST: names[0], F_MIDDLE: names[1], F_LAST: names[2]}
        return d
    elif len_listnames == 1:
        d = {F_FIRST: names[0]}
        return d
    else:
        erreur = "Format : Prénom <Milieu> Nom\nQue faire de : " + " ".join(names[3:])
        d[F_ERROR] = erreur
        return d[F_ERROR]


F_FIRST = "firstname"
F_LAST = "lastname"
F_MIDDLE = "middlename"
F_FULL = "fullname"
F_ERROR = "error"


def validate_juststring(input):
    """ si la string input contient just des caractères A-Z"""
    # si vide
    # enlever les espaces
    # regarde si AZ ou az
    print(input)
    if not len(input):
        return False
    r = re.match("^[A-Za-z]+$", input)
    print(r)
    return True if r else False


def validate(fullname):
    """ validation et affichage d'une string 
        selon format Prénom <Milieu> Nom 
    """
    names = fullname.split()
    len_listnames = len(names)
    # Vérifier que chaque str de names ne comporte que des lettres de l'alphabet
    type(names)
    for n in names:
        # n = n.strip() # Enlveve les espaces
        if not validate_juststring(n):
            # return error
            return {F_ERROR: "erreur de validation de " + n}

    d = {}
    if len_listnames == 2:
        d[F_FIRST] = names[0]
        d[F_LAST] = names[1]
    elif len_listnames == 3:
        d[F_FIRST] = names[0]
        d[F_MIDDLE] = names[1]
        d[F_LAST] = names[2]
    elif len_listnames == 1:
        d[F_LAST] = names[0]
    else:
        error = "Format : Prénom <Milieu> Nom\nQue faire de : " + " ".join(names[3:])
        d[F_ERROR] = error
    return d


def verification(names):
    if type(names) == str:
        validate_display()
    else:
        print("Erreur , erreur!")


if __name__ == "__main__":
    manage_input()
