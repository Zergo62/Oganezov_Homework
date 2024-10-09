# Домашнее задание по теме "Введение в функциональное программирование"
def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))





# dict = { "Фрукты": 22, "Пустая": 14, "Корица": 4, "Сыр": 21}
# dict["Вишня"] = 10  - получаем новый словарь