def generate_knit_chart(rows, stitches):
    chart = []

    for row in range(rows):
        if row % 2 == 0:
            chart.append(" " + " ".join("K P" * (stitches // 4)) + " ")
        else:
            chart.append(" " + " ".join("P K" * (stitches // 4)) + " ")

    return "\n".join(chart)

rows = 10  # Le nombre de rangs
stitches = 20  # Le nombre de mailles par rang

print(generate_knit_chart(rows, stitches))
