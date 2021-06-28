from tp4ej1 import ingreso_entero


def factores_primos(numero):
        
        lista = []
        
        for i in range (2, numero + 1):
            while numero % i == 0:
                lista.append(i)
                numero = numero / i
        return lista
    
def prueba():
    #Se solicita ingreso de numero
    numero = ingreso_entero("Ingrese un numero para encontrar sus factores primos")
    factores = (factores_primos(numero))
    print(factores)


if __name__ == "__main__":
    prueba()