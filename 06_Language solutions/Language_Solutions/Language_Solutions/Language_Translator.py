from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1000x626+160+50')
root.title('Language Translator')

def show():
    c1 = comb1.get()
    c2 = comb2.get()
    lab1.config(text=c1)
    lab2.config(text=c2)
    root.after(1000, show)

def translate():
    trans = Translator()
    transl = trans.translate(text1.get(1.0, END), src=comb1.get(), dest=comb2.get())

    text2.delete(1.0, END)
    text2.insert(END, transl.text)

def clear():
    text1.delete(1.0, END)
    text2.delete(1.0, END)

def exite():
    root.destroy()

img = PhotoImage(file=r'D:\Language_Solutions\background.png')
lab = Label(root, image=img)
lab.pack(fill=BOTH, expand=YES)

language = list(LANGUAGES.values())

convert_img = PhotoImage(file=r'D:\Language_Solutions\Convert.png')

clear_img = PhotoImage(file=r'D:\Language_Solutions\cl.png')

exit_img = PhotoImage(file=r'D:\Language_Solutions\exts.png')

comb1 = ttk.Combobox(root, values=language)
comb1.place(x=50, y=70)
comb1.set('English')

lab1 = Label(root, text='English', font=('Engravers', '30', 'bold'), bg='white', fg='#5582f9')
lab1.place(x=50, y=10)


lab2 = Label(root, text='Hindi', font=('Engravers', '30', 'bold'), fg='white', bg='#5582f9')
lab2.place(x=720, y=10)

comb2 = ttk.Combobox(root, values=language)
comb2.place(x=720, y=70)
comb2.set('Hindi')

text1 = Text(root, height=10, width=35, bg='#5582f9', fg='white', wrap=WORD)
text1.place(x=20, y=220)

text2 = Text(root, height=10, width=35, bg='white', fg='#5582f9')
text2.place(x=640, y=220)


correct = Button(root, text='correct', command=translate, font=('arial 20'), bd=0, bg='white', image=convert_img, cursor='hand2')
correct.place(x=20, y=550)


clear = Button(root, text='clear', command=clear, font=('Times New Roman', '20'), bd=0, bg='#5582f9', image=clear_img, cursor='hand2')
clear.place(x=390, y=550)


ext = Button(root, text='exit', command=exite, font=('arial 20'), bd=0, bg='#5582f9', image=exit_img, cursor='hand2')
ext.place(x=730, y=550)
show()
root.mainloop()
