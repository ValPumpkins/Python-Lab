def convert_knit_size(size):
    sizes = {
        "XS": (81, 66, 86),  # Tour de poitrine, tour de taille, tour de hanches en cm
        "S": (86, 71, 91),
        "M": (91, 76, 96),
        "L": (96, 81, 101),
        "XL": (101, 86, 106),
    }

    if size in sizes:
        measurements = sizes[size]
        return f"Taille {size}: Tour de poitrine {measurements[0]} cm, Tour de taille {measurements[1]} cm, Tour de hanches {measurements[2]} cm"
    else:
        return "Taille non valide."

size = "M"  # Entrez la taille de vêtement à convertir
print(convert_knit_size(size))
