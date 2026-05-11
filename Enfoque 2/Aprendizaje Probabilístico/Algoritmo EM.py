datos = [
    2,
    4,
    6,
    8
]

media = 0

for _ in range(5):

    esperanza = (
        sum(datos)
        /
        len(datos)
    )

    media = (
        media
        +
        esperanza
    ) / 2

    print(
        "Media estimada:",
        round(media, 4)
    )