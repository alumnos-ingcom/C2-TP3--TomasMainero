from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):
    resta = dividendo - divisor
    return resta

def prueba():
    #Aca se ingresan los valores de la division
    dividendo = ingreso_entero("Ingrese el dividendo")
    divisor = ingreso_entero("Ingrese el divisor")
    #Aca hago la variables vacias para usar despues
    cociente = 0
    
    #Aca se hace la division
    while dividendo >= divisor:
        division = division_lenta(dividendo, divisor)
        dividendo = dividendo - divisor
        resto = dividendo - divisor
        cociente = cociente + 1
        
    resto = dividendo
    
    print(f"El cociente de la division es #{cociente}, y el resto es #{resto}")

if __name__ == "__main__":
    prueba()