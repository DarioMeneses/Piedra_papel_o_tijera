import random

def eleccion_jugador():
    print("Para empezar el juego escribe, piedra, papel o tijera")
    return input().lower()

def eleccion_pc():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def ganador(eleccion_jugador, eleccion_pc):
    if eleccion_jugador == eleccion_pc:
        return "Empate"
    elif eleccion_jugador == "piedra" and eleccion_pc == "tijera":
        return "Felicidades ¡Ganaste!"
    elif eleccion_jugador == "papel" and eleccion_pc == "piedra":
        return "Felicidades ¡Ganaste!"
    elif eleccion_jugador == "tijera" and eleccion_pc == "papel":
        return "Felicidades ¡Ganaste!"
    else:
        return "Perdiste, buena suerte en la siguiente"

def juego():
    print("Bienvenido al juego de piedra, papel y tijera")
    print("¡Vamos a jugar!")
    jugador = eleccion_jugador()
    maquina = eleccion_pc()
    print(f"Elección PC: {maquina}")
    resultado = ganador(jugador, maquina)
    print(resultado)

juego()
