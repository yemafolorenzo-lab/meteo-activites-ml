# Documentation Intégration API Open-Meteo

Ce service permet de récupérer les données météorologiques nécessaires pour l'algorithme de recommandation d'activités. '

## Service : `weather_service.py`

### Fonction : `get_weather(date_str, lat=50.85, lon=4.35)`
Récupère les prévisions pour une date précise (format ISO `YYYY-MM-DD`).

**Contraintes :**
* La date ne peut pas être dans le passé.
* La portée maximale est de 16 jours à partir d'aujourd'hui.

### Format de Réponse (Dictionnaire)

| Clé | Type | Description |
| :--- | :--- | :--- |
| `temperature` | `float` | Température maximale prévue en °C. |
| `precipitation` | `float` | Cumul des précipitations en mm. |
| `vent` | `float` | Vitesse maximale du vent en km/h. |
| `humidite` | `float` | Humidité relative moyenne de la journée (%). |
| `condition` | `int` | Code simplifié : 0 (Clair), 1 (Léger), 2 (Modéré), 3 (Fort). |

### Gestion des Erreurs
* `ValueError` : Levée si la date est mal formatée ou hors portée.
* `ConnectionError` : Levée en cas de problème réseau ou d'indisponibilité de l'API.

---
*Note : Les données d'humidité sont calculées par une moyenne des valeurs horaires de la journée cible.*