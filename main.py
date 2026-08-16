
import random

# funcion del juego


def juego():
    # bienvenida (solo sale al principio)
    print("Intenta adivinar la palabra!")

    lista_palabras = ["pan", "manzana", "claude", "yona", "python", "gato", "perro", "casa",
                      "arbol", "sol", "luna", "estrella", "montana", "rio", "mar", "playa",
                      "libro", "mesa", "silla", "puerta", "ventana", "carro", "bicicleta",
                      "computadora", "teclado", "mouse", "pantalla", "camisa", "zapato",
                      "sombrero", "reloj", "espejo", "jardin", "flor", "hoja", "lluvia",
                      "nube", "viento", "fuego", "tierra", "agua", "piedra", "arena",
                      "bosque", "desierto", "isla", "puente", "torre", "castillo", "dragon",
                      "tigre"]  # lista de posibles palabras

    # Variables!
    # genera un numero entre 0 y 4 aleatorio, para elegir una de las palabras de "lista_palabras"
    numero_palabra = random.randint(0, 50)

    # la palabra secreta sera la que corresponde en la lista "lista_palabras" segun el numero random
    palabra_secreta = lista_palabras[numero_palabra]

    # la palabra secreta se divide en leras dentro de la lista "letras"
    letras = list(palabra_secreta)
    cantidad_letras = len(letras)   # cantidad de letras en la palabra secreta
    # cantidad de letras en la palabra secreta, sin repetir letras
    cantidad_letras_unicas = len(set(letras))

    resultado = []  # resultado, una lista vacia al principio
    letras_usadas = []  # letras_usadas va a almacenar las letras que sean ingresadas

    for l in letras:
        # la lista "resultado" se llenara con un "_" por cada letra de la palabra_secreta
        resultado.append("_")

    intentos = 0  # se le asignara una cantidad de intentos segun el modo de juego
    # la variable ronda comienza en 1, aumenta cada vez que ingresa una letra (nueva)
    ronda = 1
    # la variable comienza en 0, aumenta cada vez que acierta una letra.
    puntuacion_obtenida = 0
    puntuacion_maxima = 0  # se inicia en 0, se guardara la puntuacion maxima obtenible
    puntuacion_final = 0  # se guardara la puntuacion final que el jugador vera
    aciertos = 0  # guarda la cantidad de aciertos
    fallos = 0  # almacena la cantidad de fallos

    # Menu
    eligiendo_modo = True  # variable que controla el ciclo de menu
    while eligiendo_modo:  # ciclo de menu para elegir modo
        print("Modos de juego\n1. Casual - 15 intentos\n2. Desafio - 8 a 12 intentos (aleatorio)")
        # el jugador elige el modo
        modo_juego = input("Elige un Modo (1 o 2): ")
        # Condicion 1
        if modo_juego == "1":  # si el jugador elige "1":
            intentos = 15  # se establece maximo de intentos es 15 para modo Casual
            print("\nHaz seleccionado modo: Casual! Intentos disponibles: ", intentos)
            eligiendo_modo = False  # se detiene el ciclo de menu
        elif modo_juego == "2":
            # el maximo de intentos es aleatorio entre 8 y 12 para modo Desafio
            intentos = random.randint(8, 12)
            print("\nHaz seleccionado modo: Desafio! Intentos disponibles: ", intentos)
            eligiendo_modo = False  # se detiene el ciclo menu
        else:
            #  la opcion no es valida, se reinicia el menu
            print("\nNo se encuenta modo: ", modo_juego,
                  "\nPor favor, Ingresa una opcion valida (1 o 2)\n")

    # la puntuacion maxima se calcula: la cantidad de letras de la palabra multiplicada por los intentos (maximos) menos la cantidad de letras sin repetir
    puntuacion_maxima = cantidad_letras * ((intentos - cantidad_letras_unicas))

    print(
        "\nIntenta encontrar la palabra correcta!"
        "\nLa palabra tiene: ", cantidad_letras, "letras"
        "\nAdvertencia! cada fallo resta puntos al puntaje final")
    # Juego
    # mientras "jugando" este en "True" el ciclo while del juego se seguira ejecutando
    jugando = True
    while jugando:

        print("\nInformacion de la partida: ")
        print("Ronda actual :", ronda)  # muestra la ronda actual
        # muestra los intentos restantes
        print("Intentos restantes: ", intentos)
        # Imprime la lista resultado, mostrando el estado actual
        print("Estado actual: ", resultado)

        # se solicita una letra al usuario y se guarda en letra_ingresada.
        letra_ingresada_base = input("ingrese una letra: ")
        # letra_ingresada se transforma en minuscula para que no haya error de comparacion.
        letra_ingresada = letra_ingresada_base.lower()

        # Condicion 2
        # se evalua que la letra no haya sido ingresada antes
        if letra_ingresada in letras_usadas:
            # si ya habia sido usada muestra un mensaje
            print("\nLa letra: '", letra_ingresada,
                  "' Ya habia sido usada! \nIngresa una letra diferente")
            print("No pierdes intentos! Reiniciando ronda... :)")
            continue  # reinicia el ciclo de juego, a elegir letra de nuevo
        else:
            # si no habia sido usada, se agrega a la lista letras_usadas
            letras_usadas.append(letra_ingresada)

        # recorre cada letra de la lista "letras", y lleva conteo del indice.
        for i, l in enumerate(letras):
            # Condicion 3
            # si una letra de la lista coincide con letra_ingresada:
            if l == letra_ingresada:
                # reemplaza "_" por la letra que coindice justo en el lugar donde correspone.
                resultado[i] = l
                puntuacion_obtenida += 1  # agrega 1 puntos a la puntuacion

        # condicion 4
        # se cuenta cuantas veces aparece esa letra
        aparece = letras.count(letra_ingresada)
        if aparece == 1:
            print("\nLa letra: '", letra_ingresada, "' Aparece:",
                  aparece, "vez en la palabra secreta!")
            aciertos += 1
        elif aparece == 0:
            print("\nLa letra: '", letra_ingresada,
                  "' No aparece en la palabra secreta!")
            fallos += 1
        else:
            print("\nLa letra: '", letra_ingresada, "' Aparece:",
                  aparece, "veces en la palabra secreta!")
            aciertos += 1

        intentos -= 1  # se resta 1 a los intentos disponibles

        # Condicion 5
        # si la lista resultado es igual a la lista letras, adivino la palabra completa
        if resultado == letras:  # compara si la lista resultado es igual a la lista letras
            # si es igual, se calcula la puntuacion y muestra mensaje de juego ganado.
            # calcula la puntuacion, multiplicando por intentos restantes
            puntuacion_obtenida = puntuacion_obtenida * intentos
            # se calcula la puntuacion final dividiendo la puntuacion obtenida entre la puntuacion maxima, y se multiplica por 100
            puntuacion_final = (puntuacion_obtenida / puntuacion_maxima) * 100

            print(
                "\nJuego Terminado!\n"
                "\nFelicidades! Haz encontrado la palabra con exito!"
                "\nResultados:"
                "\nPalabra secreta encontrada: ", palabra_secreta,
                "\nRondas jugadas: ", ronda,          # muestra la cantidad de rondas jugadas
                "\nIntentos sobrantes: ", intentos,   # los intentos restantes tras ganar
                "\nAciertos: ", aciertos,           # muestra la contidad de aciertos
                "\nFallos: ", fallos,               # muestra el total de fallos
                # salida esperada: 90/100, 100/100, 50/100, etc...
                f"\nPuntuacion Final: {puntuacion_final:.0f}/100"
            )
            if puntuacion_final == 100:  # mensaje cuando hay puntuacion perfecta
                print("Puntuacion Perfecta! Eres increible :O")
            elif intentos == 0:  # mensaje cuando se gana al ultimo intento xd
                print("'La ultima es la vencida', eh? Ganaste por un pelo"
                      "\nSin intentos restantes la puntuacion es 0, ganas pero no ganas nada")
            jugando = False  # Cuando se pone "= Flase" detiene el while del juego

        elif intentos == 0:  # evalua si los intentos restantes es igual a 0
            # si los intentos restantes son 0, muestra mensaje de juego perdido
            print(
                "\nJuego termidado!\n"
                "\nQue lastima... perdiste"
                "\nResultados:"
                "\nTu estado final: ", resultado,     # muestra la lista de letras encontradas
                # muestra la palabra secreta que se buscaba
                "\nPalabra secreta: ", palabra_secreta,
                "\nRondas jugadas: ", ronda,          # muestra la cantidad de rondas jugadas
                "\nAciertos: ", aciertos,           # muestra la contidad de aciertos
                "\nFallos: ", fallos,               # muestra el total de fallos
                # salida esperada: 4/100, 10/100, 12/100, etc...
                f"\nPuntuacion Final: {puntuacion_final:.0f}/100"
                "\nMejor suerte a la proxima"
            )
            if aciertos == 0:  # mensaje si no acierta ninguna letra XDD
                print("Siquiera era posible no acertar ninguna letra...?")
            jugando = False  # Termina el juego

        ronda += 1  # suma 1 a la variable ronda cada que inicia el ciclo


juego()  # inicia el programa
