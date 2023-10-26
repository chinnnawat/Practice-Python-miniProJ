from tkinter import *
root = Tk()
root.title("Area Circle")
#In put Radius
Label(text="radius",font=30).grid(row=0,sticky=W)       # sticky => ชิดด้าน "(ซ้ายบน)"
radius = IntVar()
et1 = Entry(textvariable=radius,width=30,font=30)
et1.grid(row=0,column=1)

Label(text="Area",font=30).grid(row=1,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=1,column=1)

#Calculate Area
def calculate():
    r = radius.get()            # Recieve Vallue from radius
    area = 3.1415926535*r*r
    et2.delete(0,END)           # เพิ่มขั้นตอนนี้เพื่อลบข้อมูลที่อาจมีอยู่ใน et2
    et2.insert(0,area)          # การแทรกค่า area ใน et2 ตำแหน่งที่0


btn1 = Button(text="Calculate",command=calculate).grid(row=2,column=1,sticky=W)

root.mainloop()