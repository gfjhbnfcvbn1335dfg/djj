print("""Голенищенко Сергiй Дмитрович
Лабораторна робота №1
Варіант 3 
Визначення, чи iснує трикутник з заданими кутами, та чи буде вiн прямокутним.


Обчислення за допомогою валідаторів та регулярних виразів.\n""")


import re

while True:
    re_number = re.compile("^[+-]?\d+([.][0-9])*$")


    def validator(pattern, str):
        text = input(str)
        while bool(pattern.match(text)) is False:
            text = input(str)
        return text


    def num_between_zero_180_validator(str):
        number = float(validator(re_number, str))
        while number <= 0 or number >= 180:
            number = float(validator(re_number, str))
        return number


    angle1 = num_between_zero_180_validator('Enter first angle(between 0 and 180):\n')
    angle2 = num_between_zero_180_validator('Enter second angle(between 0 and 180):\n')
    if angle1 + angle2 >= 180:
        print('For values', angle1, 'and', angle2, 'triangle does not exist.')
    elif angle1 + angle2 == 90:
        print('For values', angle1, 'and', angle2, 'triangle exists and it is right.')
    else:
        print('For values', angle1, 'and', angle2, 'triangle exists and it is not right.')
    while True:
        answer = input('Run again? (y/n):\n ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.\n')
    if answer == 'y':
        continue
    else:
        break
