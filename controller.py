import view
import model


def run():
    view.greetings()
    while True:
        view.menu()
        answer = input("Выберите опцию меню: ")
        if answer == "1":
            date = model.read_phonebook()
            view.show_phonebook(date)

        elif answer == "2":
            model.add_contact()

        elif answer == "3":
            model.find()

        elif answer == "4":
            model.change()

        elif answer == "5":
            model.delete_all()

        elif answer == "0":
            break
