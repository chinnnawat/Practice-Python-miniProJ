from cgitb import text
from tkinter import *
from tkinter import font
from googletrans import Translator


def translate():
    input_text = text1.get('1.0','end-1c')         #ดึงข้อความจาก text1 มาเก็บในตัวแปล message, end-1c คือการลบช่องว่างด้านหลังที่ต้องการพิมพ์
    translator = Translator()
    output = translator.translate(text=input_text,src='en',dest='th')
    text2.delete('1.0', 'end')
    text2.insert('1.0', output.text)
    

def reset():
    text1.delete(1.0,'end')
    text2.delete(1.0,'end')

# Display size
root = Tk()         # root = หน้าจอโปรแกรม แก้สี ภาพ การแสดงได้หมด
root.title("Google Translate EN-TH")
root.geometry("530x300")
root.maxsize(530,300)
root.minsize(530,300)

# widget
label = Label(text="English - Thai",font=('Arial',25,'bold'))
label.place(x=150,y=20)    #Position of label

# เก็บข้อความภาษาอังกฤษ
text1=Text(root,width=30,height=10)
text1.place(x=10,y=70)

# เก็บข้อความภาษาไทย
text2=Text(root,width=30,height=10)
text2.place(x=260,y=70)

# ปุ่ม
translatebtn = Button(root,text="แปลภาษา",command=translate)
translatebtn.place(x=180,y=250)

clearbtn = Button(root,text="Clear",command=reset)
clearbtn.place(x=280,y=250)

root.mainloop()


