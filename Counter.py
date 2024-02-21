from tkinter import*

def read():
    resSent.delete(1.0,END)
    s1 = arr1.get()
    s2 = arr2.get()
    itog = (chess(s1,s2))
    str_itog = ' '.join(itog)
    resSent.insert("1.0",str_itog)
def chess(s1,s2):
    result = []
    s1_1 = s1.strip().split()
    s2_2 = s2.strip().split()
    delta = len(s1_1)-len(s2_2)
    k,k1=0,1
    if delta==0:
        for i in range (0,len(s1_1)):
            result.insert(i+k,s1_1[i])
            k+=1
        for i in range (0,len(s2_2)):
            result.insert(i + k1, s2_2[i])
            k1+=1
    if delta>0:
        for i in range (0,len(s1_1)):
            if (i)>=len(s2_2):
                result.insert(i+len(s2_2),s1_1[i])
            else:
                result.insert(i+k,s1_1[i])
            k+=1
        for i in range (len(s2_2)):
            result.insert(i+k1,s2_2[i])
            k1+=1
    if delta <0:
        for i in range (0,len(s1_1)):
            result.insert(i+k,s1_1[i])
            k+=1
        for i in range (len(s2_2)):
            if (i)>=len(s1_1):
                result.insert(i+len(s1_1),s2_2[i])
            else:
                result.insert(i+k1,s2_2[i])
    return result
root = Tk()
root.geometry("600x300")
root.resizable(False, False)
root.title("Перестановка слов в предложении")
btnf = Button(root, text='Переставить', fg='DeepSkyBlue4')
btnf.bind('<Button-1>',lambda event: read())
root.bind("<Return>", lambda event: read())
btnf.place(x=486, y=255)
lbl1 = Label(root, text='Введите первый массив символов ', justify='left').pack(anchor=NW, padx=10, pady=10)
arr1 = Entry(root)
arr1.pack(ipadx = 200, padx= 10, pady=5, anchor=NW)
lbl2 = Label(root, text='Введите второй массив символов', justify='left').pack(anchor=NW, padx=10, pady=10)
arr2 = Entry(root)
arr2.pack(ipadx = 200, padx= 10, pady=5, anchor=NW)
lbl3 = Label(root, text='Результирующее предложение:', justify='left').place(x=10, y=140)
resSent = Text(root, wrap=WORD, width=56, height=1)
resSent.place(x=10, y=170)
root.mainloop()