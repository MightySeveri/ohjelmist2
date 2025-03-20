import random

class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = random.randint(100, 200)
        self.matka = 0

    def kiihdytä(self):
        nopeuden_muutos = random.randint(-10, 15)
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self):
        self.matka += self.nopeus

    def __str__(self):
        return f"{self.rekisteritunnus}\t{self.huippunopeus} km/h\t{self.nopeus} km/h\t{self.matka:.2f} km"

def kilpailu():
    autot = []

    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        autot.append(Auto(rekisteritunnus))

    while True:
        for auto in autot:
            auto.kiihdytä()
            auto.kulje()

        if any(auto.matka >= 10000 for auto in autot):
            break

    print("Rekisteritunnus\tHuippunopeus\tNopeus\tMatka")
    for auto in autot:
        print(auto)

kilpailu()
