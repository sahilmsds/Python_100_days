class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, current_question, user_answer):
        if user_answer == current_question.answer:
            print("You git it Right")
            self.score += 1
        else:
            print("That's wrong Answer.")
        print(f"The correct answer is {current_question.answer}")
        print(f'Your current Score is {self.score}/{self.question_number}\n')

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(current_question, user_answer)