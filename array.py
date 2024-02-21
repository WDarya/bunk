import random
print("Введите количество элементов массива: ")
n = int(input())
print ("Введите начало интервала разброса")
a = int(input())
print ("Введите конец интервала разброса")
b = int(input())
array =[]
proz =1
sum =0
max =0
number = n -1
count_otr=0
count_pol =0
i=0
while (i<n):
    array.append(round(random.random()* random.randint(a,b),2))
    if i==0:
        max = array[i]
    elif array[i]>max:
        max = array[i]
        number = i
    if array[i] <0:
        proz*=array[i]
        count_otr+=1
    else:count_pol+=1
    i+=1
for j in range (0,number):
    if array[j]>0:
        sum+=array[j]
print ("Полученный массив: ",array)
if count_otr>0:
    print ("Произведение отрицательных элементов массива: ",proz)
else: print("В массиве не было отрицательных элементов")
if count_pol>0:
    print ("Сумма положительных элементов до максимального: ",round(sum,2))
else: print("В массиве не было положительных элементов")
print ("Массив в обратном порядке: ",array[::-1])

def insert(arr):
    n=len(arr)

    for i in range (1,n):
        a = arr[i]
        j =i-1

        while (j>=0 and arr[j]>a):
            arr[j+1] =arr[j]
            j-=1
        arr[j+1] = a
    return arr
print("Сортировка вставкой: ",insert(array))
