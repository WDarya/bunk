import math
count=0
print("Введите R: ")
R = float(input())
while (count!=10):
    print("Введите x: ")
    x = float(input())
    print("Введите y: ")
    y = float(input())
    if R!=0:
        if (x>=0)and(y>=0)and(x**2+y**2<=R**2) or (x<=0)and(y<=0)and(y>=-1*R-R):
            print("Вы попали")
        else: print("вы не попали. Попробуйте еще раз")
    else: print("Радиус не может быть нулевым")
