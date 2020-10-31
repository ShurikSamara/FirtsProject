def fibonacci():
    a, b = 0, 1
    while a < 1000:
        print(a, end='; ')
        a, b = b, a+b
    print('\n')
    aList = list(range(1, 1))
    aTuple = tuple(range(1, 1))
    print(aList, aList.__sizeof__())
    print(aTuple, aTuple.__sizeof__())


fibonacci()