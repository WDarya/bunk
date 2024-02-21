class ArrayOfString:
    def __init__(self, size, length):
        self.array = [''] * size
        self.length = length
    def __setitem__(self, index, value):
        if len(value) != self.length:
            print('Ошибка: неверная длина строки')
        else:
            self.array[index] = value
    def __getitem__(self, index):
        return self.array[index]
    def print_element(self, index):
        print(self.array[index])
    def print_array(self):
        for i in range(len(self.array)):
            print(self.array[i], sep = '')

    def concatenate(self, other):
        result = []
        for i in range(len(self.array)):
            result.append(self.array[i]+other[i])
        for i in range(len(result)):
            print(result[i])
    def merge(self, other):
        result = ArrayOfString(len(self.array) + len(other.array), self.length)
        for i in range(len(self.array)):
            result[i] = self.array[i]
        j = len(self.array)
        for i in range(len(other.array)):
            if other[i] not in self.array:
                result[j] = other[i]
                j += 1
        return result

def main():
    size = int(input('Введите размер массива: '))
    length = int(input('Введите длину строки: '))
    array = ArrayOfString(size, length)
    for i in range(size):
        print('Введите ', i + 1, '-ую строку: ')
        value = input()
        while len(value) != length:
            print('Некорректная длина строки. Введите снова: ')
            value = input()
        array[i] = value
    while True:
        print('Выберите действие:')
        print('1. Выполнение операций поэлементного сцепления двух массивов с образованием нового массива')
        print('2. Слияние двух массивов с исключением повторяющихся элементов')
        print('3. Вывод на экран элемента массива по заданному индексу')
        print('4. Вывод на экран всего массива')
        print('0. Выход')
        choice = input('Ваш выбор: ')
        if choice == '1':
            other = ArrayOfString(size, length)
            for i in range(size):
                value = input(f'Введите {i+1}-ую строку: ')
                while len(value)!=length:
                    print("Некорректная длина строки. Введите снова")
                    value=input()
                other[i] = value
            result = array.concatenate(other)
        elif choice == '2':
            other = ArrayOfString(size, length)
            for i in range(size):
                value = input(f'Введите {i+1} строку: ')
                other[i] = value
                while len(value) != length:
                    print("Некорректная длина строки. Введите снова")
                    value = input()
                other[i] = value
            result = array.merge(other)
            result.print_array()
        elif choice == '3':
            index = int(input('Введите индекс: '))
            if index>=size:
                print("Такого элемента нет.")
            else:
                print(array[index])
        elif choice == '4':
            array.print_array()
        elif choice == '0':
            break
        else:
            print('Неверный выбор')
if __name__ == '__main__':
    main()