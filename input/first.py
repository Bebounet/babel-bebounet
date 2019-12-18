# Premier traitement

fullname = input("Quel est votre nom et prénom ?")
print(fullname)

names = fullname.split()

# print(names)
# print(type(names))
# print(len(names))

len_listnames = len(names)
print(len_listnames)

if len_listnames == 2:
    print("Nom : " + names[0] + " prénom : " + names[1])
elif len_listnames == 3:
    print(f"Nom : {names[0]}, Milieu : {names[1]}, Prénom : {names[2]}")
elif len_listnames == 1:
    print("Nom : " + names[0])
else:
    print(f"Nom : {names[0]}, Milieu : {names[1]}, Prénom : {names[2]}")
    print("Format : Nom <Milieu> Prénom")
    print("Que faire de : " + " ".join(names[3:]))
