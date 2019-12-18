from second import F_ERROR
import second


def printseparator():
    """ Fonction qui affiche une ligne de séparation """
    print("-" * 50)


printseparator()
print("1 er")
printseparator()
d = second.validate("Coco popo")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)

printseparator()
print("2 eme")
printseparator()
d = second.validate("")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)

printseparator()
print("3 eme")
printseparator()
d = second.validate("popo25 cococo984q#|``@àà")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)

# second.validate_display("Nicolas Bebounet")
# second.validate_display("dodo dada didi")
# second.validate_display("popo papa pupu pipi pepe")
# second.manage_input()
