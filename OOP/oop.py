# Objektovo orientované programovanie (OOP)
# Definícia triedy
class Zviera:
    def __init__(self, meno):
        self.meno = meno

    def pozdrav(self):
        return f"Ahoj, ja som {self.meno}"

# Vytvorenie objektu
pes = Zviera("Buddy")
print(pes.pozdrav())

