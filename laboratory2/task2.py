print("""Голенищенко Сергiй Дмитрович
Лабораторна робота №2
Варіант 3 
Обчислення кiлькостi парних цифр в заданому числi. 


Обчислення за допомогою валідаторів та регулярних виразів.\n""")


import re


while True:
    re_integer = re.compile("^\d+$")


    def validator(pattern, str):
        text = input(str)
        while bool(pattern.match(text)) is False:
            text = input(str)
        return text


    number = int(validator(re_integer, 'Enter natural number:'))
    amount = 0
    while number > 0:
        if (number % 10) % 2 == 0:
            amount += 1
        number //= 10
    if amount == 0:
        print('In this number there is no even numbers.\n')
    elif amount == 1:
        print('In this number there is one even number.\n')
    else:
        print('In this number there are ', amount, ' even numbers.\n')
    while True:
        answer = input('Run again? (y/n):\n ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.\n')
    if answer == 'y':
        continue
    else:
        break