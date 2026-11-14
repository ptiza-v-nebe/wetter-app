from wetter import position, wetter_an
from bewertung import tipps

# Schritt 1: Stadtname -> Position
pos = position("Berlin")
print("Gefunden:", pos["stadt"], "bei", pos["breitengrad"], "/", pos["laengengrad"])

# Schritt 2: Position -> Wetter
w = wetter_an(pos)
print("Wetter:", w["beschreibung"], w["temperatur"], "°C")

# Schritt 3: Wetter -> Bewertung
print("Tipps:")
for tipp in tipps(w):
    print("  -", tipp)
