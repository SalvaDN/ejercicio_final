import random
import api
import time
import menu

lista = api.api_preguntas()
nombre = menu.menu()
puntos = 0
comodin_usado = False
eleccion_comodin = None

# Juego
for num_preg, pregunta in enumerate(lista):
    print("\n----------------------------------------")
    print(f"Pregunta {num_preg + 1}:")

    opciones = pregunta['incorrect_answers'] + [pregunta['correct_answer']]
    random.shuffle(opciones)

    # Printeo
    print(pregunta['question'])
    for respuestas, opcion in enumerate(opciones, 1):
        print(f"{respuestas}) {opcion}")

    if not comodin_usado:
        eleccion_comodin = input("¿Quieres usar el comodin? (s/n): ")
    elif comodin_usado:
        eleccion = input("Elige la opción (1-4) (6) para plantarse): ")

    # Elegir
    if not comodin_usado and eleccion_comodin == "s":
            time.sleep(1)
            print(" ")
            print("Acabas de saltar la pregunta! jeje XD.")
            comodin_usado = True

            continue
    elif eleccion_comodin == "s":
        print(" Recordatorio: !Ya usaste el comodín¡")
    print(" ")

    time.sleep(1)
    if eleccion == '6':
        time.sleep(1)
        print(" ")
        print(f"!Te has plantado :S!")
        break
    elif eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
        if opciones[int(eleccion) - 1] == pregunta['correct_answer']:
            puntos = puntos + 1
            print(f"¡Correcto! Puntuación actual: {puntos}")
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['correct_answer']} :'(")
            puntos = 0
            break
    else:
        print("Por favor, introduce una opción válida, ¡espabila!.")

print(f"Juego terminado. Puntuación final: {puntos}")
