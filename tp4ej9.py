from tp4ej1 import ingreso_entero

def es_primo(numero):
    contador = 0
    for i in range (1, numero+1):
        if numero % i == 0:
            contador = contador + 1
    if contador == 2:
        return("es primo")
    else:
        return("es compuesto")

def prueba():
    #Aca se solicita el ingreso del numero a analizar
    numero = ingreso_entero("Ingrese un numero para ver si es primo o compuesto")
    #Aca se realiza la prueba
    resultado = es_primo(numero)
    print(f"El numero {resultado}")
    
    
    
if __name__ == "__main__":
    prueba()