def calculate_skeins_needed(desired_length, meters_per_skein, grams_per_skein):
    total_meters = desired_length
    meters_per_gram = meters_per_skein / grams_per_skein
    skeins_needed = total_meters / meters_per_skein

    return f"Pour un projet nécessitant {total_meters} mètres de fil, vous aurez besoin d'environ {skeins_needed:.2f} écheveaux."

# Exemple d'utilisation
desired_length = 300  # Nombre de mètres nécessaires pour le projet
meters_per_skein = 400  # Longueur par écheveau en mètres
grams_per_skein = 100  # Poids par écheveau en grammes

print(calculate_skeins_needed(desired_length, meters_per_skein, grams_per_skein))
