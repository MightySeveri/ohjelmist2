class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, muutos):
        self.tamanhetkinennopeus += muutos
        if self.tamanhetkinennopeus > self.huippunopeus:
            self.tamanhetkinennopeus = self.huippunopeus
        elif self.tamanhetkinennopeus < 0:
            self.tamanhetkinennopeus = 0

    def kulje(self, tunti):
        self.tamanhetkinennopeus * tunti
        if self.tamanhetkinennopeus > 0:
            self.kuljettumatka = self.tamanhetkinennopeus * tunti

auto1 = Auto("ABC-123", 142 )
print(f"rekisteritunnus on {auto1.rekisteritunnus}, huippunopeus {auto1.huippunopeus} km/h, tämänhetkinen nopeus on {auto1.tamanhetkinennopeus}, auton kuljettu matka on {auto1.kuljettumatka}")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"nopeus kiihdytyksen jälkeen {auto1.tamanhetkinennopeus} km/h")

auto1.kulje(3)
print(f"kuljettumatka kolmessa tunnisa on {auto1.kuljettumatka} km")

auto1.kiihdyta(-200)
print(f"nopeus hätäjarrutuksen jälkeen {auto1.tamanhetkinennopeus} km/h")