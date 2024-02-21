from tkinter import *

american_number_system = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,
    'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18, 'nineteen': 19,
    'twenty': 20,'thirty': 30,'forty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'eighty': 80,'ninety': 90,
    'hundred': 100}
def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(american_number_system[number_word])
    if len(numbers)>=5:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 4:
        if (numbers[0]<numbers[1]) and (numbers[1]==100) and (numbers[1]>numbers[2]) and (numbers[2]>numbers[3]) and (numbers[0]<=9) and (numbers[2]>=20) and (numbers[3]<=9):
            return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
        elif(numbers[0]==100):
            return "Перед числом сотенного формата должно стоять число единичного формата"
        elif (numbers[0]>=20 and numbers[1] == 100 ):
            return "После числа десятичного формата не может стоять число формата сотни"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] == 100):
            return "После числа формата 10-19 не может стоять число формата сотни"
        elif (numbers[1]!=100 and numbers[0]<10 and  numbers[1]>=20):
            return "После числа единичного формата не может стоять число десятичного формата"
        elif (numbers[1] != 100 and numbers[0] < 10 and numbers[1] >=10 and numbers[1] <= 19):
            return "После числа единичного формата не может стоять число формата 10-19"
        elif (numbers[0] < 10 and numbers[1] < 10):
            return "После числа единичного формата не может стоять число единичного формата "
        elif (numbers[0] >= 20 and numbers[1] >= 20 ):
            return "После числа десятичного формата не может стоять число десятичного формата"
        elif (numbers[0] >= 20 and numbers[1] >= 10 and numbers[1] <= 19):
            return "После числа десятичного формата не может стоять число формата 10-19"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 10 and numbers[1] <= 19):
            return "После числа формата 10-19 не может стоять число формата 10-19"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 20 ):
            return "После числа формата 10-19 не может стоять число десятичного формата"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] < 10):
            return "После числа формата 10-19 не может стоять число единичного формата"
        elif (numbers[1] < 10 and numbers[1]!=100 and numbers[2] < 10):
            return "После числа единичного формата не может стоять число единичного формата "
        elif (numbers[1]<10 and numbers[1]!=100 and numbers[2]>=10 and numbers[2]<=19):
            return "После числа единичного формата не может стоять число формата 10-19"
        elif (numbers[1] >= 20  and numbers[1]!=100 and numbers[2] >= 20 ):
            return "После числа десятичного формата не может стоять число десятичного формата"
        elif (numbers[1] >= 20  and numbers[1]!=100 and numbers[2] >= 10 and numbers[2] <= 19):
            return "После числа десятичного формата не может стоять число формата 10-19"
        elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] >= 10 and numbers[2] <= 19):
            return "После числа формата 11-19 не может стоять число формата 10-19"
        elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] >= 20 ):
            return "После числа формата 10-19 не может стоять число десятичного формата"
        elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] < 10):
            return "После числа формата 10-19 не может стоять число единичного формата"
        elif (numbers[2]<10 and numbers[3]>=20 ):
            return "После числа единичного формата не может стоять число десятичного формата"
        elif (numbers[2]<10 and numbers[3]>=10 and numbers[3]<=19):
            return "После числа единичного формата не может стоять число формата 10-19"
        elif (numbers[2]< 10 and numbers[3] <10):
            return "После числа единичного формата не может стоять число единичного формата "
        elif (numbers[2]>=20 and numbers[3]>=20 ):
            return "После числа десятичного формата не может стоять число десятичного формата"
        elif (numbers[2]>=20 and numbers[3]>=10 and numbers[3]<=19):
            return "После числа десятичного формата не может стоять число формата 10-19"
        elif (numbers[2]>=10 and numbers[2]<=19 and numbers[3]>=10 and numbers[3]<=19):
            return "После числа формата 10-19 не может стоять число формата 10-19"
        elif (numbers[2]>=10 and numbers[2]<=19 and numbers[3]>=20  ):
            return "После числа формата 10-19 не может стоять число десятичного формата"
        elif (numbers[2]>=10 and numbers[2]<=19 and numbers[3]<10):
            return "После числа формата 10-19 не может стоять число единичного формата"
    elif len(numbers) == 3:
        if (numbers[0]<numbers[1]) and (numbers[1]==100) and (numbers[1]>numbers[2]) and (numbers[0]<=9):
            return numbers[0] * numbers[1] + numbers[2]
        elif (numbers[0] == 100):
            return "Перед числом сотенного формата должно стоять число единичного формата"
        elif ( numbers[0]>=20 and numbers[1] == 100 ):
            return "После числа десятичного формата не может стоять число формата сотни"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] == 100):
            return "После числа формата 10-19 не может стоять число формата сотни"
        elif (numbers[1]!=100 and numbers[0]<10 and  numbers[1]>=20):
            return "После числа единичного формата не может стоять число десятичного формата"
        elif (numbers[1] != 100 and numbers[0] < 10 and numbers[1] >=10 and numbers[1] <= 19):
            return "После числа единичного формата не может стоять число формата 10-19"
        elif (numbers[0] < 10 and numbers[1] < 10):
            return "После числа единичного формата не может стоять число единичного формата "
        elif ( numbers[0]<10 and  numbers[1]>=20):
            return "После числа единичного формата не может стоять число десятичного формата"
        elif (numbers[0] >= 20 and numbers[1] >= 20 ):
            return "После числа десятичного формата не может стоять число десятичного формата"
        elif (numbers[0] >= 20 and numbers[1] >= 10 and numbers[1] <= 19):
            return "После числа десятичного формата не может стоять число формата 10-19"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 10 and numbers[1] <= 19):
            return "После числа формата 10-19 не может стоять число формата 10-19"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 20 ):
            return "После числа формата 10-19 не может стоять число десятичного формата"
        elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] < 10):
            return "После числа формата 10-19 не может стоять число единичного формата"
        elif (numbers[1] < 10 and numbers[1]!=100 and numbers[2] < 10):
            return "После числа единичного формата не может стоять число единичного формата "
        elif (numbers[1]<10 and numbers[1]!=100 and numbers[2]>=10 and numbers[2]<=19):
            return "После числа единичного формата не может стоять число формата 10-19"
        elif (numbers[1] >= 20  and numbers[1]!=100 and numbers[2] >= 20 ):
            return "После числа десятичного формата не может стоять число десятичного формата"
        elif (numbers[1] >= 20  and numbers[1]!=100 and numbers[2] >= 10 and numbers[2] <= 19):
            return "После числа десятичного формата не может стоять число формата 10-19"
        elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] >= 10 and numbers[2] <= 19):
            return "После числа формата 10-19 не может стоять число формата 10-19"
        elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] >= 20 ):
            return "После числа формата 10-19 не может стоять число десятичного формата"
        elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] < 10):
            return "После числа формата 10-19 не может стоять число единичного формата"
    elif len(numbers) == 2:
        if 100 in numbers:
            if (numbers[0]<numbers[1] and numbers[0]<10) :
                return numbers[0] * numbers[1]
            elif (numbers[0] == 100):
                return "Перед числом сотенного формата должно стоять число единичного формата"
            elif ( numbers[0] >= 20 and numbers[1] == 100):
                return "После числа десятичного формата не может стоять число формата сотни"
            elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] == 100):
                return "После числа формата 10-19 не может стоять число формата сотни"
            elif (numbers[1] != 100 and numbers[0] < 10 and numbers[1] >= 20):
                return "После числа единичного формата не может стоять число десятичного формата"
            elif (numbers[1] != 100 and numbers[0] < 10 and numbers[1] >= 10 and numbers[1] <= 19):
                return "После числа единичного формата не может стоять число формата 10-19"
        else:
            if numbers[0]>numbers[1] and numbers[0]>=20 and numbers[1]<10:
                return numbers[0] + numbers[1]
            elif (numbers[0] < 10 and numbers[1] < 10):
                return "После числа единичного формата не может стоять число единичного формата "
            elif (numbers[0] < 10 and  numbers[1] >= 20):
                return "После числа единичного формата не может стоять число десятичного формата"
            elif (numbers[0] < 10 and (numbers[1] >=10 and numbers[1] <=19)):
                return "После числа единичного формата не может стоять число формата 10-19"
            elif (numbers[0] >= 20 and numbers[1] >= 20 ):
                return "После числа десятичного формата не может стоять число десятичного формата"
            elif (numbers[0] >= 20 and numbers[1] >= 10 and numbers[1] <= 19):
                return "После числа десятичного формата не может стоять число формата 10-19"
            elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 10 and numbers[1] <= 19):
                return "После числа формата 10-19 не может стоять число формата 10-19"
            elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 20 ):
                return "После числа формата 10-19 не может стоять число десятичного формата"
            elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] < 10):
                return "После числа формата 10-19 не может стоять число единичного формата"
    else:
        return "Необходимо ввести трехзначное число"
def word_to_num(number_sentence):
    if type(number_sentence) is not str:
        print("Неккоректный ввод. Введите строку\')")
    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower()
    if(number_sentence.isdigit()):
        print("Введите число прописью.")
    split_words = number_sentence.strip().split()
    clean_numbers = []
    for word in split_words:
        if word in american_number_system:
            clean_numbers.append(word)
        else:
            return "Ошибка в слове  "+word
    if len(clean_numbers) == 0:
        print("Вы не ввели строку. Попробуйте еще раз")
    total_sum = 0
    if len(clean_numbers) > 0:
        if len(clean_numbers) == 1:
                total_sum += american_number_system[clean_numbers[0]]
        else:
            hundreds = number_formation(clean_numbers)
            if type(hundreds)==int:
                total_sum += hundreds
            else: return hundreds
    return total_sum

def translate():
    number2.delete(1.0,END)
    entry_s =number1.get()
    convert = str(word_to_num(entry_s))
    if len(convert)<=3:
        lbl.configure(text=" ")
        number2.insert("1.0",convert)
    else:
        lbl.configure(text = " ")
        lbl.configure(text='             Возникла ошибка типа:\n'+ convert)
root = Tk()
root.geometry("650x250")
root.resizable(False, False)
lblerr = Label(root, text='')
root.title("Перевод трёхзначного числа прописью в цифровой вариант")
root.geometry("650x250+620+400")
lbl1 = Label(root, text='Введите число прописью:', justify='left').pack(anchor=NW, padx=10, pady=10)
number1 = Entry(root)
number1.pack(ipadx = 200, padx= 10, anchor=NW)
lbl2 = Label(root, text='Введенное число, представленное в цифровом виде:', justify='left').pack(anchor=NW, padx=10, pady=10)
number2 = Text(root, wrap=WORD, width=10, height=1)
number2.pack(padx=10, pady=5, anchor=NW)
root.bind("<Return>", lambda event: translate())
lbl = Label(root)
lbl.place(x=10,y=130)
btn = Button(root, text='Преобразовать', fg='DeepSkyBlue4')
btn.bind('<Button-1>',lambda event:translate())
btn.place(x=510, y=200)
root.mainloop()

#if (numbers[0]<numbers[1]) and (numbers[1]==100) and (numbers[1]>numbers[2]) and (numbers[2]>numbers[3]) and (numbers[0]<=9) and (numbers[2]>=20) and (numbers[3]<=9):
#elif(numbers[0]==100):
        #     return "Перед числом сотенного формата должно стоять число единичного формата"
        # elif ((numbers[0]==10 or numbers[0]>=20) and numbers[1] == 100 ):
        #     return "После числа десятичного формата не может стоять число формата сотни"
        # elif (numbers[0] > 10 and numbers[0] <= 19 and numbers[1] == 100):
        #     return "После числа формата 10-19 не может стоять число формата сотни"
        # elif (numbers[1]!=100 and numbers[0]<10 and  numbers[1]>=20):
        #     return "После числа единичного формата не может стоять число десятичного формата"
        # elif (numbers[1] != 100 and numbers[0] < 10 and numbers[1] >=10 and numbers[1] <= 19):
        #     return "После числа единичного формата не может стоять число формата 10-19"
        # elif (numbers[0] < 10 and numbers[1] < 10):
        #     return "После числа единичного формата не может стоять число единичного формата "
        # elif (numbers[0] >= 20 and numbers[1] >= 20 ):
        #     return "После числа десятичного формата не может стоять число десятичного формата"
        # elif (numbers[0] >= 20 and numbers[1] >= 10 and numbers[1] <= 19):
        #     return "После числа десятичного формата не может стоять число формата 10-19"
        # elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 10 and numbers[1] <= 19):
        #     return "После числа формата 11-19 не может стоять число формата 10-19"
        # elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] >= 20 ):
        #     return "После числа формата 10-19 не может стоять число десятичного формата"
        # elif (numbers[0] >= 10 and numbers[0] <= 19 and numbers[1] < 10):
        #     return "После числа формата 10-19 не может стоять число единичного формата"
        # elif (numbers[1] < 10 and numbers[1]!=100 and numbers[2] < 10):
        #     return "После числа единичного формата не может стоять число единичного формата "
        # elif (numbers[1]<10 and numbers[1]!=100 and numbers[2]>=10 and numbers[2]<=19):
        #     return "После числа единичного формата не может стоять число формата 10-19"
        # elif (numbers[1] >= 20  and numbers[1]!=100 and numbers[2] >= 20 ):
        #     return "После числа десятичного формата не может стоять число десятичного формата"
        # elif (numbers[1] >= 20  and numbers[1]!=100 and numbers[2] >= 10 and numbers[2] <= 19):
        #     return "После числа десятичного формата не может стоять число формата 10-19"
        # elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] >= 10 and numbers[2] <= 19):
        #     return "После числа формата 11-19 не может стоять число формата 10-19"
        # elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] >= 20 ):
        #     return "После числа формата 10-19 не может стоять число десятичного формата"
        # elif (numbers[1] >= 10 and numbers[1] <= 19 and numbers[2] < 10):
        #     return "После числа формата 10-19 не может стоять число единичного формата"
        # elif (numbers[2]<10 and numbers[3]>=20 ):
        #     return "После числа единичного формата не может стоять число десятичного формата"
        # elif (numbers[2]<10 and numbers[3]>=10 and numbers[3]<=19):
        #     return "После числа единичного формата не может стоять число формата 10-19"
        # elif (numbers[2]< 10 and numbers[3] <10):
        #     return "После числа единичного формата не может стоять число единичного формата "
        # elif (numbers[2]>=20 and numbers[3]>=20 ):
        #     return "После числа десятичного формата не может стоять число десятичного формата"
        # elif (numbers[2]>=20 and numbers[3]>=10 and numbers[3]<=19):
        #     return "После числа десятичного формата не может стоять число формата 10-19"
        # elif (numbers[2]>=10 and numbers[2]<=19 and numbers[3]>=10 and numbers[3]<=19):
        #     return "После числа формата 10-19 не может стоять число формата 10-19"
        # elif (numbers[2]>=10 and numbers[2]<=19 and numbers[3]>=20  ):
        #     return "После числа формата 10-19 не может стоять число десятичного формата"
        # elif (numbers[2]>=10 and numbers[2]<=19 and numbers[3]<10):
        #     return "После числа формата 10-19 не может стоять число единичного формата"
        # if (numbers[3]<10 and numbers[4]>=20 ):
        #     return "После числа единичного формата не может стоять число десятичного формата"
        # elif (numbers[3]<10 and numbers[4]>=10 and numbers[4]<=19):
        #     return "После числа единичного формата не может стоять число формата 10-19"
        # elif (numbers[3]< 10 and numbers[4] <10):
        #     return "После числа единичного формата не может стоять число единичного формата "
        # elif (numbers[3]>=20 and numbers[4]>=20 ):
        #     return "После числа десятичного формата не может стоять число десятичного формата"
        # elif (numbers[3]>=20 and numbers[4]>=10 and numbers[4]<=19):
        #     return "После числа десятичного формата не может стоять число формата 10-19"
        # elif (numbers[3]>=10 and numbers[3]<=19 and numbers[4]>=10 and numbers[4]<=19):
        #     return "После числа формата 10-19 не может стоять число формата 10-19"
        # elif (numbers[3]>=10 and numbers[3]<=19 and numbers[4]>=20  ):
        #     return "После числа формата 10-19 не может стоять число десятичного формата"
        # elif (numbers[3]>=10 and numbers[3]<=19 and numbers[4]<10):
        #     return "После числа формата 10-19 не может стоять число единичного формата"
