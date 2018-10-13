import statistics
from tkinter import *
from tkinter import messagebox
import os
def show_about():
 messagebox.showinfo("О программе", "Вычислитель среднего арифметического\nВерсия 1.1\nУтилита предназначенная для вычисления статических характеристик чисел, таких как: Среднее арифметическое, Размах и Медиана")
def show_message():
 user_input = message.get()
 user_list = user_input.split(",")
 try:
  i_ui = [int(i) for i in user_list]
 except:
  messagebox.showerror("Ошибка","Введеные значения не являються числами.")
 res = sum(i_ui)
 result = res/len(user_list)
 amplitude = max(i_ui)-min(i_ui)
 m = statistics.median(i_ui)
 messagebox.showinfo("Результат", "Cр. ар.: "+str(result)+"\n"+"Размах: " + str(amplitude)+"\n"+"Медиана: " + str(m))
 
root = Tk()
root.title("Mean")
root.geometry("300x250")
main_menu = Menu(root)       # формируется меню
root.config(menu=main_menu)  # меню добавляется к окну
file_menu = Menu(main_menu)  # создается подменю
main_menu.add_cascade(label="Справка", menu=file_menu)
# Заполняется меню File
file_menu.add_command(label="О программе", command=show_about)
message = StringVar()
message_label = Label(text = "Числа (через ','):")
message_label.place(relx=.2,rely=.1,anchor="c")
message_entry = Entry(textvariable=message)
message_entry.place(relx=.7,rely=.1,anchor="c")
message_button = Button(text="Пуск", command=show_message)
message_button.place(relx=.5,rely=.5,anchor="c")
root.mainloop()


  
    
