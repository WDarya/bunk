import math

dx = 0.1
print("Введите x0: ")
x0 = float(input())
print("Введите xe: ")
xe = float(input())
print("Введите R: ")
R = float(input())
print('Заголовок таблицы')
print('|x|\t|f(x)|')
if R!=0 and (x0<xe):
    for i in range(int((xe - x0) / dx)):
        if (x0+i*dx>=-3) and (x0+i+dx<=-1):
            y = -2*(x0+i*dx)-2
        elif (x0+i*dx>-1) and (x0+i*dx<=1):
            y = 0
        elif (x0+i*dx>1) and (x0+i*dx<=5):
            y = math.sqrt(math.fabs(R**2-(x0+i*dx)**2))
        elif (x0+i*dx>5) and (x0+i*dx<=7):
            y = -0.5*(x0+i*dx)+2.5
        else: y = None
        if (y!=None): print (x0+i*dx,"", y)
        else: print ("Функция не определена в этой точке")
else: print("Радиус не может быть 0")


