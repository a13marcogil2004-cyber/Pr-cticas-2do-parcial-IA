estrategias = ["Cooperar", "Traicionar"]

pagos = {
    ("Cooperar", "Cooperar"): (-1, -1),
    ("Cooperar", "Traicionar"): (-5, 0),
    ("Traicionar", "Cooperar"): (0, -5),
    ("Traicionar", "Traicionar"): (-3, -3)
}

for a in estrategias:
    for b in estrategias:

        pago_a, pago_b = pagos[(a, b)]

        print(
            f"A:{a} | B:{b} -> "
            f"A={pago_a}, B={pago_b}"
        )