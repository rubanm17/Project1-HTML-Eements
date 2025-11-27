from tkinter import *

window = Tk()
window.title('Tkinter no:1')
window.geometry('300x300')

greeting = Label(text="Hello World",fg="black",bg='White')

button = Button(text="click Me",fg="white",bg="Black")

entry = Entry(fg="red",bg="blue",width=50)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window,relief=FLAT,borderwidth=5)
frame.pack()
label = Label(master=frame,text='Sample Frame')
label.pack()

textbox = Text(fg='green',bg='yellow')
textbox.pack()
window.mainloop()