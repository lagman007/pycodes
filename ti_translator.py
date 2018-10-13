from tkinter import *
from tkinter import messagebox
def about():
 messagebox.showinfo("О программе", "Переводчик в римские цифры\nВерсия 2.1\nУтилита предназначенная для перевода чисел в римские цифры.")
def show_message():
 time_list = list(time.get())
 tl_count = len(time_list)
 sec = 5 - tl_count
 clock_list = time_list[:2-sec]
 clock = ''.join(clock_list)
 minutes_list = time_list[3-sec:5-sec]
 minutes = ''.join(minutes_list)
 if int(clock) > 12 and int(clock) <= 24:
  result = int(clock)-12
  messagebox.showinfo("Результат", str(result)+":"+minutes+" PM")
 if int(clock) < 12:
  messagebox.showinfo("Результат", time.get()+" AM")
root = Tk()
root.title("Time Translator")
root.geometry("300x250")
main_menu = Menu(root)       # формируется меню
root.config(menu=main_menu)  # меню добавляется к окну
file_menu = Menu(main_menu)  # создается подменю
main_menu.add_cascade(label="Справка", menu=file_menu)
# Заполняется меню File
file_menu.add_command(label="About", command=about)
time = StringVar()
message_label = Label(text = "Время в 24-часовом формате:")
message_label.place(relx=.3,rely=.1,anchor="c")
message_entry = Entry(textvariable=time)
message_entry.place(relx=.8,rely=.1,anchor="c")
message_button = Button(text="Пуск", command=show_message)
message_button.place(relx=.5,rely=.5,anchor="c")
root.mainloop()
