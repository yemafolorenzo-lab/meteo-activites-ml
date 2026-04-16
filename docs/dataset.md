# Spécifications du Dataset Météo

## Variables et Unités
- **temperature** : Celsius (°C)
- **precipitation** : Millimètres (mm)
- **vent** : Kilomètres par heure (km/h) - *Aligné sur l'unité Open-Meteo*
- **humidite** : Pourcentage (%)

## Structure
- **Nombre de lignes** : 600
- **Classes** : 8 activités (distribution équilibrée de 75 lignes/activité)
  Le dataset est équilibré avec **75 lignes par activité** :
1. **Balade en ville**
2. **Balade à vélo**
3. **Barbecue**
4. **Cinéma**
5. **Musée / Expo**
6. **Pique-nique au parc**
7. **Randonnée en forêt**
8. **Sport en salle**
- **Source** : Généré via `generate_dataset.py` (simulations basées sur le climat belge)

## Correspondance API
Le dataset utilise les mêmes unités que l'API **Open-Meteo** pour garantir la précision des prédictions en production sans conversion supplémentaire.
