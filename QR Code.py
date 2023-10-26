from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image
root = Tk()     #หน้าจอหลัก
root.title("QRCode Generator")
canvas = Canvas(root,width=400,height=500)       #หน้าจอย่อย
canvas.pack()

#ดึงข้อมูล link make QRcode
def generateQRcode():
    #ดึงข้อมูล link make QRcode
    link_name = name_entry.get()        #link_name เก็บชื่อ
    link = link_entry.get()             #link = เก็บไฟล์ QRcode
    file_name = link_name +".png"       #file_name from link_name นามสกุล .png
    #make QRcode
    url = pyqrcode.create(link)
    url.png(file_name,scale=5)
    #แสดงภาพ QR code
    image = ImageTk.PhotoImage(Image.open(file_name))       #เรียกใช้งาน ImageTk บรรทัดนี้ใช้สำหรับเปิดไฟล์ภาพและสร้าง ImageTk.PhotoImage ซึ่งเป็นวิธีการใช้ภาพใน Tkinter โดย file_name คือชื่อของไฟล์ภาพที่ต้องการเปิด เช่น "image.png" หรือ "photo.jpg" โดยภาพจะต้องอยู่ในโฟลเดอร์เดียวกับโค้ดหรือใช้เส้นทางสำหรับไฟล์ภาพ
    image_label = Label(image=image)       # สร้าง widjet  บรรทัดนี้สร้าง Widget ของ Tkinter ที่ชื่อว่า Label และกำหนดให้ Widget นี้เป็นรูปภาพที่เราได้สร้างจากข้อความที่ 1 โดย image เป็นค่าที่เก็บรูปภาพที่เราสร้างไว้ในตัวแปร ImageTk.PhotoImage
    image_label.image=image                 # เอา image ไปแปะล่าสุด บรรทัดนี้เป็นการแปะรูปภาพ (image) ลงใน widget (image_label) เพื่อให้แสดงผลลัพท์ภาพในหน้าต่าง Tkinter
    canvas.create_window(200,370,window=image_label)



# Name program
app_label = Label(root,text="QRCode Generator",font=('Arial',20,'bold'))
canvas.create_window(200,50,window=app_label)       # x => 200, y => 50

# specific name and Link URL
name_label = Label(root,text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200,100,window=name_label)


link_label = Label(root,text="URL")
canvas.create_window(200,160,window=link_label)

#Text Box
name_entry = Entry(root)
canvas.create_window(200,130,window=name_entry)

link_entry = Entry(root)
canvas.create_window(200,180,window=link_entry)

#Button Generate QR
btn=Button(text="Generate",command=generateQRcode)
canvas.create_window(200,230,window=btn)

root.mainloop()
