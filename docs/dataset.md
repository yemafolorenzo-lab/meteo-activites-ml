# Spécifications du Dataset Météo

## Variables et Unités
- **temperature** : Celsius (°C)
- **precipitation** : Millimètres (mm)
- **vent** : Kilomètres par heure (km/h) - *Aligné sur l'unité Open-Meteo*
- **humidite** : Pourcentage (%)

## Structure
- **Nombre de lignes** : 600
- **Classes** : 8 activités (distribution équilibrée de 75 lignes/activité)
- **Source** : Généré via `generate_dataset.py` (simulations basées sur le climat belge)

## Correspondance API
Le dataset utilise les mêmes unités que l'API **Open-Meteo** pour garantir la précision des prédictions en production sans conversion supplémentaire.