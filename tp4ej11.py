def es_palindromo(texto, texto_invertido):
    if texto == texto_invertido:
        return "true"
    else:
        return "false"


def prueba():
    #Aqui se ingresa una frase
    texto = input("Ingrese texto para analizar si es polindromo: ")
    texto_en_minuscula = texto.lower()
    texto_sin_espacios = texto_en_minuscula.replace(" ", "")
    
    texto_final = texto_sin_espacios
    texto_invertido = (texto_final[::-1])
    #Aca se hace la prueba
    resultado = es_palindromo(texto_final, texto_invertido)
    print(resultado)
    

if __name__ == "__main__":
    prueba()