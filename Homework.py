import json

def add():
    print(" ")
    name = input("Введите имя: ")
    phones = input("Введите телефоны через пробел: ").split(" ")
    birthday = input("Введите дату рождения: ")
    email = input("Введите email: ")
    contact = {'phones': phones,
                        'birthday': birthday, 'email': email}
    phonebook[name] = contact
    print(contact)
    print("Контакт добавлен")
    print()
    
    
def save():
    with open("contants.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
        
def show():
    if len(phonebook) != 0:
        for name, values in phonebook.items():
            print(name, values)
    else:
        print("Нет ни одного контакта! ")

def edit():
    contact_name = input("Введите имя контакта для изменения: ")
    try:
        print(f"Контакт для изменения: {contact_name}")
        print(phonebook[contact_name])
        new_name = input("Введите новое имя: ")
        if new_name != "":
            phonebook[new_name] = phonebook[contact_name]
            del phonebook[contact_name]
            contact_name = new_name
        new_phones = input("Введите телефоны через пробел: ").split(" ")
        if new_phones != "":
            phonebook[contact_name]['phones'] = new_phones
        new_birthday = input("Введите дату рождения: ")
        if new_birthday != "":
            phonebook[contact_name]['birthday'] = new_birthday
        new_email = input("Введите email: ")
        if new_email != "":
            phonebook[contact_name]['email'] = new_email       
        save()

    except:
        print("Такого контакта нет")
    
def delete():
    contact = input("Введите имя контакта для удаления: ")
    try:
        print(phonebook[contact])
        choice = input("Введите 'Y' если уверены:  ")
        if choice == "Y":
            del phonebook[contact]
            print("Контакт удален")
            save()
    except:
        print("Такого контакта нет")

def load():
    try:
        with open("contants.json", "r", encoding="utf-8") as fh:
            contacts = json.loads(fh.read())
    except:
        print("Нет контактов, добавьте хотя бы один [add]")
        contacts = None
    return contacts

phonebook = load()

while True:
    print("Вам доступны команды: add, save, show, edit, delete")
    command = input("Введите команду: ")
    if command == "add":
        add()
    elif command == "save":
        save()
    elif command == "show":
        show()
    elif command == "delete":
        delete()
    elif command == "edit":
        edit()
    else:
        print("Неверная команда")