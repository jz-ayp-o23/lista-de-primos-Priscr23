"""
Diseña un programa para encontrar la lista de números primos menores o iguales a un número entero dado.
750722
"""
#Entradas 
numero = int(input("Introduzca un número: "))

#Proceso
if numero > 0:
    for i in range (1, numero):
        creciente = 2
        es_primo = True
        while es_primo and creciente < i:
            if i % creciente == 0:
                es_primo = False
            else:
                creciente += 1
        if es_primo:
            print(f"Los números menores o iguales a {numero} son: {i}")





