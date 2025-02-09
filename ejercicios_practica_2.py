# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    archivo = open('stock.csv')

    lista = list(csv.DictReader(archivo))

    archivo.close()
    suma = 0

    for i in lista:
        linea = i
        cant_tornillos = int(linea.get('tornillos'))
        suma += cant_tornillos
    
    print('La cantidad de tornillos es: {}'.format(suma))


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = open('propiedades.csv')
    lista = list(csv.DictReader(archivo))
    archivo.close()
    suma_2 = 0
    suma_3 = 0
    
    for i in lista:
        try:
            ambientes = int(i.get('ambientes'))

        except:
            print('Error linea {}'.format(i))  

        if ambientes == 2:
            suma_2 += 1
        
        if ambientes == 3:
            suma_3 += 1

    print('Dptos 2 ambientes: {}'.format(suma_2))
    print('Dptos 3 ambientes: {}'.format(suma_3))

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
