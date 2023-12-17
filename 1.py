from typing import List, Union

def replace_none(input_list: List[List[Union[int, None]]]) -> List[List[int]]:

    """
        Создает новый список, заменяя значения None на 0.

        input_list: Исходный список с возможными значениями None.

        Новый список, в котором None заменены на 0.
    """

    new_list = []
    """
    
    Создаем пустой список для результата
    
    """

    for sublist in input_list:
        new_sublist = [0 if x is None else x for x in sublist] # Заменяем None на 0 в каждом подсписке
        new_list.append(new_sublist) # Добавляем обновленный подсписок в новый список
    return new_list

test_lst = [  # Исходный список
    [1, 2, 3],
    [4, 5, 6],
    [None, 8, 9],
    [10, 11, 12],
    [13, None, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, None],
]


replace_none(test_lst)  # Вызываем функцию
print(new_list)  # Выводим результат