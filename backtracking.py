import time
def lights_out(tablero):
    inicial = tablero
    solucion_encontrada = False

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

    def backtrack(tablero, x, y,movs):
        nonlocal solucion_encontrada

        if x == 5:
            if all(valor == 0 for fila in tablero for valor in fila):
                solucion_encontrada = True
                print('- Solución encontrada para: ')
                print(movs)
                movs=[]
            return

        if y == 5:
            backtrack(tablero, x + 1, 0,movs)
            return

        # No apagar la luz
        backtrack(tablero, x, y + 1,movs)

        # Apagar la luz y las luces adyacentes
        apagar(x, y, tablero)
        movs.append(str(x)+','+str(y))
        backtrack(tablero, x, y + 1,movs)
        apagar(x, y, tablero)  # Restaurar el tablero al estado anterior
        movs.remove(str(x) + ',' + str(y))

    # Resolución
    print('Tablero inicial: ')
    imprimir_tablero(inicial)
    print('-----------------------------------')
    print('Movimientos que ganan este tablero: ')
    print('-----------------------------------')
    movs=[]

    start_time = time.time()  # Tiempo inicial
    backtrack(inicial, 0, 0,movs)
    end_time = time.time()  # Tiempo final
    execution_time = end_time - start_time
    print()
    print('Backtracking - tiempo de ejecución:', execution_time, 'segundos')

    if not solucion_encontrada:
        print('No se encontró solución')


tablero = [
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1]
]

lights_out(tablero)