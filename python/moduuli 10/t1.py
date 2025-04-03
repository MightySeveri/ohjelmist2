class Hissi:
    def __init__(self):
        self.pohja = 1
        self.ylin = 5
        self.nykyinen = 1

    def kerros_ylös(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1

    def kerros_alas(self):
        if self.nykyinen > self.pohja:
            self.nykyinen -= 1

    def siirry_kerrokseen(self, muutos):
        if self.nykyinen == muutos:
            print("Olet jo perillä.")
        elif self.nykyinen > muutos:
            while self.nykyinen > muutos:
                self.kerros_alas()
        elif self.nykyinen < muutos:
            while self.nykyinen < muutos:
                self.kerros_ylös()
        print(f"Olet nyt kerroksessa {self.nykyinen}")

hissi = Hissi()
hissi.siirry_kerrokseen(5)
