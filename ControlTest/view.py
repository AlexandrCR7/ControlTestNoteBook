import datetime
import time

def input_number():
    ask = int(input('Выберите действие:\n'
                    '9 - Прекратить запись\n'
                    '1 - Создать новую заметку:\n'
                    '2 - Найти заметку по элементу:\n'
                    '3 - Показать все заметки: \n'
                    '4 - Внести изменения в заметки:\n'
                    '5 - Удалить заметку:\n'
                    '6 - Отсортировать строку:\n'))
    return ask


def input_del_number():
    ask_1 = int(input('Выберите способ изменения заметки:\n'
                      '0. Вернуться в основное меню\n'
                      '1. Изменение по номеру строки.\n'
                      '2. Изменение по элементу.\n'))
    return ask_1


def input_name():
    id = input('Введите id заметки: ')
    name = input('Введите Тему: ')
    tel = input('Введите текст заметки: ')
    local_time = time.localtime()
    final_time = time.strftime('%a, %d %b %Y %H:%M:%S', local_time)
    data_name = "\n" + id + ';' + name + ';' + tel + ';' + final_time
    return data_name


def input_element():
    element = input('Введите элемент для поиска: ')
    return element


def search_id():
    element = int(input('Введите номер строки Заметки, которую хотите поменять: '))
    return element


def del_id():
    element = int(input('Введите номер заметки, которую хотите удалить: '))
    return element
