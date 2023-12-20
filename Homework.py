import sqlite3 as sl




def add():
    print(" ")
    name = input("Введите имя: ")
    phones = input("Введите телефоны через пробел: ")
    birthday = input("Введите дату рождения: ")
    email = input("Введите email: ")
    cur.execute(f"INSERT INTO users VALUES ('{name}', '{phones}', '{birthday}', '{email}');")
    print("Контакт добавлен")
    print()

        
def show():
    cur.execute("SELECT name FROM users;")
    print(cur.fetchall())

def edit():
    show()
    contact_name = input("Введите имя контакта для изменения: ")
    try:
        cur.execute(f"SELECT * FROM users WHERE name = '{contact_name}';")
        print(f"Контакт для изменения: {cur.fetchall()}")
        new_name = input("Введите новое имя: ")
        if new_name != "":
            cur.execute(f"UPDATE users SET name = '{new_name}' WHERE name = '{contact_name}';")
            contact_name = new_name
        new_phones = input("Введите телефоны через пробел: ")
        if new_phones != "":
            cur.execute(f"UPDATE users SET phones = '{new_phones}' WHERE name = '{contact_name}';")
        new_birthday = input("Введите дату рождения: ")
        if new_birthday != "":
            cur.execute(f"UPDATE users SET birthday = '{new_birthday}' WHERE name = '{contact_name}';")
        new_email = input("Введите email: ")
        if new_email != "":
            cur.execute(f"UPDATE users SET email = '{new_email}' WHERE name = '{contact_name}';")
    except:
        print("Такого контакта нет")
    
def delete():
    show()
    contact = input("Введите имя контакта для удаления: ")
    try:
        choice = input("Введите 'Y' если уверены:  ")
        if choice == "Y":
            cur.execute(f"DELETE FROM users WHERE name = '{contact}';")
            print("Контакт удален")
    except:
        print("Такого контакта нет")


def search():
    searched_name = input("Введите имя для поиска: ")
    cur.execute(f"SELECT * FROM users WHERE name = '{searched_name}';")
    print(cur.fetchall())


conn = sl.connect("phonebook.db")
cur = conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
            name TEXT PRIMARY KEY,
            phones TEXT,
            birthday TEXT,
            email TEXT
            );
            """)


Flag = True
while Flag:
    print("Вам доступны команды: add, show, search, edit, delete. \nДля сохранения изменений и выхода введите exit.")
    command = input("Введите команду: ")
    if command == "add":
        add()
    elif command == "show":
        show()
    elif command == "search":
        search()
    elif command == "delete":
        delete()
    elif command == "edit":
        edit()
    elif command == "exit":
        Flag = False
    else:
        print("Неверная команда")

conn.commit()
conn.close()