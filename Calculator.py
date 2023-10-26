from tkinter import *
root = Tk()
root.title("Calculator")

content = ""                    #เก็บสมการ
txt_input = StringVar(value="0")         #นำสมการมาใช้งาน และแสดงผล

# 7 100 => 7100 ,   7 + 10 => 7+10  เก็บใน content
def btn(number):                           #parameter ของการเก็บตัวเลข เช่นกด 7 เก็บ 7 ใน number
    global content                      #global = โปรแกรมสามารถเข้าถึง content ทั้งในและนอกได้เลย
    content = content+str(number)       #change number => string
    txt_input.set(content)

def calculate():
    global content
    calculate = str(eval(content))      #ฟังก์ชัน eval() ในภาษา Python จะทำการคำนวณสมการที่กำหนดในรูปของสตริงและส่งคืนผลลัพธ์เป็นตัวเลขทศนิยมหรือจำนวนเต็ม
    txt_input.set(calculate)
#calculate  7+10/5*9

def equal():                        #function การ calculate
    calculate()
    global content
    content = txt_input.get()
    #content = ""                #เคลียให้เป็นค่าว่าง

def clear():
    global content
    content = ""
    txt_input.set("")
    display.delete(0,END)
    display.insert(0,"0")

# OutPut 5 x 4
display = Entry(font=('arail',30,'bold'), fg = "white", bg="green",textvariable=txt_input,justify="right")     #arail => fontstyle ,bola => ตัวหนา ,justify => chang position txt_input
display.grid(columnspan=4)          #มีพื้นที่เป็น span 4 ส่วน

#input


#row1
btn7 = Button(fg="black",font=('arial',30,'bold'),text="7",padx=30,pady=30,command=lambda:btn(7)).grid(row=1,column=0)
btn8 = Button(fg="black",font=('arial',30,'bold'),text="8",padx=30,pady=30,command=lambda:btn(8)).grid(row=1,column=1)
btn9 = Button(fg="black",font=('arial',30,'bold'),text="9",padx=30,pady=30,command=lambda:btn(9)).grid(row=1,column=2)
btnC = Button(fg="black",font=('arial',30,'bold'),text="C",padx=32,pady=30,command=clear).grid(row=1,column=3)

#row2
btn4 = Button(fg="black",font=('arial',30,'bold'),text="4",padx=30,pady=30,command=lambda:btn(4)).grid(row=2,column=0)
btn5 = Button(fg="black",font=('arial',30,'bold'),text="5",padx=30,pady=30,command=lambda:btn(5)).grid(row=2,column=1)
btn6 = Button(fg="black",font=('arial',30,'bold'),text="6",padx=30,pady=30,command=lambda:btn(6)).grid(row=2,column=2)
btnplaus = Button(fg="black",font=('arial',30,'bold'),text="+",padx=35,pady=30,command=lambda:btn("+")).grid(row=2,column=3)

#row3
btn1 = Button(fg="black",font=('arial',30,'bold'),text="1",padx=30,pady=30,command=lambda:btn(1)).grid(row=3,column=0)
btn2 = Button(fg="black",font=('arial',30,'bold'),text="2",padx=30,pady=30,command=lambda:btn(2)).grid(row=3,column=1)
btn3 = Button(fg="black",font=('arial',30,'bold'),text="3",padx=30,pady=30,command=lambda:btn(3)).grid(row=3,column=2)
btnminus = Button(fg="black",font=('arial',30,'bold'),text="-",padx=40,pady=30,command=lambda:btn("-")).grid(row=3,column=3)

#row4
btn0 = Button(fg="black",font=('arial',30,'bold'),text="0",padx=30,pady=30,command=lambda:btn(0)).grid(row=4,column=1)
btndot = Button(fg="black",font=('arial',30,'bold'),text=".",padx=35,pady=30,command=lambda:btn(".")).grid(row=4,column=0)
btndivision = Button(fg="black",font=('arial',30,'bold'),text="/",padx=35.5,pady=30,command=lambda:btn("/")).grid(row=4,column=2)
btnmultiply= Button(fg="black",font=('arial',30,'bold'),text="x",padx=35,pady=30,command=lambda:btn("*")).grid(row=4,column=3)

#row5
btnequal = Button(fg="black",font=('arial',30,'bold'),text="=",padx=95,pady=30,command=equal).grid(row=5,column=2,columnspan=2)
btnopen = Button(fg="black",font=('arial',30,'bold'),text="(",padx=35,pady=30,command=lambda:btn("(")).grid(row=5,column=0)
btnclose = Button(fg="black",font=('arial',30,'bold'),text=")",padx=35,pady=30,command=lambda:btn(")")).grid(row=5,column=1)

root.mainloop()