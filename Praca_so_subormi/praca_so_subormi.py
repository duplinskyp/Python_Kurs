# Práca so súbormi
# Zápis do súboru
with open("subor.txt", "w") as f:
    f.write("Ahoj, svet!
")

# Čítanie zo súboru
with open("subor.txt", "r") as f:
    obsah = f.read()
    print(obsah)

