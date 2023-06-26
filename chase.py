import time


def lights_out(tablero):


    def imprimir_tablero(tablero):
        print('    ', end='')
        for col in range(5):
            print(col, end=' ')
        print('\n  ', end='')
        print('- ' * 6)

        for i, fila in enumerate(tablero):
            print(i, '|', end=' ')
            for valor in fila:
                print(valor, end=' ')
            print()

    def switch(n):
        if n == 1:
            return 0
        else:
            return 1

    def apagar(x, y, actual):
        actual[x][y] = switch(actual[x][y])
        if y + 1 <= 4:
            actual[x][y + 1] = switch(actual[x][y + 1])
        if y - 1 >= 0:
            actual[x][y - 1] = switch(actual[x][y - 1])
        if x + 1 <= 4:
            actual[x + 1][y] = switch(actual[x + 1][y])
        if x - 1 >= 0:
            actual[x - 1][y] = switch(actual[x - 1][y])

        if solucion(actual):
            print('------------------------------------------------')
            print('Se encontro solucion para el conjunto de luces: ')
            print(conjunto)
            print('------------------------------------------------')
            imprimir_tablero(actual)
            end_time = time.time()  # Tiempo final
            execution_time = end_time - start_time
            print()
            print('Greedy - tiempo de ejecución:',
                  execution_time, 'segundos')
            exit()

    def solucion(actual):
        for fila in actual:
            if 1 in fila:
                return False

        return True

    def selec_luz(conjunto, actual):
        # Recorre lista de arreglos
        for i in range(5):
            arreglo = actual[i]
            # Recorre valores del arreglo
            for j in range(5):
                valor = arreglo[j]

                if valor == 1 and i < 4:
                    # Guarda y retorna indices de la celda inferior
                    pick = str(i + 1) + str(j)
                    conjunto.append(pick)
                    return (i + 1, j, conjunto)

        return (0, 0, conjunto)

    def chase_lights(conjunto):
        for i in range(5):
            # Selección Persiguiendo
            for j in range(5):
                # Selecciona celda, si no hay a cual seguir devuelve x=0
                x, y, conjunto = selec_luz(conjunto, actual)

                # Sale del bucle si x=0, no tiene solución persiguiendo
                if x == 0:
                    break

                # Cambia el estado de la celda seleccionada
                apagar(x, y, actual)
        return actual

    def patron(actual,conjunto):
        if actual[4]==[0,0,1,1,1]:
            apagar(0,3,actual)
            conjunto.append(str(0)+str(3))
        if actual[4]==[0,1,0,1,0]:
            apagar(0,1,actual)
            apagar(0,4,actual)
            conjunto.append(str(0) + str(1))
            conjunto.append(str(0) + str(4))
        if actual[4]==[0,1,1,0,1]:
            apagar(0,0,actual)
            conjunto.append(str(0) + str(0))
        if actual[4]==[1,0,0,0,1]:
            apagar(0,3,actual)
            apagar(0,4,actual)
            conjunto.append(str(0) + str(3))
            conjunto.append(str(0) + str(4))
        if actual[4]==[1,0,1,1,0]:
            apagar(0,4,actual)
            conjunto.append(str(0) + str(4))
        if actual[4]==[1,1,0,1,1]:
            apagar(0,2,actual)
            conjunto.append(str(0) + str(2))
        if actual[4]==[1,1,1,0,0]:
            apagar(0,1,actual)
            conjunto.append(str(0) + str(1))

    # Resolución
    print('Tablero inicial: ')
    actual = tablero
    imprimir_tablero(actual)
    start_time = time.time()  # Tiempo inicial
    conjunto = []
    actual = chase_lights(conjunto)
    patron(actual,conjunto)
    actual = chase_lights(conjunto)

    print('No se encontró solucion')


tablero = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1]
]
lights_out(tablero)


# {11,14,40,44}
'''
Con tecnica
[
    [0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

Sin tecnica
[
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1]
]

'''