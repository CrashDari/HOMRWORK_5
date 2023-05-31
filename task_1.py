import random
# 0 - пустое поле
# 1 - крестик
# 2 - нолик

# Формируем таблицу игры в крестики нолики
table_X_O = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(random.randint(0,2))
    table_X_O.append(row)

# По сформированной таблице определяем результат
def result(table):
    # Проверяем все строки
    for row in table:
        target_row = row[0]
        for el in row:
            if el != target_row:
                break
        else:
            if target_row != 0:
                return f'Победил {target_row}'

    # Проверяем все столбцы
    for col in range(len(table)):
        target_col = table[0][col]
        for row in table:
            if row[col] != target_col:
                break
        else:
            if target_col != 0:
                return f'Победил {target_col}'

    # Проверяем все диагонали
    target_col_row = table[0][0]
    for col_row in range(len(table)):
        if table[col_row][col_row] != target_col_row:
            break
    else:
        if target_col_row != 0:
            return f'Победил {target_col_row}'

    target_col_row = table[0][len(table) - 1]
    for col_row in range(len(table)):
        if table[col_row][len(table) - 1 - col_row] != target_col_row:
            break
    else:
        if target_col_row != 0:
            return f'Победил {target_col_row}'

    return 'Ничья'

print(table_X_O)
print(result(table_X_O))