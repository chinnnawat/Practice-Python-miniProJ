from tkinter import *
from gtts import gTTS
def convertToMP3():
    #ดึงข้อมูลมาใช้งาน
    word = text_entry.get()        #เอาข้อมูลที่ป้อนในกล่อง text entry มาใช้
    language = 'th'             # แปลงเป็น ภาษาไทย
    #แปลงข้อความเป็นเสียง
    output = gTTS(text=word,lang=language,slow=False)    #ดึงมาใช้
    output.save("sound.mp3")           



root = Tk()
root.title("text to speech")
canvas = Canvas(root,width=400,height=300)
canvas.pack()

app_label = Label(text="Text to Speech",font=('arial',20,'bold'))
canvas.create_window(200,100,window=app_label)

text_entry = Entry(root)
canvas.create_window(200,180,window=text_entry)

bnt = Button(text="Change",command=convertToMP3)
canvas.create_window(200,230,window=bnt)
root.mainloop()