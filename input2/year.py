# Validate Year

import datetime
import re


def printseparator():
    """ Fonction qui affiche une ligne de séparation """
    print("-" * 50)


def controller_input():
    """Demande de l'année de naissance """
    annee = input("Quel est votre année de naissance ? ")
    # print(date_naissance)
    controller_file(annee)


def controller_file(year):
    """Verifier l'input de l'utilisateur, taille et caracteres 
       Si caractéres autres que [0-9] alors on redemande a l'utilisateur de taper la date"""
    lon_date = len(year)
    if lon_date > 4:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
        controller_input()
    elif lon_date == 3:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
        controller_input()
    elif lon_date == 2:
        # print("good pour 2", year)
        r = re.match("[0-9]", year)
        # print(r)
        if r:
            validate_year(year)
            return year
        else:
            print("Veuillez entrer des chiffres ! \nex : <1999> ou <99>")
            controller_input()
    elif lon_date == 1:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
        controller_input()
    elif lon_date == 0:
        print("Bye")
    else:
        # print("good pour 4", year)
        r = re.match("[0-9]", year)
        # print(r)
        if r:
            validate_year(year)
            return year
        else:
            print("Veuillez entrer des chiffres ! \nex : <1999> ou <99>")
            controller_input()


def validate_year(data_year, isverbose=True):
    """ Vérifier si la date est au format <YY> ou <YYYY>
        Si <YY> verifier si supérieur a 19"""
    dt = datetime.datetime.now()
    todyear = dt.year
    valyear = int(todyear)
    # valyear = l'année d'aujourd'hui
    if len(data_year) == 2:
        twoyear = valyear - 2000
        if isinstance(data_year, str):
            try:
                data_year = int(data_year)
            except ValueError as error:
                print(error)
                printseparator()
                print("Veuillez entrer des chiffres ! \nEx : <1999> ou <99>")
                return controller_input()
        if data_year >= twoyear:
            # data_year = str(data_year)
            data_year += 1900
            if isverbose:
                printseparator()
                print("Vous étes né en ", data_year)
                display_line_year(data_year)
                printseparator()
            else:
                return data_year

        else:
            data_year += 2000
            data_year = str(data_year)
            printseparator()
            print("Vous étes né en ", data_year)
            display_line_year(data_year)
            printseparator()
    else:
        # data_year = str(data_year)
        printseparator()
        print("Vous etes né en " + str(data_year))
        display_line_year(data_year)
        printseparator()


def display_line_year(data_year_from_arg):
    """Fonction qui calcule le nombre de jours entre la date de l'utilisateur et la date du jour"""
    date_now = datetime.date.today()
    date = datetime.date(int(data_year_from_arg), 10, 15)
    # date_now = int(str(date_now))
    # duree = int(duree)
    nb_jour = date_now - date
    print("Il y a", nb_jour.days, "jours.")


if __name__ == "__main__":
    controller_input()
