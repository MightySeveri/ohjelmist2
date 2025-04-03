class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.pohja = alinkerros
        self.ylin = ylinkerros
        self.nykyinen = alinkerros

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1

    def kerros_alas(self):
        if self.nykyinen > self.pohja:
            self.nykyinen -= 1

    def aja_hissiä(self, muutos):
        if self.nykyinen == muutos:
            print("Olet jo perillä.")
        elif self.nykyinen > muutos:
            while self.nykyinen > muutos:
                self.kerros_alas()
        elif self.nykyinen < muutos:
            while self.nykyinen < muutos:
                self.kerros_ylös()
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")


class Talo:
    def __init__(self, hissin_alinkerros, hissin_ylinkerros, hissienmäärä):
        self.hissit = [Hissi(hissin_alinkerros, hissin_ylinkerros) for _ in range(hissienmäärä)]
        self.alinkerros = hissin_alinkerros

    def aja_hissiä(self, hissin_numero, muutos):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero+1} kerrokseen {muutos}")
            self.hissit[hissin_numero].aja_hissiä(muutos)
        else:
            print("Virhe: Hissin numero ei ole olemassa!")

#seuraavaan for looppiin sain apua stackoverflowsta ja tiedän mitä enumerate tekee
    def palohälytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen!")
        for i, hissi in enumerate(self.hissit):
            print(f"Hissi {i+1} siirtyy pohjakerrokseen")
            hissi.aja_hissiä(self.alinkerros)
        print("Kaikki hissit ovat nyt pohjakerroksessa.")

talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 5)

talo.aja_hissiä(1, 8)

talo.palohälytys()
