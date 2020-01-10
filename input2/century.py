def controller_input():
    """Demande de l'année de naissance """
    annee = input("Quel est votre année de naissance ? ")
    # print(date_naissance)
    clean(annee)


def clean(data_year):
    if len(data_year) == 1:
        century = int(data_year) + 1
        return print(f"{century} eme siecle")
    if len(data_year) == 2:
        century = data_year[:1]
    if len(data_year) == 3:
        pass
    if len(data_year) == 4:
        century = data_year[:2] + 1
        return century


def get_century(self):
    date = int(self.date_birth.year)
    if date > 100:
        century = date % 100
        if century == 0:
            self.century_birth = date // 100
        else:
            self.century_birth = date // 100 + 1
    else:
        self.century_birth = 1


def century():
    year = input("date année?")
    # month = input("date mois?")
    # day = input("date jours?")
    # date = datetime.date(int(year), int(month), int(day))
    # print(date)
    # if not date:
    # print("Bye")
    # else:
    if int(year) < 101:
        if int(year) < 1:
            return "0"
        else:
            return "Premier"
    if len(year) < 4:
        unite_siecle = year[:1]
        test_siecle = int(unite_siecle) * 100
        print("test_siecle ", test_siecle)
        if int(test_siecle) == int(year):
            return {unite_siecle}
        else:
            siecle = int(unite_siecle)
            siecle += 1
            return {siecle}
    if len(year) < 5:
        unite_siecle = year[:2]
        test_siecle = int(unite_siecle) * 100
        print("test_siecle ", test_siecle)
        if int(test_siecle) == int(year):
            return {unite_siecle}
        else:
            siecle = int(unite_siecle)
            siecle += 1
            return {siecle}
    return "pas de date ?"


if __name__ == "__main__":
    controller_input()
