from view import get_info as gi
from view import find_info as fi
from view import change_info as ci
from view import delete_all_info as dai
from view import choice_some_info as csi


def read_phonebook():
    with open("Phonebook.txt", "r", encoding="utf-8") as file:
        print(*file)


def add_contact():
    info = gi()
    with open("Phonebook.txt", "a", encoding="utf-8") as file:
        # file.write((input("Введите данные контакта: \n")) + "\n")
        # file.write(f"Фамилия: {info[0]}\n"
        #            f"Имя: {info[1]}\n"
        #            f"Отчество: {info[2]}\n"
        #            f"Номер: {info[3]}\n\n")
        file.write(f"Фамилия: {info[0]}"" "
                   f"Имя: {info[1]}"" "
                   f"Отчество: {info[2]}"" "
                   f"Номер: {info[3]}\n")


def find():
    key = fi()
    with open("Phonebook.txt", "r", encoding="utf-8") as file:
        for line in file:
            if key in line:
                print(line)


def change():
    key_2 = csi()
    key_3 = ci()
    with open("Phonebook.txt", "rt", encoding="utf-8") as file:
        data = file.read()
        data = data.replace(key_2, key_3)
    with open("Phonebook.txt", "wt", encoding="utf-8") as file:
        file.write(data)
        print("Успешно")


# def delete():
#     key_3 = di()
#     with open("Phonebook.txt", "rt", encoding="utf-8") as file:
#         data = file.read()
#         data = data.replace(key_3, "_____")
#     with open("Phonebook.txt", "wt", encoding="utf-8") as file:
#         file.write(data)
#         print("Информация удалена")


def delete_all():
    key = dai()
    with open("Phonebook.txt", "r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if key not in line:
                file.write(line)
        file.truncate()
        print("\nУдалено\n")
