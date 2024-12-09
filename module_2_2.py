first = int(input('Уважаемый пользователь, введите число № 1: '))
second = int(input('Уважаемый пользователь, введите число № 2: '))
third = int(input('Уважаемый пользователь, введите число № 3: '))

if first == second and second == third:
    print(3)

elif first == second or first == third or second == third:

    print(2)

elif first != second and first != third and second != third:

    print(0)