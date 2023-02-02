print("Календарь")
a = int(input("Введите год: "))

def Date(x):
    d = 0
    for i in range(x+1):
        if i<10:
            d = d + i
        else:
            hh = str(i)
            h = list(hh)
            d = d + int(h[0]) + int(h[1])
    return d



try:
    if(a%4==0):
        print("Год високосный")
        b = Date(31) * 7 + Date(29) + Date(30) * 4
        print("Итог: ", b)
    else:
        print("Год невисокосный")
        b = Date(31) * 7 + Date(28) + Date(30) * 4
        print("Итог: ", b)
except:
    print("Произошла какая-то ошибка(")


