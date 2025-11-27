import sys
from solucion import reloj_arena

def main():
    lineas = sys.stdin.read().splitlines()

    # Validar cantidad de líneas
    if len(lineas) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    altura_str = lineas[0]
    caracter_str = lineas[1]

    # Validar entero
    try:
        m = int(altura_str)
    except:
        print("Error: La altura debe ser un numero entero")
        return

    # Validar carácter no vacío
    if caracter_str == "":
        print("Error: El caracter no puede ser vacío")
        return

    # Ejecutar lógica del reloj
    resultado = reloj_arena(m, caracter_str[0])
    print(resultado)

if __name__ == "__main__":
    main()
