from random import randint
import time

def lights_out(tablero):
    inicial = tablero
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
        if n==1:
            return 0
        else:
            return 1

    def apagar(x,y,actual):
        actual[x][y] = switch(actual[x][y])
        if y+1 <= 4:
            actual[x][y+1] = switch(actual[x][y+1])
        if y-1 >= 0:
            actual[x][y-1] = switch(actual[x][y-1])
        if x+1 <= 4:
            actual[x+1][y] = switch(actual[x+1][y])
        if x-1 >= 0:
            actual[x-1][y] = switch(actual[x-1][y])

    def solucion(actual):
        for fila in actual:
            if 1 in fila:
                return False

        return True

    def selec_luz(conjunto):
        x = randint(0, 4)
        y = randint(0, 4)
        pick = str(x) + str(y)
        while pick in conjunto:
            x = randint(0, 4)
            y = randint(0, 4)
            pick = str(x) + str(y)
        conjunto.append(pick)

        return x, y, conjunto

    #Resolución
    print('Tablero inicial: ')
    actual = inicial
    imprimir_tablero(actual)

    start_time = time.time()  # Tiempo inicial
    for i in range(10000000):
        conjunto = []
        actual = [
                    [1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 1, 1, 0, 1],
                    [0, 1, 0, 1, 1]]
        for j in range(25):
            x,y,conjunto = selec_luz(conjunto)
            apagar(x,y,actual)
            if solucion(actual):
                print('------------------------------------------------')
                print('Se encontro solucion para el conjunto de luces: ')
                print(sorted(conjunto))
                print('------------------------------------------------')
                imprimir_tablero(actual)
                end_time = time.time()  # Tiempo final
                execution_time = end_time - start_time
                print()
                print('Greedy - tiempo de ejecución:', execution_time, 'segundos')
                exit()


    print('No se encontró solucion')

tablero = [
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1]
]
lights_out(tablero)


