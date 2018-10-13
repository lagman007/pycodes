from tkinter import *
from tkinter import messagebox
import os
def show_about():
 messagebox.showinfo("О программе", "Переводчик в римские цифры\nВерсия 1.1\nУтилита предназначенная для перевода чисел в римские цифры.")
def show_message():
  roman = {
	        1:"I",
	        2:"II",
	        3:"III",
	        4:"IV",
	        5:"V",
	        6:"VI",
	        7:"VII",
	        8:"VIII",
	        9:"IX",
	        10:"X"
	       }
  try:
   if int(message.get()) in roman:
    messagebox.showinfo("Результат", roman[int(message.get())])
  except:
   messagebox.showerror("Ошибка", "Введеное значение не являеться числом.")
  if int(message.get()) > 10:
   cur = int(message.get())-10
   try:
    messagebox.showinfo("Результат", roman[10]+roman[cur])
   except:
    messagebox.showerror("Ошибка", "Больше 20 не переводит (в разработке)")
 
root = Tk()
root.title("Roman Translator")
root.geometry("300x250")
main_menu = Menu(root)       # формируется меню
root.config(menu=main_menu)  # меню добавляется к окну
file_menu = Menu(main_menu)  # создается подменю
main_menu.add_cascade(label="Справка", menu=file_menu)
# Заполняется меню File
file_menu.add_separator()
file_menu.add_command(label="О программе", command=show_about)
message = StringVar()
message_label = Label(text = "Число (пока не > 20):")
message_label.place(relx=.2,rely=.1,anchor="c")
message_entry = Entry(textvariable=message)
message_entry.place(relx=.7,rely=.1,anchor="c")
message_button = Button(text="Пуск", command=show_message)
message_button.place(relx=.5,rely=.5,anchor="c")
root.mainloop()
