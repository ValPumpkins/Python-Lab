import random

def generate_knit_pattern(rows, stitches):
    pattern = ""
    knit_symbols = ["K", "P", "YO", "K2tog", "SSK"]

    for row_num in range(1, rows + 1):
        row = f"Row {row_num}: "
        for stitch_num in range(1, stitches + 1):
            symbol = random.choice(knit_symbols)
            if symbol in ["K", "P"]:
                symbol += str(random.randint(1, 9))  # Ajouter un nombre aléatoire de 1 à 9
            row += symbol + " "
        pattern += row + "\n"

    return pattern

rows = 10  # nb de rangs
stitches = 20  # nb de mailles par rang

print(generate_knit_pattern(rows, stitches))
