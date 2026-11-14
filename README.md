# Wetter-App

Kleine Python-Programme, die das aktuelle Wetter von [Open-Meteo](https://open-meteo.com) abfragen.
Open-Meteo ist kostenlos und braucht kein Konto und keinen API-Schlüssel – nur Internet.

| Ordner | Was drin ist |
|---|---|
| `v1/` | Die einfachsten Versionen, jeweils eine einzige Datei |
| `v2/` | Größere Version, aufgeteilt in mehrere Dateien, mit Reisetipps und Rekorden |

## Einrichten (einmalig)

Du brauchst einen Mac mit Internet. Alles passiert im **Terminal**
(Programme → Dienstprogramme → Terminal).

**1. uv installieren.** uv kümmert sich um Python und alles, was die App braucht.

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Danach das Terminal schließen und neu öffnen.

**2. Die App herunterladen.**

```
git clone https://github.com/ptiza-v-nebe/wetter-app.git
cd wetter-app
```

Falls `git` fehlt, fragt der Mac, ob er die Entwicklerwerkzeuge installieren soll – mit „Installieren“ bestätigen.
Oder auf GitHub auf **Code → Download ZIP** klicken und die ZIP-Datei entpacken.

## Starten

Beim ersten Start lädt uv automatisch Python und das Paket `requests` herunter. Das dauert ein paar Sekunden.

### v1 – die einfachen Versionen

```
cd v1
uv run wetter-v1.py
uv run wetter-v2.py
```

- `wetter-v1.py` fragt das Wetter für feste Koordinaten (Berlin) ab.
- `wetter-v2.py` sucht zuerst die Koordinaten einer Stadt und fragt dann das Wetter ab.
  Die Stadt kannst du oben in der Datei ändern: `stadt = "Berlin"`.

### v2 – die größere Version

```
cd v2
uv run mein_programm.py    # Wetter und Tipps für Berlin
uv run reise.py            # fragt nach einem Land und zeigt das Wetter in seinen Städten
uv run extreme.py          # vergleicht alle Städte (dauert etwas länger)
```

## Aktuelle Version holen

Wenn es auf GitHub etwas Neues gibt:

```
cd wetter-app
git pull
```

## In VS Code programmieren

1. In VS Code die Erweiterung **Python** installieren.
2. Den Ordner `v1` oder `v2` öffnen (Datei → Ordner öffnen).
3. Einmal `uv run ...` im Terminal ausführen, damit der Ordner `.venv` entsteht.
4. In VS Code `Cmd+Shift+P` → **Python: Select Interpreter** → `.venv/bin/python` auswählen.
