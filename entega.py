import random

def generar_tablero():
    """Genera un tablero de Sudoku incompleto respetando las reglas."""
    tablero = [[0 for _ in range(9)] for _ in range(9)]

    # Llena aleatoriamente algunas celdas para iniciar el Sudoku
    for _ in range(random.randint(12, 20)):  # Entre 12 y 20 números iniciales
        fila, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while tablero[fila][col] != 0 or not es_valido(tablero, fila, col, num):
            fila, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        tablero[fila][col] = num
    return tablero

def es_valido(tablero, fila, col, num):
    """Verifica si num puede colocarse en tablero[fila][col] sin violar las reglas."""
    for x in range(9):
        if tablero[fila][x] == num or tablero[x][col] == num:
            return False
    inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False
    return True

def resolver_sudoku(tablero):
    """Resuelve el tablero de Sudoku utilizando backtracking."""
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:  # Encuentra una celda vacía
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num  # Intenta con un número
                        if resolver_sudoku(tablero):  # Llama recursiva
                            return True
                        tablero[fila][col] = 0  # Retrocede
                return False
    return True

def imprimir_tablero(tablero):
    """Imprime el tablero de Sudoku en formato legible con separaciones claras."""
    for i, fila in enumerate(tablero):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        print(" ".join(
            ("| " if j % 3 == 0 and j != 0 else "") + (str(num) if num != 0 else '.')
            for j, num in enumerate(fila)
        ))

# Generar un tablero aleatorio
sudoku_incompleto = generar_tablero()

print("Tablero de Sudoku Incompleto:")
imprimir_tablero(sudoku_incompleto)

if resolver_sudoku(sudoku_incompleto):
    print("\nTablero de Sudoku Resuelto:")
    imprimir_tablero(sudoku_incompleto)
else:
    print("No se encontró solución para el Sudoku.")

