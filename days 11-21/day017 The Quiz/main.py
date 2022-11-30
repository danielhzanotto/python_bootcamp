from question_model import Question, QuestionOuter
# from data import question_data
# from quiz_brain import QuizBrain
from outer_data import data
from quiz_brain_outer import QuizBrainOuter


question_bank_2 = []
# question_bank = []
question_data = data
# quiz_brain = QuizBrain(question_bank)
quiz_brain = QuizBrainOuter(question_bank_2)

# for data in question_data:
#     question_text = data["text"]
#     question_answer = data["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

for d in data:
    question_text = d["question"]
    question_answer = d["correct_answer"]
    question_category = d["category"]
    new_question = QuestionOuter(
        question_text, question_answer, question_category)
    question_bank_2.append(new_question)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()
quiz_brain.final_score()
