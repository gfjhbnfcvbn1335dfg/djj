print("""Голенищенко Сергiй Дмитрович
Лабораторна робота №1
Варіант 3 
Обчислення виразу(1/(x^2+1), якщо х більше -3, вираз дорівнює 9, якщо х менше/рівне -3.
 
 
Обчислення за допомогою валідаторів та регулярних виразів.\n""")

import re

while True:
    re_number = re.compile("[+-]?\d+([.][0-9])*")


    def validator(pattern, str):
        text = input(str)
        while bool(pattern.match(text)) is False:
            text = input(str)
        return float(text)


    x = validator(re_number, 'Enter value of x: ')

    if x <= -3:
        print('For value', x, 'result is 9')
    else:
        print('For value', x, 'result is ', 1 / (x ** 2 + 1))
    while True:
        answer = input('Run again? (y/n):\n ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.\n')
    if answer == 'y':
        continue
    else:
        break
