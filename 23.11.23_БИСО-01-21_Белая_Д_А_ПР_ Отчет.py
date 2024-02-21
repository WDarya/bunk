# class Price (object):
#     def __init__(self,product,shop,charge):
#         self.product = product
#         self.shop = shop
#         self.charge = charge
# def is_digit(string):
#     if string.isdigit():
#         return True
#     else:
#         try:
#             float(string)
#             return True
#         except ValueError:
#             return False
#
# prices = []
# print("Введите количество объектов Price: ")
# n = int(input())
# for i in range (0,n):
#     print("Введите название товара: ")
#     product = input()
#     if len(product)==0:
#         print("Поле не может быть пустым")
#         product = input()
#     print("Введите название магазина: ")
#     shop= input()
#     if len(shop)==0:
#         print("Поле не может быть пустым")
#         shop = input()
#     print("Введите стоимость товара: ")
#     charge = input()
#     if is_digit(charge):
#         charge = float(charge)
#         prices.append(Price(product,shop,charge))
#     else:
#         print("Стоимость товара должна быть в рублях")
#         charge=None
#         prices.append(Price(product, shop,charge))
# prices.sort(key = lambda s: s.shop)
#
# a = 0
# while (a==0):
#     print("Введите 1/2/3 для выбора действия: ")
#     print("1.Вывод на экран информации о товарах, продающихся в магазине")
#     print("2.Запись массива в файл под заданным с клавиатуры именем")
#     print("3.Выход")
#     choice = int(input())
#     if choice ==1:
#         m = 0
#         print("Введите название магазина: ")
#         sh = input()
#         for i in range (0,n):
#             if prices[i].shop ==sh:
#                 print (f"Информация о товарах в магазине {sh}:\n Название товара: {prices[i].product};\n Цена товара: {prices[i].charge}.")
#                 m+=1
#         if m==0:
#             print("Такого магазина нет")
#     elif choice ==2:
#         print("Введите файл для записи:")
#         name = input()
#         print("Вы хотите добавить данные в файл (1) или записать заново (2) ?")
#         if int(input())==1:
#             file = open(name,"a")
#         else:
#             file = open(name,"w")
#         for i in prices:
#             file.write("Название товара: ")
#             file.write(str(i.product))
#             file.write(" Название магазина: ")
#             file.write(str(i.shop))
#             file.write(" Стоимость товара: ")
#             file.write(str(i.charge))
#             file.write("\n")
#         file.close()
#         print("Данные успешно добавлены.")
#     elif choice ==3:
#         a= 3



class Price:
    def __init__(self, name, shop, cost):
        self.name = name
        self.shop = shop
        self.cost = cost

    def to_string(self):
        return f"Название товара: {self.name}, Магазин: {self.shop}, Стоимость: {self.cost} руб."

def is_digit(string):
       if string.isdigit():
             return True
       else:
             try:
                 float(string)
                 return True
             except ValueError:
                 return False

def display_menu():
    print("Меню:")
    print("1. Ввод данных")
    print("2. Сортировка и вывод данных")
    print("3. Удаление данных")
    print("4. Сохранение данных в файл")
    print("5. Чтение из файла")
    print("6. Выход")


def get_choice_input():
    choice = input("Выберите пункт меню: ")
    return int(choice)


def get_price_input():
    name = input("Введите название товара: ")
    shop = input("Введите название магазина: ")
    cost = float(input("Введите стоимость товара: "))
    return Price(name, shop, cost)


def save_to_file(prices, filename):
    print("Вы хотите обновить данные в файле (1) или дополнить их (2) ?")
    if int(input()) == 1:
        with open(filename, "w") as file:
            for price in prices:
                file.write(price.to_string() + "\n")
    else:
        with open(filename, "a") as file:
            for price in prices:
                file.write(price.to_string() + "\n")


def read_from_file(filename):
    prices = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            split_data = line.strip().split(", ")
            name = split_data[0].split(": ")[1]
            shop = split_data[1].split(": ")[1]
            cost = float(split_data[2].split(": ")[1].split(" руб.")[0])
            prices.append(Price(name, shop, cost))
    return prices


def sort_data(prices, sort_type):
    if sort_type == 1:
        return sorted(prices, key=lambda price: price.name)
    elif sort_type == 2:
        return sorted(prices, key=lambda price: price.shop)
    elif sort_type == 3:
        return sorted(prices, key=lambda price: price.cost)
    else:
        return prices


def remove_data(prices, edge_cost):
    return [price for price in prices if price.cost <= edge_cost]


def main():
    prices = []
    while True:
        display_menu()
        choice = get_choice_input()

        if choice == 1:
            price = get_price_input()
            prices.append(price)

        elif choice == 2:
            sort_type = int(
                input("Выберите тип сортировки (1-по названию товара, 2-по названию магазина, 3-по стоимости): "))
            sorted_prices = sort_data(prices, sort_type)
            for price in sorted_prices:
                print(price.to_string())

        elif choice == 3:
            edge_cost = float(input("Введите стоимость товара после которой следует удаление: "))
            prices = remove_data(prices, edge_cost)

        elif choice == 4:
            print("Введите имя файла, в который будут сохраняться значения: ")
            filename = input()
            save_to_file(prices, filename)
            print("Данные сохранены в файл.")

        elif choice == 5:
            print("Введите имя файла, из которого будут считываться значения: ")
            filename = input()
            prices = read_from_file(filename)
            for price in prices:
                print(price.to_string())

        elif choice == 6:
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()










