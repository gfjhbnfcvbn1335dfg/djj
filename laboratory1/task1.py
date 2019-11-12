print("""Голенищенко Сергiй Дмитрович
Лабораторна робота №1
Варіант 3 
Обчислення гiпотенузи, площi та периметру трикутника з заданими катетами.


Обчислення за допомогою валідаторів та регулярних виразів.\n
""")

import re

while True:
    re_number = re.compile("[+-]?\d+([.][0-9])*")


    def validator(pattern, str):
        text = input(str)
        while bool(pattern.match(text)) is False:
            text = input(str)
        return text


    def num_greater_zero_validator(str):
        number = float(validator(re_number, str))
        while number <= 0:
            number = float(validator(re_number, str))
        return number


    cathetus1 = num_greater_zero_validator('Enter length of first cathetus:\n')
    cathetus2 = num_greater_zero_validator('Enter length of second cathetus:\n')
    hypotenuse = (cathetus1 ** 2 + cathetus2 ** 2) ** .5
    perimeter = hypotenuse + cathetus2 + cathetus1
    area = cathetus1 * cathetus2 * .5
    print('For values', cathetus2, 'and', cathetus1, 'hypotenuse of triangle is ', hypotenuse,
          ', perimeter of triangle is ', perimeter, ', area of triangle is ', area, '.')
    while True:
        answer = input('Run again? (y/n):\n ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.\n')
    if answer == 'y':
        continue
    else:
        break
