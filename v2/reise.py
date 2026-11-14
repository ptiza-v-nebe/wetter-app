from wetter import position, wetter_an
from bewertung import tipps
from staedte import LAENDER

land = input("In welches Land fliegst du? ")

if land not in LAENDER:
    print("Das Land kenne ich leider nicht. Möglich sind:")
    print(", ".join(LAENDER))
else:
    for stadt in LAENDER[land]:
        pos = position(stadt)      # Schritt 1
        w = wetter_an(pos)         # Schritt 2
        print()
        print(f"{w['stadt']}: {w['beschreibung']}, {w['temperatur']} °C")
        for tipp in tipps(w):      # Schritt 3
            print("  -", tipp)
