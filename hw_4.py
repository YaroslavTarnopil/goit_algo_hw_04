def greet():
    return "How can I help you?"

def add_contact(contacts, name, phone):
    if name in contacts:
        return f"Контакт {name} вже існує."
    contacts[name] = phone
    return f"Контакт {name} успішно додано."

def change_contact(contacts, name, phone):
    if name not in contacts:
        return f"Контакт {name} не знайдено."
    contacts[name] = phone
    return f"Контакт {name} успішно оновлено."

def show_phone(contacts, name):
    return contacts.get(name, f"Контакт {name} не знайдено.")

def show_all_contacts(contacts):
    if not contacts:
        return "Список контактів порожній."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    parts = user_input.strip().lower().split(' ', 1)
    command = parts[0]
    if len(parts) > 1:
        args = parts[1].split()
    else:
        args = []
    return command, args

def main():
    contacts = {}
    print("Консольний бот-асистент. Введіть команду або 'exit'/'close' для завершення.")

    while True:
        user_input = input(">>> ")
        command, args = parse_input(user_input)

        if command == "hello":
            print(greet())
        elif command == "add" and len(args) == 2:
            name, phone = args
            print(add_contact(contacts, name, phone))
        elif command == "change" and len(args) == 2:
            name, phone = args
            print(change_contact(contacts, name, phone))
        elif command == "phone" and len(args) == 1:
            name = args[0]
            print(show_phone(contacts, name))
        elif command == "all":
            print(show_all_contacts(contacts))
        elif command in ("exit", "close"):
            print("Good bye!")
            break
        else:
            print("Невідома команда або неправильна кількість аргументів.")

if __name__ == "__main__":
    main()