from tkinter import *
from tkinter import messagebox
import os
def show_about():
 messagebox.showinfo("О программе", "Переводчик раскладки клавиатуры\nВерсия 1.1\nАртём Лазарев, 2018\nУтилита предназначенная для перевода раскладки клавиатуры")
def show_message():
 state = var.get()
 if state == False:
  word = word_entry.get()
  source = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m','.','/'];
  target = ['й','ц','у','к','е','н','г','ш','щ','з','ф','ы','в','а','п','р','о','л','д','ж','я','ч','с','м','и','т','ь','ю','.'];
  for i in range(len(source)):
   word = word.replace(source[i],target[i])
  messagebox.showinfo("Результат",word)
 if state == True:
  word = word_entry.get()
  source = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m','.','/'];
  target = ['й','ц','у','к','е','н','г','ш','щ','з','ф','ы','в','а','п','р','о','л','д','ж','я','ч','с','м','и','т','ь','ю','.'];
  for i in range(len(target)):
   word = word.replace(target[i],source[i])
  messagebox.showinfo("Результат",word)
  
root = Tk()
root.title("Переводчик раскладки")
root.geometry("300x250")
main_menu = Menu(root)       # формируется меню
root.config(menu=main_menu)  # меню добавляется к окну
file_menu = Menu(main_menu)  # создается подменю
main_menu.add_cascade(label="Справка", menu=file_menu)
# Заполняется меню File
file_menu.add_separator()
file_menu.add_command(label="О программе", command=show_about)
message = StringVar()
message_label = Label(text = "Слово:")
message_label.place(relx=.1,rely=.1,anchor="c")
word_entry = Entry(textvariable=message)
word_entry.place(relx=.5,rely=.1,anchor="c")
var = BooleanVar()
cb = Checkbutton(text="Запустить обратный процесс", variable=var)
cb.place(relx=.4,rely=.3,anchor="c")
message_button = Button(text="Перевести", command=show_message)
message_button.place(relx=.5,rely=.5,anchor="c")
root.mainloop()
