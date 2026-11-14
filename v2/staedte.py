# Liste bekannter Städte, sortiert nach Land.
# Die Städtenamen sind meist auf Englisch, damit die API sie sicher findet.
# Zurück bekommst du trotzdem den deutschen Namen (z.B. "Cape Town" -> "Kapstadt").

LAENDER = {
    "Deutschland": ["Berlin", "München", "Hamburg"],
    "Großbritannien": ["London"],
    "Frankreich": ["Paris"],
    "Italien": ["Rome"],
    "Spanien": ["Madrid"],
    "Norwegen": ["Oslo"],
    "Island": ["Reykjavik"],
    "Russland": ["Moscow"],
    "Ägypten": ["Cairo"],
    "Kenia": ["Nairobi"],
    "Südafrika": ["Cape Town"],
    "VAE": ["Dubai"],
    "Indien": ["Mumbai", "New Delhi"],
    "Thailand": ["Bangkok"],
    "Singapur": ["Singapore"],
    "China": ["Beijing"],
    "Japan": ["Tokyo", "Osaka", "Sapporo"],
    "Australien": ["Sydney", "Melbourne"],
    "USA": ["New York", "Los Angeles", "Miami", "Anchorage"],
    "Kanada": ["Toronto", "Vancouver"],
    "Mexiko": ["Mexico City"],
    "Brasilien": ["Rio de Janeiro", "Sao Paulo"],
    "Argentinien": ["Buenos Aires"],
}

# Alle Städte in einer einzigen Liste
STAEDTE = []
for staedte_im_land in LAENDER.values():
    STAEDTE.extend(staedte_im_land)
