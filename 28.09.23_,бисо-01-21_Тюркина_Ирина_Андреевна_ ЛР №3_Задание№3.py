import math
print("Введите x начальное")
x0 = float(input())
print("Введите x конечное")
xe = float(input())
print("Введите точность")
eps = float(input())
print("Введите шаг")
dx = float(input())
if (x0>xe):
    print("Конец интервала меньше начала")
elif (dx >xe-x0):
    print("Слишком большой шаг")
elif (dx <=0):0
elif (abs(x0) <=1 or abs(xe)<=1):
    print("|x|<1")
else:
    print("Значение x  arcsin(x)")
    pi = 3.141592653
    while (x0<=xe):
        sum=0
        x=x0
        t=1
        n=1
        while (abs(t)>=eps):
            t = 1 / ((2*n+1)*x**(2*n+1))
            sum+=t
            n+=1
        v = sum
        print("%.4f | %.4f | %.4f |" % (x0, v, n))
        x0+=dx

