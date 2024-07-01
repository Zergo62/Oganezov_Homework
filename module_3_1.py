# Домашняя работа по уроку "Пространство имён"
calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

print(string_info('Корова'))
print(string_info('Овца'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)