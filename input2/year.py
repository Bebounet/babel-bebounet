# Validate Year

import datetime
import re

dt = datetime.datetime.now()

dt.year


def controller_input():
    """Demande de la date de naissance """
    date_naissance = input("Quel est votre date de naissance ? ")
    print(date_naissance)
    controller_file(date_naissance)


def controller_file(year):
    """Verifier l'input de l'utilisateur, taille et characteres"""
    lon_date = len(year)
    if lon_date > 4:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
    elif lon_date == 3:
        print("Format de date invalide ! \n <YYYY> ou <YY>")
    elif lon_date == 2:
        print("good pour 2", year)
        r = re.match("[0-9]", year)
        print(r)
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
        print("good pour 4", year)
        r = re.match("[0-9]", year)
        print(r)
        if r:
            validate_year(year)
            return year
        else:
            print("Veuillez entrer des chiffres ! \n ex : <1999> ou <99>")


def validate_year(data_year):
    """ Vérifier si la date est au format <YY> ou <YYYY>
        Si <YY> verifier si supérieur a 19"""
    if len(data_year) == 2:
        data_year = int(data_year)
        if data_year >= 19:
            print("Vous étes né en 19", data_year)
        else:
            print("Vous étes né en 20", data_year)
    else:
        print("Vous etes né en ", data_year)


def display_line_year():
    pass


if __name__ == "__main__":
    controller_input()
