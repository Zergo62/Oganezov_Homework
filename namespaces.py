# Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()      # вызов inner_function внутри test_function не дает результата

# inner_function() # не может быть вызвана вне функции test_function, т.к. существует только внутри

test_function()


