from wetter import position, wetter_an
from bewertung import tipps, rekorde
from staedte import STAEDTE

# Schritt 1 + 2 für alle Städte (dauert ein paar Sekunden)
print("Hole Wetter für", len(STAEDTE), "Städte ...")
alle = []
for stadt in STAEDTE:
    pos = position(stadt)
    alle.append(wetter_an(pos))

# Schritt 3: Bewerten
print()
for titel, w in rekorde(alle).items():
    print(f"{titel}: {w['stadt']} ({w['beschreibung']}, {w['temperatur']} °C, "
          f"Wind {w['wind']} km/h, {w['luftfeuchtigkeit']} %)")
    for tipp in tipps(w):
        print("  -", tipp)

# Filtern: Wo regnet es gerade?
regen_staedte = []
for w in alle:
    if w["regen"] > 0:
        regen_staedte.append(w["stadt"])

print()
if regen_staedte:
    print("Hier regnet es gerade:", ", ".join(regen_staedte))
else:
    print("Gerade regnet es nirgends.")

# Rangliste: Top 5 wärmste Städte
print()
print("Top 5 wärmste Städte:")
sortiert = sorted(alle, key=lambda w: w["temperatur"], reverse=True)
platz = 1
for w in sortiert[:5]:
    print(f"  {platz}. {w['stadt']}: {w['temperatur']} °C")
    platz += 1
