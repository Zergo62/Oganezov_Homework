# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(1, 11):      # закомментировали после создания, чтобы не дублировалась
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', i*10, '1000'))

#cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1', (500,))    # закомментировано после выполнения

# cursor.execute('DELETE FROM Users WHERE (id - 1) % 3 = 0')  # закомментировано после выполнения

cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for i in users:
   print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

connection.commit()
connection.close()