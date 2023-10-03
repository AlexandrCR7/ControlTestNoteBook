from data_base import *
from view import *


def main():
    while True:
        num = input_number()
        if num == 9:
            break
        if num == 1:
            write_name(input_name())
            print("Успешно записано.\n")
            add_number_id()
        if num == 2:
            read_element(input_element())
        if num == 3:
            add_number_id()
        if num == 4:
            def string_change():
                while True:
                    number = input_del_number()
                    if number == 1:
                        add_number_id()
                        change_string(search_id(), input_name())
                        print("Строка изменена.\n")
                        break
                    add_number_id()
                    if number == 2:
                        change_string_22(input_element(), input_name())
                        print('Строка изменена.\n')
                        break
                    if number == 0:
                        break
            string_change()
        if num == 5:
            def num_del():
                while True:
                    one = input_del_number()
                    if one == 1:
                        add_number_id()
                        del_string(del_id())
                        print("Строка удалена.\n")
                        add_number_id()
                    if one == 2:
                        add_number_id()
                        del_string_22(input_element())
                        print('Строка удалена.\n')
                        add_number_id()
                    if one == 0:
                        break
            num_del()
        if num == 6:
            sort_list()
            print("Успешно отсортировано.\n")


main()
