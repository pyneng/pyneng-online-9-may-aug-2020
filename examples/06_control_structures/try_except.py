

#while True:
#    a = input('Введите число: ')
#    b = input('Введите число: ')
#
#    if a.isdigit() and b.isdigit() and int(b) != 0:
#        print(int(a) / int(b))
#        break
#    else:
#        print('Поддерживаются только числа')


while True:
    a = input('Введите число: ')
    b = input('Введите число: ')

    try:
        result = int(a) / int(b)
    except ValueError:
        print('Поддерживаются только числа')
    else:
        print(result)
        break
    print('#'*50)
