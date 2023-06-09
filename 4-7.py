#4
def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
print('количество перешагиваний для 20 ступенек',count_ways(20))
print('количество перешагиваний для4 ступенек',count_ways(4))
print('количество перешагиваний для 5 ступенек',count_ways(5))


#5
"""
В этом коде мы определяем класс ThreeStacks, который содержит три стека.
Конструктор класса принимает емкость массива, который содержит три стека.
Мы используем простой одномерный массив для хранения элементов всех
трех стеков.

Метод push используется для добавления элемента в соответствующий стек,
который задается параметром stack_num.
Метод проверяет, что соответствующий стек не переполнен, и, если это не так,
увеличивает соответствующий индекс и помещает значение в массив.

Метод pop используется для удаления элемента из соответствующего стека.
Метод проверяет, что стек не пуст, и, если это не так,
уменьшает соответствующий индекс и возвращает значение элемента.

В данном примере мы использовали подход "фиксированной емкости",
где каждый стек имеет фиксированную емкость в массиве.
Если требуется реализовать стеки переменной емкости,
то можно использовать аналогичный подход,
где каждый стек начинается с начала массива и
расширяется вправо при добавлении элементов.
"""

#6
def min_missing_number(arr):
    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)
    count_arr = [0] * (max_val - min_val + 1)
    for i in range(n):
        count_arr[arr[i] - min_val] += 1
    for i in range(max_val - min_val + 1):
        if count_arr[i] == 0:
            return min_val + i
    return None  

arr = [3, 4, -1, 1, 2, 6, 8]
print('массив: ', arr)
print('ответ',min_missing_number(arr))  # Output: 5
print('массив: ', arr)
arr = [1, 2, 0, 4]
print('ответ',min_missing_number(arr))  # Output: 3
print('массив: ', arr)
arr = [-2, 2, 2, 2, 3,6]
print('ответ',min_missing_number(arr))  # Output: 3

"""
Найдем минимальное значение и максимальное значение в массиве.
Создадим вспомогательный массив C размера (max - min + 1), заполненный нулями.

Пройдем по массиву и увеличим соответствующее
значение в массиве C на единицу за каждое появление числа в массиве.

Пройдем по массиву C и найдем первый элемент,
который равен 0.
Его индекс будет наименьшим недостающим числом в исходном массиве.
"""\
#7

def exp_filter(x, alpha):
    if len(x) == 1:
        return x[0]
    else:
        return alpha * x[-1] + (1 - alpha) * exp_filter(x[:-1], alpha)
x = [1, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
alpha = 0.5

filtered_x = [exp_filter(x[:i+1], alpha) for i in range(len(x))]
print('параметр фильтрации:  ', alpha, 'отсортированный список', filtered_x)

"""
Здесь x - это входной массив значений, а alpha - параметр фильтра,
который определяет вклад текущего значения и
результатов предыдущих вызовов функции.
Lенуться до O(1) в данном случае невозможно, т.к.
необходимо хранить определенное количество предыдущих значений
(в примере выше - N-1).
"""
