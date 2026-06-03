# par-Impar – Mayor-numero
#*****************************************
#**    Desarrollado por: Hector Lavoe   **
#*****************************************
# inicia desarrollo de la funciín dada

# cuando imprime resultado
# en el print "Su nommbre y la salida del resultado de la función"
# compruebe buen funcionamiento


# Par 4 – FunsionG4.py
# Lista-Número – Lista-Contenido
# *****************************************
# Estudiante 1: Juan Miranda
# *****************************************

def cantidad_elementos(lista):
    return len(lista)

print("Estudiante 1:", cantidad_elementos([1, 2, 3, 4, 5]))


# Estudiante 2: Melany Rodriguez

def valor_minimo(lista):
    return min(lista)

print("Estudiante 2:", valor_minimo([8, 3, 12, 1, 9]))

#***************************************
# Desarrollado por: Roger Herrera
#***************************************

def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

print("Roger Herrera:", par_impar(8))


#****Desarrollado por Meylin Hill****

def mayor_numero(a, b):
    if a > b:
        return a
    else:
        return b

print("Meylin Hill:", mayor_numero(10, 25))

