from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox

app = Tk()
app.title('Textpadd')

edit = Text()
edit.pack()

filepath = ''

dark_mode = False


def saveFilePath(path):
    global filepath
    filepath = path
    

def save():
    if filepath == '':
        path = asksaveasfilename(filetypes=[("textdata Files", "*.txt"),("All Files", "*.*")])
    else:
        path = filepath
        
    with open(path, 'w') as file:
            textdata = edit.get('1.0', END)
            file.write(textdata)
            saveFilePath(path)


def saveAs():
    path = asksaveasfilename(filetypes=[("textdata Files", "*.txt"),("All Files", "*.*")])

    with open(path, 'w') as file:
            textdata = edit.get('1.0', END)
            file.write(textdata)
            saveFilePath(path)


    
def openFile():
    path = askopenfilename(filetypes=[("textdata Files", "*.txt"),("All Files", "*.*")])
    with open(path, 'r') as file:
        textdata = file.read()
        edit.delete('1.0', END)
        edit.insert('1.0', textdata)
        saveFilePath(path)


def darkMode():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        edit.config(
            bg="black",
            fg="white",
            insertbackground="white"
        )
        app.config(bg="black")
        filemenu.config(bg="black", fg="white")

    else:
        edit.config(
            bg="white",
            fg="black",
            insertbackground="black"
        )
        app.config(bg="white") 
        filemenu.config(bg="white", fg="black")


def exitApp():
    answer = messagebox.askyesno(
        "Exit",
        "Do you want to exit?"
    )

    if answer:
        app.destroy()



menu_bar = Menu(app)
app.config(menu=menu_bar)


filemenu = Menu(menu_bar, tearoff=0)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_command(label='Dark/Light Mode', command=darkMode)
filemenu.add_command(label='Exit', command=exitApp)
menu_bar.add_cascade(label='Options', menu=filemenu)

app.config(menu=menu_bar)


app.mainloop()
