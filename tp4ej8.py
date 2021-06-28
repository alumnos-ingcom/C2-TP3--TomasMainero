from tp4ej1 import ingreso_entero

def ordenar_mayor_a_menor(uno, dos, tres):
    valor_maximo = max (lista)
    valor_minimo = min (lista)
    valor_medio = (lista) - lista[{valor_maximo}] - [{valor_minimo}]
    return (valor_maximo, valor_minimo)

def ordenar_menor_a_mayor(uno, dos, tres):
    
    return menor_a_mayor

def prueba():
    lista = []
    numero_1 = []
    numero_2 = []
    numero_3 = []
    numeros_por_ingresar= 3
    #Aca se crea la lista a ordenar
    print("Ingrese 3 numeros")
    while numeros_por_ingresar > 0:
        numeros_por_ingresar = numeros_por_ingresar -1
        numero = ingreso_entero("Ingrese un numero")
        lista.append(numero)
        print(f"Se agrego {numero} a la lista")
  
    #Aca se ordena de mayor a menor
        valor_maximo, valor_minimo = ordenar_mayor_a_menor(numero_1, numero_2, numero_3)
        
        
if __name__ == "__main__":
    prueba()