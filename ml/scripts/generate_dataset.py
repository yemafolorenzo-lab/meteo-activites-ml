import pandas as pd
import random
import os

# Configuration
NUM_SAMPLES = 600
FILE_PATH = "ml/data/dataset_meteo.csv"

ACTIVITES = [
    "Pique-nique au parc",
    "Balade à vélo",
    "Randonnée en forêt",
    "Barbecue",
    "Balade en ville",
    "Cinéma",
    "Musée / Expo",
    "Sport en salle"
]

def generate_data():
    data = []
    # On calcule combien de lignes il faut par activité (600 / 8 = 75)
    samples_per_activity = NUM_SAMPLES // len(ACTIVITES)
    
    for activite in ACTIVITES:
        for _ in range(samples_per_activity):
            # Génération de la météo SPÉCIFIQUE à l'activité
            if activite == "Pique-nique au parc":
                temp = round(random.uniform(18, 32), 1)
                precip = 0.0
                vent = round(random.uniform(0, 15), 1)
                cond = 0
            elif activite == "Barbecue":
                temp = round(random.uniform(20, 35), 1)
                precip = 0.0
                vent = round(random.uniform(0, 15), 1)
                cond = 0
            elif activite == "Balade à vélo":
                temp = round(random.uniform(15, 25), 1)
                precip = round(random.uniform(0, 0.5), 1) # Tolère une micro goutte
                vent = round(random.uniform(0, 20), 1)
                cond = 0 if precip == 0 else 1
            elif activite == "Randonnée en forêt":
                temp = round(random.uniform(10, 22), 1)
                precip = round(random.uniform(0, 1.5), 1)
                vent = round(random.uniform(0, 25), 1)
                cond = 0 if precip == 0 else 1
            elif activite == "Balade en ville":
                temp = round(random.uniform(10, 25), 1)
                precip = round(random.uniform(0, 2.5), 1)
                vent = round(random.uniform(0, 30), 1)
                cond = 1 if precip > 0 else 0
            elif activite == "Musée / Expo":
                temp = round(random.uniform(-5, 15), 1)
                precip = round(random.uniform(1.0, 10.0), 1)
                vent = round(random.uniform(10, 40), 1)
                cond = 2 if precip <= 5 else 3
            elif activite == "Cinéma":
                temp = round(random.uniform(-5, 35), 1)
                precip = round(random.uniform(5.0, 15.0), 1) # Grosse pluie
                vent = round(random.uniform(20, 70), 1)
                cond = 3
            elif activite == "Sport en salle":
                # Temps froid ou pluvieux
                temp = round(random.uniform(-10, 12), 1) 
                precip = round(random.uniform(2.0, 15.0), 1)
                vent = round(random.uniform(10, 80), 1)
                cond = 2 if precip <= 5 else 3
            
            # Ajustement logique de l'humidité
            if precip > 0:
                humidite = round(random.uniform(70, 95), 1)
            else:
                humidite = round(random.uniform(30, 65), 1)

            data.append([temp, precip, vent, humidite, cond, activite])

    # On mélange tout le dataset pour que l'IA n'apprenne pas dans l'ordre
    random.shuffle(data)

    # Création du DataFrame
    df = pd.DataFrame(data, columns=["temperature", "precipitation", "vent", "humidite", "condition", "activite"])
    
    # Sauvegarde()
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    df.to_csv(FILE_PATH, index=False)
    
    print(f"✅ Dataset généré avec succès : {NUM_SAMPLES} lignes dans {FILE_PATH}")
    print("\nDistribution des activités :")
    print(df['activite'].value_counts())

if __name__ == "__main__":
    generate_data()