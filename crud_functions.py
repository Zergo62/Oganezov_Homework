import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

connection.commit()
connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()
    connection.commit()
    connection.close()



# cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                (1, 'Product1', 'Для поднятия тонуса', 100))
# cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                (2, 'Product2', 'Для хорошего настроения', 200))
# cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                (3, 'Product3', 'Укрепляющий комплекс', 300))
# cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)',
#                (4, 'Product4', 'От всех болезней', 400))