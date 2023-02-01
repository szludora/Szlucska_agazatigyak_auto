import datetime


def beker():
    print("I/A:")
    nev = input("\tAutó neve: ")
    datum = int(input("\tGyártási dátum: "))
    mai = datetime.datetime.now().year

    if datum == mai:
        valasz = f"\tEz a(z) {nev} friss gyártás"
    elif datum >= 2000:
        valasz = f"\tEz a(z) {nev} átlagos korú"
    else:
        valasz = f"\tEz a(z) {nev} öreg autó"

    print(valasz)
