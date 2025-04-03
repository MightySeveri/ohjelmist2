class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu: {self.nimi}")

class kirja(julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara}")

class lehti(julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")


hyttinr6 = kirja("Hytti N:o 6", "Rosa", 200)
aku_ankka = lehti("Aku Ankka", "Aki Hyyppä")

hyttinr6.tulosta_tiedot()
aku_ankka.tulosta_tiedot()
