import math
print("Введите x: ")
x = float(input())
print("Введите R: ")
R = float(input())
if R!=0:
    if (x>=-3) and (x<=-1):
        y = -2*x-2
    elif (x>-1) and (x<=1):
        y = 0
    elif (x>1) and (x<=5):
        y = math.sqrt(R**2-x**2)
    elif (x>5) and (x<=7):
        y = -0.5*x+2.5
    else: y = None
    if (y!=None): print ("Значение функции: ", y)
    else: print ("Функция не определена в этой точке")
else: print("Радиус не может быть 0")