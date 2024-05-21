# Výnimky a chybové hlásenia
# Ošetrovanie výnimiek
try:
    cislo = int("XYZ")
except ValueError:
    print("Nastala chyba: Hodnota nie je číslo.")
finally:
    print("Tento blok sa vykoná vždy.")

