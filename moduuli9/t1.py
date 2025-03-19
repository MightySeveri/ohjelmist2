class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinennopeus = 0
        self.kuljettumatka = 0

auto1 = Auto("ABC-123", 142 )
print(f"rekisteritunnus on {auto1.rekisteritunnus}, huippunopeus {auto1.huippunopeus} km/h, tämänhetkinen nopeus on {auto1.tamanhetkinennopeus}, auton kuljettu matka on {auto1.kuljettumatka}")