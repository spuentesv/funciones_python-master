# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"
nbrlst = []
# Ejercicios con funciones

def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    # En esta función debe determinar cual de los dos
    global nbrlst

    # números ingresados por parámetro es mayor
    nbrlst.append(numero_1)
    nbrlst.append(numero_2)    

    # y luego imprimir dicho valor en pantalla
    print('Valor maximo', max(nbrlst), ' Valor minimo', min(nbrlst))



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Alumno: Complete la función "imprimir_mayor"
    imprimir_mayor(2, 10)

    print("terminamos")