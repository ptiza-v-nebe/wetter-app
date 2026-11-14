import requests

stadt = "Berlin"

# Schritt 1: Wir fragen die Städte-Webseite: "Wo liegt diese Stadt?"
antwort = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={
        "name": stadt,       # welche Stadt wir suchen
        "count": 1,          # wir wollen nur den ersten Treffer
    },
)
ort = antwort.json()["results"][0]

breitengrad = ort["latitude"]
laengengrad = ort["longitude"]
print(stadt, "liegt bei", breitengrad, "/", laengengrad)

# Schritt 2: Mit diesen Koordinaten fragen wir die Wetter-Webseite – genau wie in wetter-v1.py
antwort = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": breitengrad,
        "longitude": laengengrad,
        "current": "temperature_2m",
    },
)
daten = antwort.json()

print("In", stadt, "sind es gerade", daten["current"]["temperature_2m"], "°C")
