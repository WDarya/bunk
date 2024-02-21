import math
x_l =0
x_r =0
f_r =0
f_l =0
a = 0
b = 2
e = 0.1
u = 0.1
k = 0

while (b-a >e):
    x_l = (a+b)/2 - u
    x_r = (a+b)/2 + u
    print(f"Значение точек xk1: (a+b)/2 - u = {x_l} и xk2: (a+b)/2 + u = {x_r}")
    f_l = x_l**2 - (math.log(x_l))-0.5
    f_r = x_r**2 - (math.log(x_r))-0.5
    print(f"Значение функций в этих точках: f(xk1) = {f_l}, f(xk2) = {f_r}")
    if (f_l<f_r):
        print("fk1<fk2 -> ",sep = " ")
        b = x_r
        print(f"Новая граница b: {b}")
        print(f"Текущие границы: [{a};{b}], e = {e}")
        k+=1

    else:
        print("fk1>fk2 -> ", sep=" ")
        a = x_l
        print(f"новая граница a: {a}")
        print(f"Текущие границы: [{a};{b}], e = {e}")
        k+=1
print(f"Минимум функции найден в точке x*: {min(x_l,x_r)}, наименьшее значение функции fk: {min(f_l,f_r)},количество шагов: k={k}")
