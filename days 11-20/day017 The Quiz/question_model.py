class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionOuter:
    def __init__(self, text, correct_answer, category):
        self.question = text
        self.correct_answer = correct_answer
        self.category = category
