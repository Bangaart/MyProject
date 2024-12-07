import os
from string import digits

os.environ['TCL_LIBRARY'] = r'C:\Users\Arthur\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Arthur\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

from tkinter import Tk, Text, Entry, StringVar
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("300x200+400+200")
root.resizable(False,False)
root.minsize(400,300)
root.maxsize(600,500)
entry_text = StringVar()
entry = Entry( font= ("Arial", 14), textvariable=entry_text)
entry.grid(row = 0, column =0, columnspan = 4, sticky = "we")
def on_button_click(symbol):
    if symbol == "=":
        try:
            result = eval(entry_text.get())
            entry_text.set(result)
        except Exception:
            entry_text.set("Error")

    elif symbol == "C":
        entry_text.set("")
    else:
        entry_text.set(entry_text.get() + symbol)
DIGITS_SIGNS = [("1", 1,0),("2" ,1 ,1),("3",1,2), ("+", 1,3),
                ("4",2,0),("5",2,1),("6",2,2), ("-", 2,3),
                ("7",3,0),("8",3,1),("9",3,2), ("*",3,3),
                ("C",4,0), ("0",4,1), ("=",4,2),("/",4,3)]
for (text, row,column) in DIGITS_SIGNS:
        btn = ttk.Button(text = text,width=10, command= lambda t = text: on_button_click(t))
        btn.grid(row = row , column = column, sticky= "nsew")






root.mainloop()