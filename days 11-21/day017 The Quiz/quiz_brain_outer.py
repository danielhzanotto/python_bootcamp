class QuizBrainOuter:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, guess, correct):
        if guess.lower() == correct.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong :/")

        print(f"The correct answer is {correct}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        get_question = self.questions_list[self.question_number]
        self.question_number += 1
        print(
            f"Q {self.question_number} ({get_question.category}): {get_question.question} True or False?")
        guess = input()
        self.check_answer(guess, get_question.correct_answer)

    def final_score(self):
        print(
            f"Your final score is {self.score} out of {self.question_number}")
