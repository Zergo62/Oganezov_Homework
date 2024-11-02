# Домашнее задание по теме "Генераторы"
def all_variants(text):
    for i in range(len(text)):
        for r in range(i + 1, len(text) + 1):
            yield text[i:r]

a = all_variants("abc")
for i in a:
    print(i)