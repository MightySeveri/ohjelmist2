import random


class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self):
        nopeuden_muutos = random.randint(-10, 15)
        self.nopeus += nopeuden_muutos

        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit=1):
        self.matka += self.nopeus * tunnit

    def __str__(self):
        return f"{self.rekisteritunnus}\t{self.huippunopeus} km/h\t{self.nopeus} km/h\t{self.matka:.2f} km"


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä()
            auto.kulje()

    def tulosta_tilanne(self):
        print("KILPAILUN TILANNE")
        print("Rekisteri\tHuippunopeus\tNopeus\tMatka")
        for auto in self.autot:
            print(auto)

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)


def suorita_kilpailu():
    autot = [Auto(f"ABC-{i}") for i in range(1, 11)]
    kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            kilpailu.tulosta_tilanne()

    kilpailu.tulosta_tilanne()
    voittaja = max(autot, key=lambda x: x.matka)
    print(f"Kilpailun voittaja on {voittaja.rekisteritunnus}, joka ajoi {voittaja.matka:.2f} km!")


suorita_kilpailu()