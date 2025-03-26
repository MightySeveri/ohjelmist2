class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = 0
        self.kuljettumatka = 0

    def kulje(self, tunti):
        self.kuljettumatka += self.tamanhetkinennopeus * tunti

    def kiihdyta(self, muutos):
        self.tamanhetkinennopeus += muutos
        if self.huippunopeus > self.huippunopeus:
            self.tamanhetkinennopeus = self.huippunopeus
        elif self.tamanhetkinennopeus < 0:
            self.tamanhetkinennopeus = 0

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

sahko = Sahkoauto("ABC-15", 165, 52.5)
poltto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.kiihdyta(123)
poltto.kiihdyta(123)
sahko.kulje(3)
print(f"sähköauton kuljettumatka kolmessa tunnisa on {sahko.kuljettumatka} km")

poltto.kulje(3)
print(f"polttoainemoottori auton kuljettumatka kolmessa tunnisa on {poltto.kuljettumatka} km")

