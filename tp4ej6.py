from tp4ej1 import ingreso_entero

def minimo(lista):
    valor_minimo = min(lista)
    return valor_minimo

def maximo(lista):
    valor_maximo = max(lista)
    return valor_maximo
    
def prueba():
    #Aca se ingresan cuantos valores habra en la lista
    cantidad_de_numeros = ingreso_entero("Ingrese cuantos valores quiere en la lista")
    #Aca genero la lista vacia para agregarle su contenido luego
    lista = []
    #Aca hago que el usuario ingrese los numeros de la lista
    while cantidad_de_numeros > 0:
        numero = ingreso_entero("Ingrese un numero")
        lista.append(numero)
        cantidad_de_numeros = cantidad_de_numeros - 1
        print(lista)
    #Aca devuelvo los valores minimos y maximos
    valor_maximo = maximo(lista)
    valor_minimo = minimo(lista)
    print(f"El valor maximo es #{valor_maximo}, y el minimo es #{valor_minimo}")    
    
    
if __name__ == "__main__":
    prueba()