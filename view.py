def greetings():
    print("Добрый день!")
    print()


def menu():
    list_1 = ["1. Показать справочник",
              "2. Добавить контакт",
              "3. Найти контакт",
              "4. Изменить контакт",
              "5. Удалить контакт",
              "0. Выйти из меню "]
    print("Меню: ")
    print(*list_1, sep="\n")
    print()


def get_info():
    info = []
    name_1 = input("Введите фамилию: ")
    info.append(name_1)
    name_2 = input("Введите имя: ")
    info.append(name_2)
    name_3 = input("Введите отчество: ")
    info.append(name_3)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except ValueError:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    return info


def find_info():
    key = input("Поиск: ")
    return key


def choice_some_info():
    key_2 = input("Удалить/Изменить: ")
    return key_2


def change_info():
    key_3 = input("Изменить на : ")
    return key_3


def delete_all_info():
    key = find_info()
    return key


def show_phonebook(date):
    return None
