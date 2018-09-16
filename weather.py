from tkinter import *
from tkinter import messagebox
import requests, bs4, os
def about():
 messagebox.showinfo("О программе", "Погода (sinoptic.com.ru)\nВерсия 2.1\nАртём Лазарев, 2018\nУтилита предназначенная для получении информации о погоде в определёном городе.")
def show_message():
 s=requests.get('https://sinoptik.com.ru/погода-'+message.get())
 b=bs4.BeautifulSoup(s.text, "html.parser")
 try:
  p3=b.select('.temperature .p3')
  pogoda1=p3[0].getText()
 except:
  messagebox.showerror("Ошибка", "Такого города не существует!")
 p4=b.select('.temperature .p4')
 pogoda2=p4[0].getText()

 p5=b.select('.temperature .p5')
 pogoda3=p5[0].getText()

 p6=b.select('.temperature .p6')
 pogoda4=p6[0].getText()
 
 p=b.select('.rSide .description')
 pogoda=p[0].getText()
 messagebox.showinfo("Информация о погоде", "Утром: " + pogoda1 + " " + pogoda2 + "\nДнём: " + pogoda3 + " " + pogoda4 + "\nОписание: " + " " + pogoda)
root = Tk()
root.title("Погода (sinoptic.com.ru)")
root.geometry("300x250")
main_menu = Menu(root)       # формируется меню
root.config(menu=main_menu)  # меню добавляется к окну
file_menu = Menu(main_menu)  # создается подменю
main_menu.add_cascade(label="Справка", menu=file_menu)
# Заполняется меню File
file_menu.add_command(label="About", command=about)
message = StringVar()
message_label = Label(text = "Название города:")
message_label.place(relx=.2,rely=.1,anchor="c")
message_entry = Entry(textvariable = message)
message_entry.place(relx=.6,rely=.1,anchor="c")
message_button = Button(text="Пуск", command=show_message)
message_button.place(relx=.5,rely=.5,anchor="c")
root.mainloop()


