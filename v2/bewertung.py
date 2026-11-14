# Schritt 3: Wetter -> Bewertung
# Hier steckt keine API mehr drin, nur noch Logik mit den Wetterdaten.


def tipps(w):
    """Schaut sich die Wetterdaten an und gibt eine Liste mit Tipps zurück."""
    liste = []
    t = w["temperatur"]

    # Was anziehen?
    if t < 0:
        liste.append("Winterjacke, Mütze und Handschuhe einpacken")
    elif t < 10:
        liste.append("Warme Jacke mitnehmen")
    elif t < 20:
        liste.append("Pullover oder leichte Jacke reicht")
    elif t < 30:
        liste.append("T-Shirt-Wetter")
    else:
        liste.append("Sehr heiß: Sonnencreme, Kopfbedeckung, viel trinken")

    # Niederschlag & Unwetter
    if w["regen"] > 0 or "Regen" in w["beschreibung"]:
        liste.append("Regenschirm einpacken")
    if "Schnee" in w["beschreibung"]:
        liste.append("Feste, warme Schuhe für Schnee")
    if "Gewitter" in w["beschreibung"]:
        liste.append("Achtung, Gewitter! Flugverspätungen möglich")

    # Wind & Gefühl
    if w["wind"] > 40:
        liste.append("Starker Wind: windfeste Jacke statt Schirm")
    if t > 25 and w["luftfeuchtigkeit"] > 70:
        liste.append("Schwül: luftige Kleidung aus Baumwolle oder Leinen")
    if abs(w["gefuehlt"] - t) >= 5:
        liste.append(f"Fühlt sich an wie {w['gefuehlt']} °C")

    return liste


def rekorde(alle):
    """Bekommt eine Liste mit Wetterdaten und findet die Extreme."""
    return {
        "Am wärmsten": max(alle, key=lambda w: w["temperatur"]),
        "Am kältesten": min(alle, key=lambda w: w["temperatur"]),
        "Am windigsten": max(alle, key=lambda w: w["wind"]),
        "Am feuchtesten": max(alle, key=lambda w: w["luftfeuchtigkeit"]),
    }
