################
# Tomas Mainero - @TomasMainero
# Trabajo practico 4, ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def suma_numeros(numero_1, numero_2):
    """Este indica la suma de los dos numeros"""
    return numero_1 + numero_2
    
def prueba():
    """Aca se suman los numeros"""
    numero_1 = ingreso_entero("Ingrese un numero para sumar")
    numero_2 = ingreso_entero("Ingrese otro numero para sumar")
    sumaT = numero_1 + numero_2
    """Aca se hace la suma lenta"""
    
    if numero_1 < sumaT:
        while numero_1 != sumaT:
            numero_1 = numero_1+1
            print(numero_1)
    else:
        while numero_1 != sumaT:
            numero_1 = numero_1-1
            print (numero_1)
  
if __name__ == "__main__":
    prueba()