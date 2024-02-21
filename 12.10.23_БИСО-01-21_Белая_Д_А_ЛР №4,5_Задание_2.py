import random
def ne_otriz(array,j):
    sum = 0
    i=0
    while(i<j):
        if array[i]>=0:
            sum+=array[i]
        else:
            sum = 0
            break
        i += 1
    return sum

def sum_diag(array):
    n = len(array)
    min_sum = float('inf')
    for i in range(1, n):
        diagonal_sum1 = sum(array[j + i][j] for j in range(n - i))
        diagonal_sum2 = sum(array[j][j + i] for j in range(n - i))
        if diagonal_sum1 < min_sum:
            min_sum = diagonal_sum1
        if diagonal_sum2 < min_sum:
            min_sum = diagonal_sum2
    print("Минимальная сумма элементов диагоналей", min_sum)

print("Введите количество строк и столбцов в матрице")
x,y=map(int,input().split())
print ("Введите начало интервала разброса")
a = int(input())
print ("Введите конец интервала разброса")
b = int(input())
s=0
arr=[]
res =0
if (x>0):
    arr = [[random.randint(a, b) for i in range(x)] for j in range(y)]
    print ("Созданный массив: ",*arr, sep='\n')
i=0
while (i!=y):
    res = ne_otriz(arr[i],y)
    s+=res
    i+=1
print("Сумма элементов без отрицательных: ", s)
sum_diag(arr)






