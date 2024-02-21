import math

print("Введите x: ")
x = float(input())
print("Введите y: ")
y = float(input())
print("Введите R: ")
R = float(input())
if R!=0:
    if ((x>=-2*R) and(x<=0) and (y>=-x-2)) or ((x>=R) and (x<=2*R) and (y<=2*R) and(y<=math.sqrt(R**2-x**2))):
        print("Вы попали")
    else: print("Попробуйте еще раз")
else: print("Радиус не может быть нулевым")