'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) +
премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''


def sal(time, salary, bonus):
    try:
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('не цифра')


time_input = float(input('Выработка в часах '))
salary_input = int(input('Ставка в у.е. '))
bonus_input = int(input('Премия в у.е. '))

sal(time_input, salary_input, bonus_input)
