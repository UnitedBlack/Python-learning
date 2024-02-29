# def reverse_string(string):
#     reversed_string = ""
#     for i in string:
#         reversed_string = i + reversed_string
#         print(reversed_string)


# print(reverse_string("Abo"))


# def da(number):
#     numbers = []
#     for i in range(1, number):
#         if i >= 1:
#             if i % 3 == 0:
#                 numbers.append(i)
#             elif i % 5 == 0:
#                 numbers.append(i)
#         else:
#             return 0
#     print(numbers)
#     return sum(numbers)


# print(da(3))


# def disemvowel(string_):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     return "".join([l for l in string_ if l not in vowels])


# print(disemvowel("Abouiaudidfba"))
import math


def find_divisors(number1, number2):
    divisors = [
        divisor for divisor in range(number1, number2 + 1) if number2 % divisor == 0
    ]
    return divisors


def main(m, n):
    divisors = find_divisors(m, n)

    # print(int(summarized_divisors**0.5))


print(main(250, 500))

"""
    squared_divisors = [divisor**2 for divisor in divisors]
    summarized_divisors = sum(squared_divisors)
(285, 81380) should equal [[1, 1], [42, 2500], [246, 84100]]
(283, 80625) should equal [[42, 2500], [246, 84100]]
(559, 312500) should equal [[287, 84100]]

[[1, 1], [285, 81380]] should equal [[1, 1], [42, 2500], [246, 84100]]
[[42, 2500], [283, 80625]] should equal [[42, 2500], [246, 84100]]
[[250, 62500], [559, 312500]] should equal [[287, 84100]]

1, 246, 2, 123, 3, 82, 6, 41 — делители числа 246.
Возводя в квадрат эти делители, получаем: 1, 60516, 4, 15129, 9, 6724, 36, 1681.
Сумма этих квадратов равна 84100 это 290*290.

Задача
Найдите все целые числа между m и n (целые числа m и n с 1 <= m <= n) такие,
что сумма их квадратов делителей сама является квадратом.
Мы вернем массив подмассивов.
Подмассивы будут состоять из двух элементов:
сначала числа, квадраты делителей которого являются квадратами,
а затем суммы квадратов делителей.

Пример:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42,2500], [246, 84100]]
"""
# Компиляторы

# Для Python доступны компиляторы PyPy и Python 3. PyPy соответствует Python 3.7.

# Важно: в большинстве случаев PyPy выполняет программы быстрее,
# поэтому авторы задач рекомендуют его для использования.

# Но вы можете использовать любой из двух компиляторов.
# Иногда Python 3 (не PyPy) выполняет некоторый код эффективнее PyPy (но редко).
# Еще реже у данных компиляторов случается разница в поведении, которая может быть вам критична.

# Никакого штрафа за переотправку решения под другим компилятором нет.

# Ускорения ввода-вывода

# Рекомендуется рассмотреть возможность вывода данных с помощью комбинации:

# сбор всех результирующих данных в один массив
# приведение элементов данного массива к строкам:
# “скрепление” данных строк с помощью функции “join” у выбранного разделителя
# Пример: вывод массива целых чисел “ans” в формате “каждое число на новой строке”:

# # если ans = [1, 3, 5], то map(str, ans) сделает "1", "3", "5"
# ans_str = "\n".join(map(str, ans))
# print(ans_str)
# Работа с кодами символов

# ord(ch) - ord(‘a’) или ord(ch) - ord(‘A’) - номер символа ch в алфавите (зависит от регистра);
# chr(pos + ord(‘a’)) или chr(pos + ord(‘A’)) - символ по номеру pos в алфавите (зависит от регистра);
# Возможности стандартной библиотеки языка

# Очевидно, что это не все возможности, просто элементы из пункта 3.0.3.

# sort / sorted;
# list (динамический массив);
# set / dict - хеш-таблицы;
# модуль bisect;
# модуль collections: deque, defaultdict;
# модуль heapq.


# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


def removeDuplicates(nums: list[int]) -> int:
    for i in nums:
        count_of_duplicates = nums.count(i)
        
    if count_of_duplicates > 1:
        for n in range(count_of_duplicates):
            nums[nums.index(n)] = ""
            print(nums)
    return nums


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

