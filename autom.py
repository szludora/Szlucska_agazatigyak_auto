from Auto import Auto

kocsi = []


def autom():
    fajl = open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    tartalom = fajl.readlines()
    fajl.close()

    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip().split("$")
        auto = Auto(sor[0], sor[1])
        kocsi.append(auto)
        i += 1


def flotta():
    return len(kocsi)


def legfiatalabb():

    legfiatalabb = 0

    i = 0
    while i < len(kocsi):
        if kocsi[i].datum > kocsi[legfiatalabb].datum:
            legfiatalabb = i
        i += 1

    return kocsi[legfiatalabb]


def legoregebb():

    legoregebb = 0

    i = 0
    while i < len(kocsi):
        if kocsi[i].datum < kocsi[legoregebb].datum:
            legoregebb = i
        i += 1

    return kocsi[legoregebb]
