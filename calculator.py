from tkinter import *
from PIL import Image, ImageTk
#To declare tk

root=Tk()
root.geometry('350x350') #Total size of widget
root.title("SIMPLE CALCULATOR") #Title of the widget
img = ImageTk.PhotoImage(file='calculator-icon.png')

root.iconphoto(False,img)

#Create the input form

e = Entry(root,width=50,borderwidth=10,fg="white",bg="black")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#define functions...

def button_click(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
    	e.insert(0, f_num + int(second_number))
    if math == "subtraction":
    	e.insert(0, f_num - int(second_number))
    if math == "mulitiplication":
    	e.insert(0, f_num * int(second_number))
    if math == "Division":
    	e.insert(0, f_num / int(second_number))	

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)	

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "mulitiplication"
    f_num = int(first_number)
    e.delete(0,END)	

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0,END)

#Creating Buttons with some Commands to perform their actions
                                              #Lambda fn is allows the CMD calls functions
button_1 = Button(root,text="1",padx=40,pady=10,command=lambda:button_click(1),bg="#FFFF66")
button_2 = Button(root,text="2",padx=40,pady=10,command=lambda:button_click(2),bg="#FFFF66")
button_3 = Button(root,text="3",padx=40,pady=10,command=lambda:button_click(3),bg="#FFFF66")
button_4 = Button(root,text="4",padx=40,pady=10,command=lambda:button_click(4),bg="#FFFF66")
button_5 = Button(root,text="5",padx=40,pady=10,command=lambda:button_click(5),bg="#FFFF66")
button_6 = Button(root,text="6",padx=40,pady=10,command=lambda:button_click(6),bg="#FFFF66")
button_7 = Button(root,text="7",padx=40,pady=10,command=lambda:button_click(7),bg="#FFFF66")
button_8 = Button(root,text="8",padx=40,pady=10,command=lambda:button_click(8),bg="#FFFF66")
button_9 = Button(root,text="9",padx=40,pady=10,command=lambda:button_click(9),bg="#FFFF66")
button_0 = Button(root,text="0",padx=40,pady=10,command=lambda:button_click(0),bg="#FFFF66")

button_clear = Button(root,text="clear",padx=79,pady=10,command=button_clear,bg="black",fg="white")
button_equal = Button(root,text="=",padx=91,pady=10,command=button_equal,bg="white")
button_add = Button(root,text="ADD",padx=39,pady=10,command=button_add,bg="violet",fg="white")
button_sub = Button(root,text="SUB",padx=41,pady=10,command=button_sub,bg="blue",fg="white")
button_mul = Button(root,text="MUL",padx=39,pady=10,command=button_mul,bg="green",fg="white")
button_div = Button(root,text="DIV",padx=40,pady=10,command=button_div,bg="gray",fg="white")

#Creating Grids for the Buttons...

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)


button_0.grid(row=4, column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)


root.mainloop()