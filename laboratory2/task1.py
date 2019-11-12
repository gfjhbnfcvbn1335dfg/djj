print("""Голенищенко Сергiй Дмитрович
Лабораторна робота №2
Варіант 3 
Обчислення виразу. 


Обчислення за допомогою валідаторів та регулярних виразів.\n""")


import re

while True:
    re_integer = re.compile("^[-+]{0,1}\d+$")
    re_number = re.compile("^[+-]?\d+([.][0-9])*$")


    def validator(pattern, str):
        text = input(str)
        while bool(pattern.match(text)) is False:
            text = input(str)
        return text


    def num_greater_one_validator(str):
        number = int(validator(re_integer, str))
        while number <= 1:
            number = int(validator(re_number, str))
        return number


    x = float(validator(re_number, 'Enter value of x:'))
    n = num_greater_one_validator('Enter value of n:')
    intsum = x ** 2
    for i in range(n + 1):
        intsum += (i ** 2 - x ** 2)
    print(intsum)
    while True:
        answer = input('Run again? (y/n):\n ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.\n')
    if answer == 'y':
        continue
    else:
        break
