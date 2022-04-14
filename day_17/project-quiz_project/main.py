from quiz_brain import QuizBrain
from question_model import QuestionModel

counter = 1
cont_game = True
quiz_brain = QuizBrain()
while cont_game:
    q = quiz_brain.get_next_question()
    question = QuestionModel(q["text"], q["answer"])
    user_answer = input(f"Q.{counter}: {question.question} True/False?:")
    quiz_brain.is_correct_answer(user_answer, question)
    quiz_brain.report_current_score()
