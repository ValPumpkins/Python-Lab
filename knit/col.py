import random

def generate_knit_color_name():
    adjectives = ["Chaud", "Doux", "Léger", "Mousseux", "Épais", "Givré", "Pastel", "Vif", "Foncé", "Pâle", "Éclatant", "Rustique", "Brillant"]
    colors = ["Rouge", "Bleu", "Vert", "Rose", "Jaune", "Violet", "Gris", "Marron", "Or", "Argent", "Blanc", "Noir"]

    adjective = random.choice(adjectives)
    color = random.choice(colors)

    return f"{adjective} {color}"

for _ in range(5):  # Génère 5 noms de couleurs
    print(generate_knit_color_name())
