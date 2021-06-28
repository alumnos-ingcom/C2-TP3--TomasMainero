from tp4ej1 import ingreso_entero

def convertir_a_fahrenheit(centigrados):
    return (centigrados * 9/5) + 32


def convertir_a_centigrados(fahrenheit):
    return (fahrenheit - 32) * 5/9

def prueba():
    """Aca se pide que se quiere convertir"""
    unidadxconvertir = str(input("Ingrese f para convertir a fahrrenheit, o c para convertir a centigrados ") )
    f = "f"
    
    """Aca se convierte"""
    if unidadxconvertir == f:
        fahrenheit = float(ingreso_entero("Ingrese los grados fahrenheit"))
        grados_conver_centigrados = convertir_a_centigrados(fahrenheit)
        print(f"Los {fahrenheit} grados F equivalen a {grados_conver_centigrados} grados C")
    else:
        centigrados = float(ingreso_entero("Ingrese los grados centigrados"))
        grados_conver_fahrenheit = convertir_a_fahrenheit(centigrados)
        print(f"Los {centigrados} grados C equivalen a {grados_conver_fahrenheit} grados F")
        
if __name__ == "__main__":
    prueba()