def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos > 0:
        try:
            valor = ingreso_entero(mensaje)
            return valor 
        except IngresoIncorrecto as error:
            cantidad_reintentos = cantidad_reintentos - 1
            print(f"te quedan {cantidad_reintentos}")
    raise IngresoIncorrecto("te quedaste si intentos")
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    pass
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 

def prueba():
    mi_numero = ingreso_entero_reintento("ingrese un numero")
    print(f"mi numero es {mi_numero}")

if __name__ == "__main__":
    prueba()