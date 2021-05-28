"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться
после них.
"""

list_1 = []

while True:
    item = input('Пожалуйста введите число: ')
    if not item.isdigit():
        print("Введены некорректные данные. Попробуйте снова")
        continue
    else:
        item = int(item)

    idf = None

    for i, num in enumerate(list_1):
        if item > num:
            idx = i
            break

    if idf is None:
        list_1.append(item)
    else:
        list_1.insert(idf, item)

    print(list_1)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break
