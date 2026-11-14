import requests


# ---------------------------------------------------------------
# Schritt 1: Stadtname -> Position
# ---------------------------------------------------------------
def position(stadt):
    """Sucht eine Stadt und gibt ihren Namen und ihre Koordinaten zurück."""
    suche = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": stadt, "count": 1, "language": "de"},
    ).json()

    if "results" not in suche:
        raise ValueError(f"Stadt '{stadt}' nicht gefunden")

    ort = suche["results"][0]
    return {
        "stadt": ort["name"],
        "breitengrad": ort["latitude"],
        "laengengrad": ort["longitude"],
    }


# ---------------------------------------------------------------
# Schritt 2: Position -> Wetter
# ---------------------------------------------------------------
def beschreibung(code):
    """Übersetzt den Wetter-Code der API (eine Zahl) in Worte."""
    if code == 0:
        return "klar"
    if code <= 3:
        return "bewölkt"
    if code <= 48:
        return "Nebel"
    if code <= 67:
        return "Regen"
    if code <= 77:
        return "Schnee"
    if code <= 82:
        return "Regenschauer"
    if code <= 86:
        return "Schneeschauer"
    return "Gewitter"


def wetter_an(pos):
    """Holt das aktuelle Wetter für eine Position."""
    daten = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": pos["breitengrad"],
            "longitude": pos["laengengrad"],
            "current": "temperature_2m,apparent_temperature,relative_humidity_2m,"
                       "wind_speed_10m,precipitation,weather_code",
        },
    ).json()["current"]

    return {
        "stadt": pos.get("stadt", "Unbekannter Ort"),
        "beschreibung": beschreibung(daten["weather_code"]),
        "temperatur": daten["temperature_2m"],
        "gefuehlt": daten["apparent_temperature"],
        "luftfeuchtigkeit": daten["relative_humidity_2m"],
        "wind": daten["wind_speed_10m"],
        "regen": daten["precipitation"],
    }


# ---------------------------------------------------------------
# Abkürzung: beides hintereinander
# (damit reise.py und extreme.py weiter funktionieren)
# ---------------------------------------------------------------
def wetter(stadt):
    return wetter_an(position(stadt))
