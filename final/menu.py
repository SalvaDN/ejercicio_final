import time

def menu():
    print("QUIEN QUIERE SER MILLONARIO")
    print(" ")
    nombre = input("Introduce tu nombre: ")
    print(" ")
    print(f"Bienvenido {nombre}, vamos a empezar el juego en...")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("¡Empezamos!")
    time.sleep(1)
    print(" ")
    print("QUIEN QUIERE SER MILLONARIO")
    time.sleep(2)

    return nombre
