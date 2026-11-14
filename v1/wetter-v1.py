import requests

# Wir fragen die Wetter-Webseite: "Wie warm ist es gerade in Berlin?"
antwort = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 52.52,               # Breitengrad von Berlin
        "longitude": 13.41,              # Längengrad von Berlin
        "current": "temperature_2m",     # was wir wissen wollen: die Temperatur
    },
)

# Die Antwort kommt als Text zurück. .json() macht daraus ein Python-Wörterbuch.
daten = antwort.json()

# So sieht die ganze Antwort aus:
print(daten)

# Und daraus holen wir uns nur die Temperatur:
print("In Berlin sind es gerade", daten["current"]["temperature_2m"], "°C")
