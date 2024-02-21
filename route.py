class Route (object):
    def __init__(self,start,finish,number):
        self.start = start
        self.finish = finish
        self.number = number
routes = []
numbers=[]
print("Введите количество объектов Route: ")
n = int(input())
for i in range (0,n):
    print("Введите номер маршрута: ")
    number = input()
    if i!=0:
        if number in numbers:
            print("Маршруты не должны совпадать")
    numbers.append(number)
    print("Введите название начального пункта: ")
    start = input()
    print("Введите название конечного пункта: ")
    finish = input()
    if start==finish:
        print("Начальная точка маршрута не может совпадать с конечной")
    routes.append(Route(start,finish,number))
routes.sort(key = lambda n: n.number)

a = 0
while (a==0):
    print("Введите 1/2/3 для выбора действия: ")
    print("1.Вывод на экран информации о маршрутах, начинающихся/кончающихся в пункте 'Название пункта'")
    print("2.Запись массива в файл под заданным с клавиатуры именем")
    print("3.Выход")
    choice = int(input())
    if choice ==1:
        m = 0
        print("Введите название пункта: ")
        point = input()
        for i in range (0,n):
            if (routes[i].start ==point or routes[i].finish==point):
                print (f"Информация о маршрутах,содержащих в себе пункт {point}:\n Номер маршрута: {routes[i].number};\n Начальная точка: {routes[i].start};\n Конечная точка: {routes[i].finish}.")
                m+=1
        if m==0:
            print("Таких маршрутов нет")
    elif choice ==2:
        print("Введите файл для записи:")
        name = input()
        file = open(name,"w")
        for i in routes:
            file.write("Название маршрута: ")
            file.write(str(i.number))
            file.write(" Название начальной точки: ")
            file.write(str(i.start))
            file.write(" Название конечной точки: ")
            file.write(str(i.finish))
            file.write("\n")
        file.close()
    elif choice ==3:
        a= 3
