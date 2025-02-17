import random

# Variables globales para almacenar estadísticas
historico = []
estadisticas_jugador1 = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
estadisticas_jugador2 = {"ganadas": 0, "perdidas": 0, "empatadas": 0}

# Función para mostrar el menú principal
def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Jugar")
        print("2. Reglas del juego")
        print("3. Salir del juego")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_jugar()
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Función para mostrar las reglas del juego
def mostrar_reglas():
    print("\n--- REGLAS DEL JUEGO ---")
    print("1. Piedra gana a Tijera.")
    print("2. Papel gana a Piedra.")
    print("3. Tijera gana a Papel.")
    print("4. Si ambos jugadores eligen lo mismo, es un empate.")
    print("\nModos de juego:")
    print("- 1 solo jugador: Juegas contra la computadora.")
    print("- Contra la computadora: Similar al modo de 1 jugador.")
    print("- Multijugador: Dos jugadores compiten entre sí.")
    input("Presione Enter para regresar al menú principal...")

# Función para determinar el ganador de una partida
def determinar_ganador(jugador1, eleccion1, jugador2, eleccion2):
    if eleccion1 == eleccion2:
        return "Empate"
    elif (eleccion1 == "piedra" and eleccion2 == "tijera") or \
         (eleccion1 == "papel" and eleccion2 == "piedra") or \
         (eleccion1 == "tijera" and eleccion2 == "papel"):
        return f"Ganó {jugador1}"
    else:
        return f"Ganó {jugador2}"

# Función para jugar una partida
def jugar_partida(jugador1, jugador2, modo):
    opciones = ["piedra", "papel", "tijera"]
    print(f"\n{jugador1}, elige una opción:")
    eleccion1 = input("1. Piedra\n2. Papel\n3. Tijera\nOpción: ").lower()
    if eleccion1 == "1":
        eleccion1 = "piedra"
    elif eleccion1 == "2":
        eleccion1 = "papel"
    elif eleccion1 == "3":
        eleccion1 = "tijera"
    else:
        print("Elección no válida. Se asignará 'piedra' por defecto.")
        eleccion1 = "piedra"

    if modo == "computadora":
        eleccion2 = random.choice(opciones)
        print(f"{jugador2} eligió: {eleccion2}")
    else:
        print(f"\n{jugador2}, elige una opción:")
        eleccion2 = input("1. Piedra\n2. Papel\n3. Tijera\nOpción: ").lower()
        if eleccion2 == "1":
            eleccion2 = "piedra"
        elif eleccion2 == "2":
            eleccion2 = "papel"
        elif eleccion2 == "3":
            eleccion2 = "tijera"
        else:
            print("Elección no válida. Se asignará 'piedra' por defecto.")
            eleccion2 = "piedra"

    resultado = determinar_ganador(jugador1, eleccion1, jugador2, eleccion2)
    print(f"\nResultado: {resultado}")
    return resultado

# Función para mostrar el menú de opciones para jugar
def menu_jugar():
    global historico, estadisticas_jugador1, estadisticas_jugador2
    print("\n--- MENÚ DE OPCIONES PARA JUGAR ---")
    print("1. 1 solo jugador")
    print("2. Contra la computadora")
    print("3. Multijugador (2 jugadores)")
    print("4. Ver estadísticas de la última partida")
    print("5. Regresar al menú principal")
    opcion = input("Seleccione una opción: ")

    if opcion == "1" or opcion == "2" or opcion == "3":
        # Pedir nombres de los jugadores
        jugador1 = input("Ingrese el nombre del Jugador 1: ")
        if opcion == "3":
            jugador2 = input("Ingrese el nombre del Jugador 2: ")
            modo = "multijugador"
        else:
            jugador2 = "Computadora"
            modo = "computadora"

        # Preguntar si desea definir un número de partidas
        definir_partidas = input("¿Desea definir un número de partidas? (s/n): ").lower()
        if definir_partidas == "s":
            num_partidas = int(input("Ingrese el número de partidas: "))
        else:
            num_partidas = None

        # Iniciar partidas
        historico = []
        estadisticas_jugador1 = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
        estadisticas_jugador2 = {"ganadas": 0, "perdidas": 0, "empatadas": 0}
        partida_actual = 1

        while True:
            print(f"\n--- PARTIDA {partida_actual} ---")
            resultado = jugar_partida(jugador1, jugador2, modo)
            historico.append(resultado)

            if "Ganó" in resultado:
                if jugador1 in resultado:
                    estadisticas_jugador1["ganadas"] += 1
                    estadisticas_jugador2["perdidas"] += 1
                else:
                    estadisticas_jugador2["ganadas"] += 1
                    estadisticas_jugador1["perdidas"] += 1
            else:
                estadisticas_jugador1["empatadas"] += 1
                estadisticas_jugador2["empatadas"] += 1

            if num_partidas is None:
                continuar = input("¿Desea jugar otra partida? (s/n): ").lower()
                if continuar != "s":
                    break
            elif partida_actual >= num_partidas:
                break

            partida_actual += 1

        # Mostrar historial y estadísticas
        print("\n--- HISTÓRICO ---")
        print(f"Número de partidas realizadas: {len(historico)}")
        for i, resultado in enumerate(historico, start=1):
            print(f"Partida {i}: {resultado}")

        print("\n--- ESTADÍSTICAS ---")
        print(f"{jugador1}: Ganó {estadisticas_jugador1['ganadas']} partidas, Perdió {estadisticas_jugador1['perdidas']} partidas, Empató {estadisticas_jugador1['empatadas']} partidas")
        print(f"{jugador2}: Ganó {estadisticas_jugador2['ganadas']} partidas, Perdió {estadisticas_jugador2['perdidas']} partidas, Empató {estadisticas_jugador2['empatadas']} partidas")

    elif opcion == "4":
        if not historico:
            print("No hay estadísticas recientemente.")
        else:
            print("\n--- ÚLTIMO HISTÓRICO ---")
            print(f"Número de partidas realizadas: {len(historico)}")
            for i, resultado in enumerate(historico, start=1):
                print(f"Partida {i}: {resultado}")

            print("\n--- ÚLTIMAS ESTADÍSTICAS ---")
            print(f"Jugador 1: Ganó {estadisticas_jugador1['ganadas']} partidas, Perdió {estadisticas_jugador1['perdidas']} partidas, Empató {estadisticas_jugador1['empatadas']} partidas")
            print(f"Jugador 2: Ganó {estadisticas_jugador2['ganadas']} partidas, Perdió {estadisticas_jugador2['perdidas']} partidas, Empató {estadisticas_jugador2['empatadas']} partidas")

    elif opcion == "5":
        return
    else:
        print("Opción no válida. Intente nuevamente.")

# Función principal
def main():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    menu_principal()

if __name__ == "__main__":
    main()