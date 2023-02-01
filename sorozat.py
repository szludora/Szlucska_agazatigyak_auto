import random

lottoszamok = []


def feladat():
    print("II/A, B, C:")

    while len(lottoszamok) < 5:
        vel = int(random.random() * 90) + 1
        while vel not in lottoszamok:
            lottoszamok.append(vel)

    kiir = ""

    i = 0
    while i < 4:
        kiir += str(lottoszamok[i]) + "- "
        i += 1
    print("\t", kiir + str(lottoszamok[i]))


def egyjegyuek_szama():
    egyjegyu = 0

    i = 0
    while i < len(lottoszamok):
        if lottoszamok[i] < 10:
            egyjegyu += 1
        i += 1
    return egyjegyu


def konzol_kiir():
    x = egyjegyuek_szama()
    print("II/D, E:\n\tAz egyjegyűek száma:", x)
    file_kiir(x)


def file_kiir(x):
    fajl = open("szamok.txt", "w", encoding="utf-8")
    fajl.write(f"II/F:\n\tA fejek száma: {x}.")
    fajl.close()
    fajl = open("szamok.txt", "r", encoding="utf-8")
    tartalom = fajl.readlines()
    fajl.close()

    print("\nA számok.txt tartalma:\n")
    i = 0
    while i < len(tartalom):
        sor = tartalom[i].strip()
        if i == 0:
            print(sor)
        else:
            print("\t", sor)
        i += 1
