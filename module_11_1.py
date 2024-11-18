# Домашнее задание по теме "Обзор сторонних библиотек Python"

# Библиотека requests
import requests
r = requests.get('https://api.github.com', auth=('user', 'pass'))
print(r.status_code)  # Вывод в консоль: 200
# Код 200 означает, что страница доступна и нет никаких проблем. Это самый важный статус-код для SEO,
# он указывает на то, что страница доступна для пользователей и поисковых роботов.
print(r.encoding) # В консоль: utf-8
# Код выполняет запрос к API GitHub с использованием аутентификации и выводит кодировку содержимого ответа.
print(r.url) # Вывод в консоль: https://api.github.com/
# Код выводит URL страницы

# Библиотека pillow
from PIL import Image

# Функция rotate - поворачивает картинку на n градусов против часовой стрелки и открывает
# в просмотровой программе по умолчанию
with Image.open('img_1.jpg') as im:
    im.rotate(45).show() # откроет изображение, повернутое на 45 градусов против часовой стрелки

# Функция composite - создает композицию из трёх изображений
im1 = Image.open(r"img_1.jpg").convert('L') # Создание объекта изображения 1 и преобразование его в режим 'L'
# im1.show() откроет изображение
im2 = Image.open(r"img_2.jpg").convert('L') # Создание объекта изображения 2 и преобразование его в режим 'L'
# im2.show() откроет изображение
mask = Image.open(r"img_3.jpg").convert('L') # Создание объекта изображения-маски и преобразование его в режим 'L'
# mask.show() откроет изображение
im3 = Image.composite(im1, im2, mask) # Композиция всех трёх изображений
im3.show() # Отображение полученного составного изображения

# Создание водяного знака
from PIL import ImageFilter # дополнительно импортируем ImageFilter.CONTOUR
logo = "realpython-logo.png" # картинка из которой будем делать водяной знак
with Image.open(logo) as img_logo:
    img_logo.load()
img_logo = Image.open(logo)
# Изменяем изображение на оттенки серого. Уменьшаем размер и преобразуем в контурное изображение
img_logo = img_logo.convert("L")
threshold = 50
img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
img_logo = img_logo.resize((img_logo.width // 2, img_logo.height // 2))
img_logo = img_logo.filter(ImageFilter.CONTOUR)
img_logo.show() # на выходе контур логотипа
# Чтобы использовать это в качестве водяного знака, меняем местами цвета фона и контура
img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
img_logo.show() # на выходе контур логотипа c замененным цветом
forest = "forest.jpg" # картинка, на которую накладываем водяной знак
with Image.open(forest) as img_forest:
    img_forest.load()
img_forest.paste(img_logo, (480, 160), img_logo)
img_forest.show() # на выходе получили картинку с наложенным водяным знаком



