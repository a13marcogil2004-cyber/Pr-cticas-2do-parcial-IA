prob_spam = 0.4

prob_palabra_spam = 0.8

prob_palabra = 0.5

resultado = (
    prob_palabra_spam
    *
    prob_spam
) / prob_palabra

print(
    "Probabilidad de spam:"
)

print(round(resultado, 4))

if resultado > 0.5:

    print("\nCorreo clasificado como SPAM")

else:

    print("\nCorreo NO SPAM")