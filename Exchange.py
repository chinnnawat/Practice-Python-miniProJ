# 1 บาทไทย = 0.026 EUR
# 1 บาทไทย = 3.486 JPY
# 1 บาทไทย = 0.031 USD
# 1 บาทไทย = 0.023 GBP

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Exchange")

# Input
money = IntVar()
Label(text="จำนวนเงิน",padx=10,font=30).grid(row=0,sticky=W)           #padx => ระยะในแนวแกน x
et1 = Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="เลือกสกุลเงิน")
Label(text="สกุลเงิน",padx=10,font=30).grid(row=1,sticky=W)
combo = ttk.Combobox(width=30,font=30,textvariable=choice)
combo.grid(row=1,column=1)
combo["value"] = ("EUR","JPY","USD","GBP")

#calculate
def calculate():
    amount = money.get()
    currency = choice.get()

    if currency == "EUR":
        result = ((amount*0.026) ,"EUR")
        et2.insert(0,result)
    elif currency == "JPY":
        result = ((amount*3.486) ,"JPY")
        et2.insert(0,result)
    elif currency == "USD":
        result = ((amount*0.031) ,"USD")
        et2.insert(0,result)
    elif currency == "GBP":
        result = ((amount*0.023) ,"GBP")
        et2.insert(0,result)
    else :
        result = "NO Info"
    et2.delete(0, END)
    et2.insert(0, result)

def clear():
    et1.delete(0, END)
    et2.delete(0, END)

    
# Output
Label(text="result",padx=10,font=30).grid(row=2,sticky=W)
et2 = Entry(font=30,width=30)
et2.grid(row=2,column=1)

Button(text="calculate",font=30,width=15,command=calculate).grid(row=3,sticky=W,column=1)
Button(text="clear",font=30,width=15,command=clear).grid(row=3,sticky=E,column=1)
root.mainloop()