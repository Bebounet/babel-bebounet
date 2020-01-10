""" 
    UTILS.PY
    Catalog shared functions
"""

import xlrd


def get_century(year):
    """ Get century from int year and return int century """
    if year > 100:
        century = year % 100
        if century == 0:
            century_birth = year // 100
        else:
            century_birth = year // 100 + 1
    else:
        century_birth = 1
    return century_birth


def xls_reader():
    """ Permet de lire un fichier excel .xls"""
    liste_dewey = [
        (),
        (),
    ]
    path = "scrap/La_Dewey_simplifiee.xls"
    # Réouverture du classeur
    classeur = xlrd.open_workbook(path)

    # Récupération du nom de toutes les feuilles sous forme de liste
    nom_des_feuilles = classeur.sheet_names()

    # Récupération de la première feuille
    feuille = classeur.sheet_by_name(nom_des_feuilles[0])
    for i in range(0, 109):
        for j in range(0, 1):
            if feuille.cell_value(i, 1):
                number = feuille.cell_value(i, 1)
                name = feuille.cell_value(i, 2)
                liste_dewey[0] = number
                liste_dewey[1] = name
                # print(f"{liste_dewey[0]} -------- {liste_dewey[1]}")
                # liste_dewey[0], liste_dewey[1]
                print(liste_dewey)
                liste_dewey
                # print(f"Number: {number} name : {name}")
    return liste_dewey


# xls_reader()
