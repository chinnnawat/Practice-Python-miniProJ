class Controller:
    def __init__(self,data):
        self.question_list = data       #ใช้เก็บคำถามทั้งหมด
        self.question_number = 0        #เริ่มต้นที่ข้อ 0 
        self.score  = 0                 #คะแนนเริ่มต้นที่ 0 คะแนน
        self.current= None              #เซทเป็นค่าว่าง ว่าทำโจทย์เข้อที่เท่าไหร่


    # Next Question
    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number+=1
        # print(self.question_number,":",current.text," (True or False)" )
        # userAnswer = input("ป้อนคำตอบ :")
        # self.checkAnswer(userAnswer,current.answer)
        return f"{self.question_number}) {self.current.text}"


    def hasQuestion(self):
        return self.question_number<len(self.question_list)


    def checkAnswer(self,userInput):
        correct_answer = self.current.answer
        if(userInput.lower() == correct_answer.lower()):
            self.score+=1
            return True
        else:
            return False
