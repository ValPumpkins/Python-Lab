def knit_pattern(rows, stitches):
    pattern = []

    for i in range(rows):
        if i % 2 == 0:
            row = "|-" + " " * (stitches - 2) + "-|"
        else:
            row = "| " + " " * (stitches - 2) + " |"

        pattern.append(row)

    return "\n".join(pattern)

rows = 20  # nb de rangs
stitches = 50  # nb de mailles par rang

print(knit_pattern(rows, stitches))
