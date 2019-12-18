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
    """Verifier l'input de l'utilisateur, taille et characteres"""
    lon_date = len(year)
    if lon_date > 4:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
    elif lon_date == 3:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
    elif lon_date == 2:
        # print("good pour 2", year)
        r = re.match("[0-9]", year)
        # print(r)
        if r:
            validate_year(year)
            return year
        else:
            print("Veuillez entrer des chiffres ! \n ex : <1999> ou <99>")
    elif lon_date == 1:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
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
            print("Veuillez entrer des chiffres ! \n ex : <1999> ou <99>")


def validate_year(data_year):
    """ Vérifier si la date est au format <YY> ou <YYYY>
        Si <YY> verifier si supérieur a 19"""
    dt = datetime.datetime.now()
    todyear = dt.year
    valyear = int(todyear)
    if len(data_year) == 2:
        twoyear = valyear - 2000
        data_year = int(data_year)
        if data_year >= twoyear:
            data_year = str(data_year)
            printseparator()
            print("Vous étes né en 19" + data_year)
            printseparator()
        else:
            data_year = str(data_year)
            printseparator()
            print("Vous étes né en 20" + data_year)
            printseparator()
    else:
        data_year = str(data_year)
        printseparator()
        print("Vous etes né en " + data_year)
        printseparator()


def display_line_year():
    pass


if __name__ == "__main__":
    controller_input()
