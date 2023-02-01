class Auto:
    def __init__(self, nev, datum):
        self.nev = nev
        self.datum = int(datum)

    def __str__(self):
        return f"{self.nev}({self.datum})"
