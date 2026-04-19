# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# import pickle
# import numpy as np
# # Étape 2 : Charger le dataset
# df = pd.read_csv('ml/data/dataset_meteo.csv')

# # Étape 3 : Séparer les features (entrées) et la cible (sortie)
# X_raw = df[['temperature', 'precipitation', 'vent', 'humidite', 'condition']]
# y_raw = df['activite']

# # Étape 4 : Normaliser avec MinMaxScaler
# scaler = MinMaxScaler()
# X = scaler.fit_transform(X_raw)

# # Étape 5 : Encoder les labels (la cible)
# encoder = LabelEncoder()
# y = encoder.fit_transform(y_raw)

# # Étape 6 : Split train/test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Étape 7 : Sauvegarder scaler et encoder
# pickle.dump(scaler, open('ml/src/scaler.pkl', 'wb'))
# pickle.dump(encoder, open('ml/src/encoder.pkl', 'wb'))

# # Étape 8 : Afficher et vérifier
# print(f"Dimensions X_train : {X_train.shape}")
# print(f"Distribution y_train : {np.unique(y_train, return_counts=True)}")


# # --- VÉRIFICATION VISUELLE ---
# print("✅ Script exécuté avec succès !")
# print(f"Nombre de lignes pour l'entraînement : {X_train.shape[0]}")
# print(f"Nombre de lignes pour le test : {X_test.shape[0]}")
# print(f"Exemple de données normalisées (1ère ligne) : \n{X_train[0]}")
# print(f"Exemple de label encodé (1ère ligne) : {y_train[0]}")

"""
preprocess.py
Transforme le dataset CSV en tableaux numpy prêts pour Keras.
Sauvegarde le scaler et l'encoder pour les réutiliser dans FastAPI.
"""
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# ─── 1. Chargement ────────────────────────────────────────────────────────────
df = pd.read_csv("ml/data/dataset_meteo.csv")
print(f"Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
print(df.head(3))

# ─── 2. Séparation features / cible ──────────────────────────────────────────
X_raw = df[["temperature", "precipitation", "vent", "humidite", "condition"]]
y_raw = df["activite"]

print(f"\nFeatures shape : {X_raw.shape}")
print(f"Classes uniques : {y_raw.unique()}")

# ─── 3. Normalisation des features (0 à 1) ───────────────────────────────────
scaler = MinMaxScaler()
X = scaler.fit_transform(X_raw)

print(f"\nAprès normalisation :")
print(f"  Min global : {X.min():.4f}")
print(f"  Max global : {X.max():.4f}")
print(f"  Exemple première ligne avant : {X_raw.iloc[0].values}")
print(f"  Exemple première ligne après : {X[0].round(4)}")

# ─── 4. Encodage des labels (texte → entier) ─────────────────────────────────
encoder = LabelEncoder()
y = encoder.fit_transform(y_raw)

print(f"\nMapping des activités :")
for i, activite in enumerate(encoder.classes_):
    print(f"  {i} → {activite}")

print(f"\nExemple : y_raw[0] = '{y_raw.iloc[0]}' → y[0] = {y[0]}")

# ─── 5. Split train / test ────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nDimensions après split :")
print(f"  X_train : {X_train.shape}")
print(f"  X_test  : {X_test.shape}")
print(f"  y_train : {y_train.shape}")
print(f"  y_test  : {y_test.shape}")

# ─── 6. Sauvegarde scaler et encoder ─────────────────────────────────────────
pickle.dump(scaler,  open("ml/src/scaler.pkl",  "wb"))
pickle.dump(encoder, open("ml/src/encoder.pkl", "wb"))

print(f"\nFichiers sauvegardés :")
print(f"  ml/src/scaler.pkl")
print(f"  ml/src/encoder.pkl")

# ─── 7. Vérification du rechargement pickle ───────────────────────────────────
scaler2  = pickle.load(open("ml/src/scaler.pkl",  "rb"))
encoder2 = pickle.load(open("ml/src/encoder.pkl", "rb"))

test_input = [[20.0, 0.0, 10.0, 55.0, 0]]
test_scaled = scaler2.transform(test_input)
print(f"\nTest rechargement scaler :")
print(f"  Entrée brute  : {test_input[0]}")
print(f"  Entrée scalée : {test_scaled[0].round(4)}")
print(f"  Classes encoder rechargé : {encoder2.classes_}")

# ─── 8. Vérification distribution des classes ─────────────────────────────────
print(f"\nDistribution des classes dans y_train :")
unique, counts = np.unique(y_train, return_counts=True)
for u, c in zip(unique, counts):
    print(f"  {encoder.classes_[u]} : {c} exemples")
