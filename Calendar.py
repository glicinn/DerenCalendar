print("Календарь")
a = int(input("Введите год: "))

def Date(x):
    count = 0
    for i in range(x+1):
        if i<10:
            count = count + i
        else:
            SrtringDay = str(i)
            SrtringDaySymb = list(SrtringDay)
            count = count + int(SrtringDaySymb[0]) + int(SrtringDaySymb[1])
    return count



try:
    if(a%400==0 or a%100!=0 and a%4==0):
        print("Год високосный")
        b = Date(31) * 7 + Date(29) + Date(30) * 4
        print("Итог: ", b)
    else:
        print("Год невисокосный")
        b = Date(31) * 7 + Date(28) + Date(30) * 4
        print("Итог: ", b)
except:
    print("Произошла какая-то ошибка(")


