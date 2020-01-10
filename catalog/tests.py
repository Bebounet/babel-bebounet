# Create your tests here.


def test_get_century():
    year_to_test = [1705, 19, 1700, 2011, 1200, 403, 0]
    for y in year_to_test:
        century = get_century(y)
        print(f"année {y} siècle {century}")

    print("---" * 30)
    year_to_test_with_result = [
        (1701, 18),
        (19, 1),
        (1700, 17),
        (2011, 21),
        (1200, 12),
        (403, 5),
        (0, 1),
    ]
    for testy in year_to_test_with_result:
        century = get_century(testy[0])
        if century == testy[1]:
            print(f"année {testy} siècle {century} : PASSED")
        else:
            print(f"année {testy} siècle {century} expexted {testy[1]}: FAILED")
            raise Exception(f"TEST FAILED with {testy[0]}")


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


test_get_century()
