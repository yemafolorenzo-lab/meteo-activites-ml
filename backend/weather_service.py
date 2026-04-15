# """
# weather_service.py
# Récupère les prévisions météo depuis l'API Open-Meteo pour une date donnée.
# """
# import httpx
# from datetime import date, timedelta


# BASE_URL = "https://api.open-meteo.com/v1/forecast"
# MAX_DAYS = 16


# def get_weather(date_str: str, lat: float = 50.85, lon: float = 4.35) -> dict:
#     today = date.today()
#     target = date.fromisoformat(date_str)

#     # Validation de la date
#     if target < today:
#         raise ValueError(f"La date {date_str} est dans le passé.")
#     if target > today + timedelta(days=MAX_DAYS):
#         raise ValueError(f"La date {date_str} dépasse la portée maximale de {MAX_DAYS} jours.")

#     # Appel API
#     try:
#         response = httpx.get(BASE_URL, params={
#             "latitude": lat,
#             "longitude": lon,
#             "daily": "temperature_2m_max,precipitation_sum,windspeed_10m_max",
#             "hourly": "relative_humidity_2m",
#             "timezone": "Europe/Brussels",
#             "forecast_days": MAX_DAYS,
#         }, timeout=10.0)
#         response.raise_for_status()
#     except httpx.TimeoutException:
#         raise ConnectionError("L'API météo ne répond pas (timeout).")
#     except httpx.HTTPError as e:
#         raise ConnectionError(f"Erreur lors de l'appel API : {e}")

#     data = response.json()

#     # Extraire les données daily pour la date cible
#     daily_times = data["daily"]["time"]
#     if date_str not in daily_times:
#         raise ValueError(f"Date {date_str} introuvable dans la réponse API.")

#     idx = daily_times.index(date_str)
#     temperature  = float(data["daily"]["temperature_2m_max"][idx])
#     precipitation= float(data["daily"]["precipitation_sum"][idx])
#     vent         = float(data["daily"]["windspeed_10m_max"][idx])

#     # Calculer humidité moyenne depuis les données hourly
#     hourly_times = data["hourly"]["time"]
#     humidity_values = [
#         data["hourly"]["relative_humidity_2m"][i]
#         for i, t in enumerate(hourly_times)
#         if t.startswith(date_str)
#     ]
#     humidite = round(sum(humidity_values) / len(humidity_values), 1)

#     # Déduire la condition depuis precipitation_sum
#     if precipitation == 0:
#         condition = 0
#     elif precipitation <= 1:
#         condition = 1
#     elif precipitation <= 5:
#         condition = 2
#     else:
#         condition = 3

#     return {
#         "temperature": temperature,
#         "precipitation": precipitation,
#         "vent": vent,
#         "humidite": humidite,
#         "condition": condition,
#     }

#     # === PARTIE TEST ===
# # Ce bloc ne s'exécutera que si tu lances ce fichier directement
# if __name__ == "__main__":
#     print("Test avec la date d'aujourd'hui (17 avril 2026):")
#     print(get_weather("2026-04-17"))
    
#     # print("\nTest avec une date hors portée (2027):")
#     # print(get_weather("2027-01-01"))

"""
weather_service.py
Récupère les prévisions météo depuis l'API Open-Meteo pour une date donnée.
"""
import httpx
from datetime import date, timedelta

BASE_URL = "https://api.open-meteo.com/v1/forecast"
MAX_DAYS = 16

def get_weather(date_str: str, lat: float = 50.85, lon: float = 4.35) -> dict:
    today = date.today()
    target = date.fromisoformat(date_str)

    # Validation de la date
    if target < today:
        raise ValueError(f"La date {date_str} est dans le passé. Aujourd'hui nous sommes le {today}.")
    if target > today + timedelta(days=MAX_DAYS):
        raise ValueError(f"La date {date_str} dépasse la portée maximale de {MAX_DAYS} jours.")

    # Appel API
    try:
        response = httpx.get(BASE_URL, params={
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,precipitation_sum,windspeed_10m_max",
            "hourly": "relative_humidity_2m", # Correction : ajout de l'underscore
            "timezone": "Europe/Brussels",
            "forecast_days": MAX_DAYS,
        }, timeout=10.0)
        response.raise_for_status()
    except httpx.TimeoutException:
        raise ConnectionError("L'API météo ne répond pas (timeout).")
    except httpx.HTTPError as e:
        raise ConnectionError(f"Erreur lors de l'appel API : {e}")

    data = response.json()

    # Extraire les données daily pour la date cible
    daily_times = data["daily"]["time"]
    if date_str not in daily_times:
        raise ValueError(f"Date {date_str} introuvable dans la réponse API.")

    idx = daily_times.index(date_str)
    temperature  = float(data["daily"]["temperature_2m_max"][idx])
    precipitation= float(data["daily"]["precipitation_sum"][idx])
    vent         = float(data["daily"]["windspeed_10m_max"][idx])

    # Calculer humidité moyenne depuis les données hourly
    hourly_times = data["hourly"]["time"]
    # Correction ici aussi : relative_humidity_2m
    humidity_values = [
        data["hourly"]["relative_humidity_2m"][i]
        for i, t in enumerate(hourly_times)
        if t.startswith(date_str)
    ]
    
    if not humidity_values:
        humidite = 0
    else:
        humidite = round(sum(humidity_values) / len(humidity_values), 1)

    # Déduire la condition depuis precipitation_sum
    if precipitation == 0:
        condition = 0 # Clair
    elif precipitation <= 1:
        condition = 1 # Pluie légère
    elif precipitation <= 5:
        condition = 2 # Pluie modérée
    else:
        condition = 3 # Forte pluie

    return {
        "temperature": temperature,
        "precipitation": precipitation,
        "vent": vent,
        "humidite": humidite,
        "condition": condition,
    }

# === PARTIE TEST ===
if __name__ == "__main__":
    # On teste avec la date système actuelle (16 avril 2026)
    aujourdhui = date.today().isoformat()
    print(f"Test avec la date d'aujourd'hui ({aujourdhui}):")
    try:
        print(get_weather(aujourdhui))
    except Exception as e:
        print(f"Erreur : {e}")
    
    print("\nTest avec une date trop lointaine :")
    try:
        print(get_weather("2027-01-01"))
    except Exception as e:
        print(f"Erreur attendue : {e}")