# 1. Написать функцию которая на вход принимает строку и возвращает строку состоящих из слов
# длина которых более или равна N символов
# Пример вызова
# join_str("lorem ipsum A string some text" , 5) => "lorem ipsum string"

def join_str(string, N):
    lst = string.split()
    for word in lst:
        if len(word) >= N:
            print(word)

    return


join_str("lorem ipsum A string some text", 5)


# 2. Написать функцию которая принимает строку . и возвращает сумму всех цыфр из это строки
# Пример вызова
#  count_digit("test123;asjj32jdj") => 11

def count_digit(string):
    import re
    nums = re.findall('[0-9]', string)
    num = 0
    for n in nums:
        num += int(n)

    return print(num)


count_digit("test123;asjj32jdj")


# 3. Написать функцию валидации пароля которая принримает на вход две строки которая ВЕРНЕТ True / False
# Критерии валидности

#    Два пароля совпали
#   Минимум 8 символов
#    Минимум две заглавных буквы
#    Минимум один спец. символ - ! ? : ; % *

#             Пример вызова
#    validate_password('asdasd' , 'ghfdsa') => False
#    validate_password('adminadmin' , 'adminadmin') => False
#    validate_password('Password123' , 'Password123') => False
#    validate_password('Password123P!' , 'Password123P!') => True

def validate_password(password1, password2):
    upper_case = 0
    cout_spec = 0
    for char in password1:
        if 'A' <= char >= 'Z':
            upper_case += 1
        elif char in '- ! ? : ; % *':
            cout_spec += 1
    for char in password2:
        if 'A' <= char >= 'Z':
            upper_case += 1
        elif char in '- ! ? : ; % *':
            cout_spec += 1
    if len(password1) >= 8 and len(password2) >= 8 and upper_case >= 4 \
            and cout_spec >= 2 and password1 == password2:
        return print(True)
    else:
        return print(False)


#             Пример вызова
validate_password('asdasd', 'ghfdsa')
validate_password('adminadmin', 'adminadmin')
validate_password('Password123', 'Password123')
validate_password('Password123P!', 'Password123P!')


# 4. Посчитать сумму всех четных цыфр числа
#   Пример вызова
#            count_even(234) => 6
#            count_even(1) => 0
#            count_even(11) => 0
#            count_even(113) => 0
#            count_even(11268) =>


def count_even(number):
    import re
    num = re.findall('[0-9]', str(number))
    sum = 0
    for char in num:
        n = int(char)
        if n % 2 == 0:
            sum += n

    return print(sum)


count_even(234)


# 5. Написать функцию которая принимает два списка и проверяет если ли одинаковые элементы . Возвращает True если есть
# Пример вызова
#            compare_sequence([1,2,3] , [1]) => True
#            compare_sequence([1,2,3] , [5,6,7,78]) => False
#            compare_sequence([1] , [1]) => True
#            compare_sequence([1 , 4,1,2,3,4,5,78,2] , []) => False


def compare_sequence(list_1, list_2):
    for char in list_1:
        for char2 in list_2:
            if char == char2:
                print(True)

    return


# Пример вызова
compare_sequence([1, 2, 3], [1])
print('*' * 25)
compare_sequence([1, 2, 3], [5, 6, 7, 78])
print('*' * 25)
compare_sequence([1], [1])
print('*' * 25)
compare_sequence([1, 4, 1, 2, 3, 4, 5, 78, 2], [])


# 6. Реализация сортировки пузырьком. Вернуть отсортированый список. При необходимости использовать метод append
# Пример вызова
# bubble_sort([63, 80, 62, 69, 71, 37, 12, 90, 19, 67]) = > [12, 19, 37, 62, 63, 67, 69, 71, 80, 90]

def bubble_sort(some_list):
    list1 = []
    list1.append(some_list)
    len_some_list = len(some_list)
    for i in range(len_some_list - 1):
        for j in range(len_some_list - i - 1):
            if some_list[j] > some_list[j + 1]:
                some_list[j], some_list[j + 1] = some_list[j + 1], some_list[j]

    return print(list1)


bubble_sort([63, 80, 62, 69, 71, 37, 12, 90, 19, 67])

# 7. Возрастает ли список? Написать функцию is_growing. Вернуть True / False
# Пример вызова
#
#            is_growing([1,2,3]) => True
#            is_growing([10,123,500,1000 , 10001]) => True
#            is_growing([560 , 780 , 779 , 1523]) => False
#            is_growing([10, 8 , 7]) => Fals
'''

Наверное не так как нужно, но по-другому я не понял как это сделать...

'''


def is_growing(some_list):
    sort_list = sorted(some_list)
    if sort_list == some_list:
        print(True)
    else:
        print(False)


is_growing([1, 2, 3])
print('-' * 25)
is_growing([10, 123, 500, 1000, 10001])
print('-' * 25)
is_growing([560, 780, 779, 1523])
print('-' * 25)
is_growing([10, 8, 7])


# 8. Функция на вход принимает список и печатает все числа на нечетных инедксах
#  Пример вызова
#            print_odd_index(range(5))
#            >>> 1
#            >>> 3


#            print_odd_index([14,56,23,22,7,8,4,34,45,3])
#            >>> 56
#            >>> 22
#            >>> 8
#            >>> 34
#            >>> 3

def print_odd_index(some_list):
    for k, v in enumerate(some_list):
        if k % 2 == 1:
            print('>>>', v)

    return


print_odd_index(range(5))
print('*' * 25)

print_odd_index([14, 56, 23, 22, 7, 8, 4, 34, 45, 3])

# 9. Дан список целых чисел.
# Заменить отрицательные на -1, положительные - на число 1, ноль оставить без изменений.
# Без создание дополнительного списка. Менять входной список

some_list = [15, -45, 10, -85, 0, 325, 18, -41]
print(some_list)
for i in range(len(some_list)):
    if some_list[i] > 0:
        some_list[i] = 1
    elif some_list[i] < 0:
        some_list[i] = -1

print(some_list)


# 10. Написать функцию перевода из десятичной системы в n-ую систему счисления.
# Где n - основа системы счисления , 2 <= n <= 9
# Пример вызова
#            from_number_to_base(255 , 2) => 11111111
#            from_number_to_base(255 , 5) => 2010
#            from_number_to_base(347 , 7) => 1004
#            from_number_to_base(155 , 3) => 12202

def from_number_to_base(number, n):
    newNum = ''
    while number > 0:
        newNum = str(number % n) + newNum
        number //= n
    print(newNum)

    return


from_number_to_base(255, 2)
print('*' * 25)
from_number_to_base(255, 5)
print('*' * 25)
from_number_to_base(347, 7)
print('*' * 25)
from_number_to_base(155, 3)


# 11. Написать функцию . которая принимает на вход список и возвращает число , которая встречается чаще всего.
# Обратить внимание на метод count()
# Пример вызова
#                most_common([1,1,1,2,3,4,123,123,123,5,2) => 1
#                most_common([1,1,1,2,3,4,123,123 , 123 ,123,5,2) => 123
#                most_common([56 , -8 , 45 , -3 , -8 , 22) => -8

def most_common(some_list):
    some_list_set = set(some_list)
    most_common = None
    qty_most_common = 0
    for item in some_list_set:
        qty = some_list.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    print(most_common)

    return


most_common([1, 1, 1, 2, 3, 4, 123, 123, 123, 5, 2])
print('*' * 25)
most_common([1, 1, 1, 2, 3, 4, 123, 123, 123, 123, 5, 2])
print('*' * 25)
most_common([56, -8, 45, -3, -8])
