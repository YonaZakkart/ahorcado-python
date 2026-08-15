
import random

# funcion del juego


def juego():
    # bienvenida (solo sale al principio)
    print("Intenta adivinar la palabra!")

    lista_palabras = ["pan", "manzana", "claude",
                      "yona", "python"]  # lista de posibles palabras

    numero = random.randint(0, 4)  # genera un numero entre 0 y 4 aleatorio

    # la palabra secreta sera la que corresponde en la lista "lista_palabras" segun el numero random
    palabra_secreta = lista_palabras[numero]

    # la palabra secreta se divide en leras dentro de la lista "letras"
    letras = list(palabra_secreta)

    resultado = []  # resultado, una lista vacia al principio

    for l in letras:
        # la lista "resultado" se llenara con un "_" por cada letra de la palabra_secreta
        resultado.append("_")

    # mientras "jugando" este en "True" el ciclo while se seguira ejecutando
    jugando = True

    while jugando:

        print("\nEncuentra la palabra: ")
        print(resultado)  # Imprime la lista resultado, mostrando el estado actual

        # se solicita una letra al usuario y se guarda en letra_ingresada.
        letra_ingresada = input("ingrese una letra: ")

        for i, l in enumerate(letras):  # recorre cada letra de la lista "letras", y lleva conteo del indice.
            # letra_ingresada se transforma en minuscula para que no haya error de comparacion.
            if l == letra_ingresada.lower():
                # si una letra de la lista coincide con letra_ingresada:
                resultado[i] = l
                # reemplaza "_" por la letra que coindice justo en el lugar donde correspone.

        # si la lista resultado es igual a la lista letras, adivino la palabra completa
        if resultado == letras: # lo ideal es unir la lista resultado a una palabra y compararlo con palabra_secreta
            print("\nFelicidades, Haz acertado!")
            jugando = False # Cuando se pone "= Flase" detiene el while


juego()
