import os
import random

#MINIMO: int = 10
#MAXIMO: int = 18

# Códigos de escape ANSI para dar color al texto en la terminal.
CIAN: str = "\033[96m"
AMARILLO: str = "\033[93m"
RESET: str = "\033[0m"  # Regresa al color normal de la terminal


def mostrar_instrucciones() -> None:
    """Imprime las instrucciones del juego en un color distinto."""
    # En Windows, os.system("") activa el soporte de colores ANSI en la consola.
    if os.name == "nt":
        os.system("")

    print(f"{CIAN}{'=' * 50}")
    print("        JUEGO: VALIDAR SI EL NUMERO ES PRIMO ")
    print("=" * 50)
    print("Instrucciones:")
    print(f"  1. La computadora recibe un numero y lo va evaluar comentando si es primo o no")
    print("  2. Escribe un número entero y presiona Enter.")
    print(f"{AMARILLO}  Tip: presiona Ctrl+C para salir en cualquier momento.{CIAN}")
    print(f"{'=' * 50}{RESET}\n")


def dame_numero(mensaje: str) -> int | None:
    """Lee la entrada del usuario y la convierte a int.

    input() siempre devuelve un str; compararlo directamente con un int
    (por ejemplo "250" == 250) siempre da False. Por eso convertimos aquí.
    Devuelve None si la entrada no es un número válido dentro del rango.
    """
    texto = input(mensaje).strip()
    try:
        numero = int(texto)
        
    except ValueError:
        print(f"'{texto}' Tiene que ser un valor numerico.")
        return None

    
    return numero


def main() -> None:
    #secret = random.randint(MINIMO, MAXIMO)

    mostrar_instrucciones()
    #print(secret)  # Se mantiene para pruebas: muestra el número secreto

    while True:
        res = dame_numero("Dame un numero: ")
        if res is None:
            continue
        

        if (res <= 1):
            return False
            
        elif (res == 2):
            print("El numero 2 es un numero primo")
            break
            
        elif (res % 2 == 0):
            print(f"El numero que digitaste {res}, no es un numero primo!")
            break
        else: 
            print(f"El numero que digitaste {res}, es un numero primo!")
            break
            
            


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nJuego terminado.")
