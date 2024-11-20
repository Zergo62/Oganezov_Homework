# Домашнее задание по теме "Интроспекция"
import inspect
class ObjectInfo():
    def __init__(self, obj):
        self.obj = obj
        self.introspection_info()

    def introspection_info(self):
        print(f'Имя объекта: {object.__name__}')
        print(f'Объект вызываемый?: {callable(object)}')
        print(f'Тип объекта: {type(self.obj)}')
        print(f'Атрибуты и методы объекта: {dir(self.obj)}')
        print(f'Объект принадлежит модулю: {inspect.getmodule(object)}')

object = ObjectInfo(42)