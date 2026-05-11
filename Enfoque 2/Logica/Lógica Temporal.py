eventos = [
    "lluvia",
    "trafico",
    "tarde"
]

for i in range(len(eventos) - 1):

    actual = eventos[i]

    siguiente = eventos[i + 1]

    print(
        actual,
        "-> después ocurre ->",
        siguiente
    )

if "lluvia" in eventos and "trafico" in eventos:

    print(
        "\nRegla temporal válida"
    )