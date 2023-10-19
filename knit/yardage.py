def calculate_yardage(pattern, size, stitch_count, row_count):
    # Dictionnaire de métrage par type de fil
    yardage_per_type = {
        "Laine fine": 200,  # mètres par 100 g
        "Coton épais": 150,
        "Alpaga moyen": 180,
        # Ajoutez d'autres types de fil avec leur métrage ici
    }

    if pattern in yardage_per_type:
        meters_per_100g = yardage_per_type[pattern]
        total_meters = (stitch_count * row_count * meters_per_100g) / (100 * 100)
        return f"Pour un projet de taille {size} avec du fil de type {pattern}, vous aurez besoin d'environ {total_meters:.2f} mètres de fil."
    else:
        return "Type de fil non valide."

pattern = "Laine fine"  # Type de fil
size = "Moyen"  # Taille du projet
stitch_count = 400  # Nombre de mailles
row_count = 500  # Nombre de rangs

print(calculate_yardage(pattern, size, stitch_count, row_count))
