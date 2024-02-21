import math
print("Введите значение x начальное:")
x0 = float(input())
print("Введите значение x конечное:")
xe = float(input())
print("Введите шаг:")
dx = float(input())
y = float
if (x0<-3) or (xe>5):
    print("Значение вне диапазона")
else:
    if x0 >xe:
        print("Конец интервала меньше начала")
    elif (dx>xe - x0):
        print("слишком большой шаг")
    elif (dx <= 0):
        print("Некорректное значение")
    else:
        print("Таблица значений:")
        print("x            y")
        for i in range(int((xe-x0)/dx)+1):
            if (x0+dx*i>=-3) and (x0+dx*i<=-2):
                y = -1*(x0+dx*i)-2
                print(x0+dx*i,"         ",y)
            elif (x0+dx*i>-2) and (x0+dx*i<=-1):
                y  = math.sqrt(1-((x0+dx*i)+1)**2)
                print(x0+dx*i,"         ",y)
            elif (x0+dx*i>-1) and (x0+dx*i<=1):
                y = 1
                print(x0+dx*i,"         ",y)
            elif (x0+dx*i>1) and (x0+dx*i<=2):
                y = -2*(x0+dx*i)+3
                print(x0+dx*i,"         ",y)
            elif (x0+dx*i>2) and (x0+dx*i<=5):
                y = -1
                print(x0 + dx * i, "              ", y)
