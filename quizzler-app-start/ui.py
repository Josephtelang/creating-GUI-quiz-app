THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain 
# from main import quiz
# quiz = QuizBrain()
class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.minsize(width=300,height=400)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,highlightthickness=0)
        right_img = PhotoImage(file="./images/true.png")
        wrong_img = PhotoImage(file="./images/false.png")
        self.question_text = self.canvas.create_text(150,125,width=290,text="quiz question",fill=THEME_COLOR,font=("Arial",20,"italic"))
        
        
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        # label
        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1)
        
        # button
        self.right_button = Button(image=right_img,highlightthickness=0,command=self.answer_true)
        self.right_button.grid(row=2,column=0)
        self.wrong_button = Button(image=wrong_img,highlightthickness=0,command=self.answer_false)
        self.wrong_button.grid(row=2,column=1)
        self.generate_new_question()
        
        self.window.mainloop()

    def generate_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.generate_new_question)
    