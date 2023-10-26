# RUN Program
from question import Question
from data import question_data
from controller import Controller
from ui import UserInterface

all_question = []

#สร้างโจทย์ปัญหา
for item in question_data:      #เก็บข้อมูล question_data ในตัวแปล item โดยการวน loop
    text = item["text"]
    answer = item["answer"]
    question = Question(text,answer)
    all_question.append(question)       #โยนโจทย์ ปห ทั้งหมด ลงใน all_question

# print(all_question[0].text)      #show text [0] ตำแหน่งที่ 0
# print(all_question[0].answer)       #show answer [0] ตำแหน่งที่ 0

#สร้างแผงควบคุม
controller = Controller(all_question)

#เรียกใช้การแสดงผล
userInterface=UserInterface(controller)



