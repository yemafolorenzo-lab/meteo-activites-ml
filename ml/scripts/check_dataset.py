import pandas as pd

# On charge le fichier que tu viens de générer
try:
    df = pd.read_csv('ml/data/dataset_meteo.csv')
    print("✅ Fichier chargé avec succès !\n")

    # On calcule les moyennes par activité pour vérifier la logique
    # On arrondit à 2 décimales pour que ce soit lisible
    check = df.groupby('activite').agg({
        'temperature': 'mean',
        'precipitation': 'mean',
        'vent': 'mean',
        'humidite': 'mean'
    }).round(2)

    print("--- Moyennes par activité ---")
    print(check)
    
except FileNotFoundError:
    print("❌ Erreur : Le fichier 'ml/data/dataset_meteo.csv' est introuvable.")