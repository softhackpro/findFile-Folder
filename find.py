#!/usr/bin/python3

from tkinter import *
import fnmatch
import os

def find():
	output_label.delete(0, 'end')
	rootPath = str(entry.get())
	pattern =  str(entry1.get())
	 
	for root, dirs, files in os.walk(rootPath):
		for filename in fnmatch.filter(files, pattern):
			locate = os.path.join(root, filename)
			output_label.insert(END, str(locate))
			#output_label.configure(text="Path: " + locate)


root = Tk()
root.title("File or Folder Finder")
root.geometry("850x550+10+10")
root.resizable(False, False) 
root.configure(background="#d9d9d9")

frame = Frame(root)
h = Scrollbar(frame, orient = 'horizontal')  
h.pack(side = BOTTOM, fill = X)  
v = Scrollbar(frame)  
v.pack(side = RIGHT, fill = Y)

message_label = Label(text="Enter Directory name", font=('Verdana', 16, 'bold'),bg='green', fg='white')
message_label1 = Label(text="Enter Filename ", font=('Verdana', 16, 'bold'),bg='green', fg='white')
path = Label(text='Location and Path List ', font=('Verdana', 17, 'bold'),bg='red', fg='white')
#output_label = Entry(bd=3, font=('Verdana', 12), bg='white', fg='red', width=35)
output_label = Listbox(frame, xscrollcommand = h.set, yscrollcommand = v.set, bd=3, font=('Verdana', 12), bg='white', fg='red', width=85, height=13)
entry = Entry(bd=2, font=('Verdana',12, 'bold'), bg='white', fg='red', width=25)
entry1 = Entry(bd=2, font=('Verdana',12, 'bold'), bg='white', fg='red', width=15)

check_button = Button(bd=3, text="Find", font=('Verdana', 16), bg='red', fg='white', command=find)
close_button = Button(bd=3, text="Close", font=('Verdana', 16), bg='red', fg='white', command=root.destroy)


message_label.place(x=20, y=50)
message_label1.place(x=20, y=100)
entry.place(x=300, y=50)
entry1.place(x=300, y=100)
check_button.place(x=300, y=150)
close_button.place(x=200, y=150)
path.place(x=250, y=220)
frame.pack(side=BOTTOM)
#output_label.place(x=250, y=250)
output_label.pack(side = BOTTOM, fill = X)
h.config(command=output_label.xview)  
v.config(command=output_label.yview)

mainloop()

