from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import json
import os

def show_about():
 messagebox.showinfo("О программе", "Переводчик в СИ\nВерсия 1.1\nАртём Лазарев, 2018\nУтилита предназначенная для перевода стороних единиц в единицы системы СИ.")
 
def translate():    
 with open("si_config.json") as data_file:
  data = json.load(data_file)
 try:
  unit_name = data[amount.get()]['default']
  unit = data[amount.get()][user_unit.get()]
 except KeyError:
  messagebox.showerror("Ошибка", "Указаное значение не совпадает с ключом в файле.")
 result = int(num.get()) * unit
 messagebox.showinfo("Результат", str(result)+" "+unit_name)
def save_options():
 file = open("options.txt")
 file.write(patch.get())

root = Tk()
root.title("SI Translator")
root.geometry("300x250")
main_menu = Menu(root)       # формируется меню
root.config(menu=main_menu)  # меню добавляется к окну
file_menu = Menu(main_menu)  # создается подменю
main_menu.add_cascade(label="Справка", menu=file_menu)
# Заполняется меню File

file_menu.add_separator()  # черта для отделения пунктов меню
file_menu.add_command(label="О программе", command=show_about)
options_menu = Menu(main_menu)

amount_var = StringVar()
user_unit_var = StringVar()
num_var = StringVar()

amount_text = Label(text = "Величина:")
amount_text.place(relx=.2,rely=.1,anchor="c")

user_unit_text = Label(text = "Ед. измерения:")
user_unit_text.place(relx=.2,rely=.3,anchor="c")

num_text = Label(text = "Число:")
num_text.place(relx=.2,rely=.5,anchor="c")

amount = Entry(textvariable = amount_var)
amount.place(relx=.7,rely=.1,anchor="c")

user_unit = Entry(textvariable = user_unit_var)
user_unit.place(relx=.7,rely=.3,anchor="c")

num = Entry(textvariable = num_var)
num.place(relx=.7,rely=.5,anchor="c")

translate = Button(text = 'Перевести', command = translate)
translate.place(relx=.5,rely=.8,anchor="c")
root.mainloop()
