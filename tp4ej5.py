from tp4ej1 import ingreso_entero

def signo(numero):
    """
    Aca se aprovecha la ley de los signos para deducir cual es el signo
    del numero ingresado
    """
    if - numero > 0:
        return print("El numero es negativo (-)")
    elif - numero < 0:
        return print("El numero es positivo (+)")
    else:
        return print("El numero es 0")
    
def prueba():
   numero = ingreso_entero("Ingrese un numero para luego ver su signo")
   signo_del_numero = signo(numero)
    
if __name__ == "__main__":
    prueba()