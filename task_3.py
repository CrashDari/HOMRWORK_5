import copy
results = []

# Каждый результат является строкой из номеров столбцов ферзей,
# так как они все располагатся в разных строках

m = [0 for i in range(8)]

# Функция проверки, чтобы новый ферзь не пересекался по
# вертикали или диагонали ни с одним из уже стоящих

def check(x, y):
    for i in range(x):
        if m[i] == y or abs(i-x) == abs(m[i] - y):
            return False
    return True

def res(i):
    if i == 8:
        result = copy.deepcopy(m)
        results.append(result)
    else:
        for j in range(8):
            if check(i, j):
                m[i] = j
                res(i + 1)

res(0)
print(len(results))


