from types import CoroutineType


def data_types():
    a = 1
    b = 'oak'
    c = 3.14
    d = True
    e = ['какая-то строка', 1234, 3.1415] # список упорядоченный, изменяемый
    f = {'name': 'deleusis', 'location': 'Moscow', 'post code': 103999} # элементы словаря заключают в фигурные скобки, слева от двоеточия — ключ, справа — значение, каждый элемент отделяется запятой
    g = ("Tom", 37, "Google", "software developer") # в отличие от списка кортеж защищен от изменений 
    h = {"apple", "banana", "cherry"} #множество - неупорядоченная коллекция объектов, которая не допускает повторяющихся элементов. Для создания пустого множества нужно вызвать конструктор set()

    print('[%s, %s, %s, %s, %s, %s, %s, %s]'
          % (
              type(a).__name__, type(b).__name__ , #__name__ для того, чтобы выводилось только имя класса
              type(c).__name__, type(d).__name__,
              type(e).__name__, type(f).__name__ ,
              type(g).__name__, type(h).__name__
            )
          )


if __name__ == '__main__':
    data_types()