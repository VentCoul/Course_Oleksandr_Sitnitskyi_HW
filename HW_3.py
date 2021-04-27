# 1.Написать функцию которая делает следующее "При заданном целом числе n и кол-ве m посчитайте n + nn + nnn."

# Пример вызова
# calc_many_numbers(5 , 2) => 5 + 55 (60)
# calc_many_numbers(7 , 4) => 7 + 77 + 777 + 7777 (8638)

def calc_many_numbers(n, m):
    sum = 0
    for i in range(1, m + 1):
        num = i * str(n)
        num = num.split()
        for j in num:
            sum += int(j)

    print(sum)

    return


calc_many_numbers(5, 2)
print('*' * 25)
calc_many_numbers(7, 4)


# 2.Напишите функцию, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.

# Пример вызова
#    get_ext('text.txt') => 'txt'
#    get_ext('.git') => 'git'
#    get_ext('somefile.txt.log') => 'log'
#    get_ext('script.py') => 'py'
#    get_ext('script.py.') => ValueErorr
#    calc_many_numbers(7 , 4) => 7 + 77 + 777 + 7777 (8638)

def get_ext(name):
    if name[-1] == '.':
        raise ValueError('ERROR!!!!')
    name_parts = name.split('.')
    return print(name_parts[-1])


get_ext('text.txt')
get_ext('.git')
get_ext('somefile.txt.log')
get_ext('script.py')
get_ext('script.py.')

# 3.Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

nums = list(input('Input some nums >>>').split(","))
tuple_nums = tuple(nums)


# 4.Напишите функцию, которая создаёт комбинацию двух списков таким образом: на вход два списка [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]

def list_combinaation(list1, list2):
    combination_list = list(sum(zip(list1, list2), ()))
    print(combination_list, type(combination_list))

    return combination_list


list_combinaation([1, 2, 3], [11, 22, 33])


# 5.Пользователь вводит номер месяца, функция возвращает время года.

def season(number):
    num = int(number)
    if num == 1 or num == 2 or num == 12:
        print('Its Winter')
    elif 3 <= num >= 5:
        print('Its Spring')
    elif 6 <= num >= 8:
        print('Its Summer')
    elif 9 <= num >= 11:
        print('Its Autumn')
    else:
        print('Incorrect input')

    return


season(input('Input number >>>'))

# 6.Задача. Вывести таблицу умножения числа M в диапазоне от числа a до числа b. Числа M, a и b вводит пользователь.

# Например:
# Если M=4, a=2, b=9, то результат будет:

# 4x2=8

# 4x3=12

# 4x4=16

# 4x5=20

# 4x6=24

# 4x7=28

# 4x8=32

# 4x9=36

Number = int(input('Number >>>'))
num1 = int(input('Diapason num 1 >> '))
num2 = int(input('Diapason num 2 >> '))


def multiplication_table(M, a, b):
    for i in range(a, b + 1):
        result = M * i
        print("{} x {} = ".format(M, i), result)

    return


multiplication_table(Number, num1, num2)


# 7.Переписать функцию . которая у вас уже есть password_validate , так чтобы выпадало исключение если пароль невалидный

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
        raise KeyError('Invalid password')


#             Пример вызова
validate_password('asdasd', 'ghfdsa')
validate_password('adminadmin', 'adminadmin')
validate_password('Password123', 'Password123')
validate_password('Password123P!', 'Password123P!')


# 8.Переписать функцию . которая у вас уже есть password_validate , так чтобы выпадало исключение если пароль невалидный

# 9.Написать функцию которая принримает словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

def some_dict(*args):
    result = 1
    for dict1 in args:
        for key in dict1:
            result = result * dict1[key]

    return print(result)


some_dict({'key1': 5, 'key2': 5, 'key3': 5, 'key4': 5})

# 10.Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб. Использовать выражение-генератор

my_dict = {i: i ** 3 for i in range(1, 10 + 1)}
print(my_dict)


# 11.Функция принимает два списка. Необходимо вернуть из функции из них словарь таким образом, чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

def my_dict(list1, list2):
    dict1 = dict(zip(list1, list2))
    print(dict1)
    return dict1


my_dict([1, 5, 9, 4, 6], [2, 8, 6, 4, 8])


# 12.Написать функцию которая на вход принимает текст и возвращает словарь в котором ключами будет слова из строки . а значениями будет кол-во вхождений слова в строку
# Пример вызова
# count_words("some text some") => {"some": 2 , "text": 1}
def some_dict(some_text):
    some_text = some_text.split()
    my_dict = {i: some_text.count(i) for i in some_text}
    print(my_dict)
    return my_dict


some_dict(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
    'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')


# Чуть побольше задача
# Для решение этой задачи нужно будет установить библиотеку requests

# В консоли выполнить команду pip install requests

# Нужно написать функцию которая сделать запрос по адресу http://jsonplaceholder.typicode.com/posts

#        import requests
#        response_list  = requests.get("http://jsonplaceholder.typicode.com/posts").json()


# И нужно сделать пагинацию на список этих постов

# Выводить нужно по 3 элемента и программа должна зависать , и после нажатия на Enter следующие 3 записи. (Используйте функцию input() )

def pagination(response_list):
    import requests
    response_list = requests.get('http://jsonplaceholder.typicode.com/posts').json()
    for i in range(len(response_list)):
        if i % 3 == 0 and i >= 3:
            input()
        print(response_list[i])


pagination(input('pres Enter!'))

# И еще
# Сделать консольный обменник валют.

# Дать пользователю возможность выбора валюты и типа операции (покупка/продажа) и показать ему правильный резульат (сколько он получит грн при продаже валюты , или сколько нужно грн чтобы купить валюту)

# Курс валют брать с https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5


import requests

course = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
currency = input('Currency, (USD, EUR, RUR, BTC) >>>').upper()
summa = float(input('Samma >>>'))
operation = input('Operation,(buy or sale) >>>')
full_page = requests.get(course).json()
for i in full_page:
    dicts = i
    for key in dicts.keys():
        for value in dicts.values():
            if value == currency and key == operation:
                result = float(dicts.get(key[:])) * summa
                print('For  {}'.format(operation), result, 'UAH')
