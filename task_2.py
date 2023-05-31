# Создадим пример матрицы, удовлетворяющей условию задачи
M = 5
N = 8
val = 0
matrix_M_N = []
for i in range(M):
    list_M = []
    for j in range(N):
        list_M.append(val)
        val += 2
    matrix_M_N.append(list_M)
print(matrix_M_N)

# Функция, выполняющая поиск элемента из матрицы
def search_elem(matrix, val_elem):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = n - 1
    while i < m and j >= 0:
        if matrix[i][j] == val_elem:
            return (i, j)
        if matrix[i][j] > val_elem:
            j -= 1
        else:
            i += 1

    return 'Такого элемента нет'

print(search_elem(matrix_M_N, 52))