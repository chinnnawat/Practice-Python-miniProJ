from tkinter import *
from controller import Controller
theam_app = '#375362'

class UserInterface:
    def __init__(self,controller : Controller) :
        self.controller = controller
        #หน้าต่างโปรแกรม
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20,pady=20,bg=theam_app)
        #พื้นที่แสดงคะแนนสอบ
        self.scoreLabel = Label(text="Score : 0",fg="white",bg=theam_app)
        self.scoreLabel.grid(row=0,column=2)
        #พื้นที่แสดงโจทย์
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="CHinnawat",font=('arial',19,'bold'),fill = theam_app)
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        #Select Button
        true_image = PhotoImage(file="Phython/Udemy/MiniProJ/QuizeApplication/images/check.png")
        self.true_button=Button(image=true_image,command=self.true_pressed)
        self.true_button.grid(row=2,column=1)

        false_image = PhotoImage(file="Phython/Udemy/MiniProJ/QuizeApplication/images/remove.png")
        self.false_button=Button(image=false_image,command=self.false_pressed)
        self.false_button.grid(row=2,column=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):        
        if self.controller.hasQuestion():       #เช็คว่าถึงข้อสุดท้ายยัง
            q_text = self.controller.nextQuestion()
            self.scoreLabel.config(text=f"Score : {self.controller.score}")         #แสดงผลคะแนน
            self.canvas.itemconfig(self.question_text,text = q_text)
        
        else :                                  #เมื่อถึงข้อสุดท้าย
            self.scoreLabel.config(text=f"Score : {self.controller.score}") 
            self.canvas.itemconfig(self.question_text,text = "End")
            #ทำการปิดปุ่ม
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    #ปุ่ม true เมื่อมีการกด
    def true_pressed(self):
        self.controller.checkAnswer("true")
        self.waitNextQuestion()

    #ปุ่ม false เมื่อมีการกด    
    def false_pressed(self):
        self.controller.checkAnswer("false")
        self.waitNextQuestion()

    def waitNextQuestion(self):
        self.window.after(300,self.get_next_question)