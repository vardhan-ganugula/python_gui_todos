import tkinter
from tkinter import *
import os
from PIL import Image, ImageTk

class toDoList:
    def __init__(self) -> None:
        self.fileName = 'todos.txt'
        self.task_file = []
        if not os.path.exists(self.fileName):
            open(self.fileName, 'x')
    def open_file(self, listbox):
        with open(self.fileName, 'r') as file:
            tasks = file.readlines()
        for task in tasks:
            if task != '\n':
                self.task_file.append(task)
                listbox.insert(END, task)

    def addTask(self, inputTask,listBox):
        task = inputTask.get()
        if task:
            self.task_file.append(task)
            listBox.insert(END, task)
            with open(self.fileName, 'a') as file:
                file.write(task + '\n')
            inputTask.delete(0, END)

    def deleteTask(self, listBox):
        selected_index = listBox.curselection()
        if selected_index:
            index = int(selected_index[0])
            task = listBox.get(index)
            del self.task_file[index]
            listBox.delete(index)
            with open(self.fileName, 'w') as file:
                for task in self.task_file:
                    file.write(task + '\n')

    def gui(self):
        tk = tkinter.Tk()
        tk.title("To do list")
        tk.geometry("700x800+400+100")
        tk.resizable(False,False)
        imageIcon = PhotoImage(file='imgs/icon.png')
        tk.iconphoto(False,imageIcon)
        
        #menu frame
        menu = Frame(master=tk, width=100)
        logo = Image.open('imgs/icon.png')
        resized_logo = logo.resize((70, 70))
        tk_logo = ImageTk.PhotoImage(resized_logo)
        menu_left = Label(master=menu, image=tk_logo)
        menu_right = Label(master=menu, text='TO DO LIST', font=("Impact",25), fg='#ffb000', background='#4772fa', width=100)
        menu_left.pack(side='left')
        menu_right.pack(side='right')
        menu.pack()

        #body frame
        main_frame = Frame(master=tk, width=400, height=50)
        inputTask = Entry(master=main_frame, width=15, font=("Comic Sans MS",18), bd=0)
        button = Button(master=main_frame, text="ADD", width=10, bg="#4772fa", fg="#fff", bd=0, font=("Comic Sans MS",11), cursor="plus", command=lambda: self.addTask(inputTask,listBox))
        inputTask.pack(side='left', padx=1)
        inputTask.focus()
        button.pack(side='right')
        main_frame.pack(pady=20)

        #textBox

        textFrameBox = Frame(master=tk, width=700, height=280, bg="#FFC436")
        textFrameBox.pack(pady=10)
        listBox = Listbox(master=textFrameBox, font=("arial", 21), width=40, height=16, bd=0, fg="#000",cursor="hand2", selectbackground="#F4F27E", selectforeground="#6DB9EF")
        listBox.pack(side=LEFT, fill=BOTH,padx=2, pady=2)
        scroolbar = Scrollbar(textFrameBox)
        scroolbar.pack(side=RIGHT, fill=BOTH)
        listBox.config(yscrollcommand=scroolbar.set)
        scroolbar.config(command=listBox.yview)
        self.open_file(listBox)

        #delete tasks
        DeleteIcon = PhotoImage(file="imgs/delete.png")
        Button(tk,image=DeleteIcon, bd=0, cursor="hand2", command=lambda: self.deleteTask(listBox)).pack(pady=1)


        tk.mainloop()



tl = toDoList()
tl.gui()