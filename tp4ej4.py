from tp4ej1 import ingreso_entero

def comparacion_numeros(num_1, num_2):
    """Aca se comparan los numeros"""
    if num_1 > num_2:
        return 1
    elif num_1 < num_2:
        return -1
    else:
        return 0

def prueba():
    """Aca se pide el ingreso de 2 numeros"""
    num_1 = ingreso_entero("Ingrese un numero")
    num_2 = ingreso_entero("Ingrese otro numero")
    """Aca se devuelve el resultado"""
    resultado = comparacion_numeros(num_1, num_2)
    print(f"El resultado es {resultado}")

if __name__ == "__main__":
    prueba()