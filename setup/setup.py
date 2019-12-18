"""
SETUP v0.1
Programme qui affiche le setup de la machine python
Changelog : - dec 19 : initialisation
"""

import sys
import os
import datetime


def printseparator():
    """ Fonction qui affiche une ligne de séparation """
    print("-" * 50)


a = "Bonjour Monde !"
print(a)  # j'affiche l'objet #

printseparator()
print(sys.executable)
print(sys.platform)
print(sys.path)

print(sys.version_info)
v = sys.version_info
# print(type(v)) #Type de sys
# print(dir(v)) #Introspection de sys

print(f"Pyhton version {v.major}.{v.minor}.{v.micro}")
print("Pyhton version {}.{}.{}".format(v.major, v.minor, v.micro))

# print("Pyhton version %s.%s.%s" % (v.major, v.minor, v.micro))  # Version 2.7, deprécié
printseparator()
print("Environement PythonPath : " + os.getenv("PYTHONPATH", "Vide"))

printseparator()
print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
print(f"Date et Heure {dt} - Année {dt.year}")

printseparator()
help(printseparator)
