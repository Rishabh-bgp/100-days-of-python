"""Day 17 - Quiz Game: creating your own classes (Question, QuizBrain).

API-free: the course pulls questions from the Open Trivia DB; this reads a bundled questions.json.
"""
from quiz import QuizBrain, load_questions


def main(ask=input) -> int:
    quiz = QuizBrain(load_questions())
    while quiz.still_has_questions():
        prompt = quiz.next_question()
        try:
            answer = ask(f"{prompt} (True/False): ")
        except EOFError:
            break
        if quiz.check_answer(answer):
            print("You got it right!")
        else:
            print(f"That's wrong. The correct answer was: {quiz.current.answer}.")
        print(f"Your current score is: {quiz.score}/{quiz.question_number}\n")
    print(f"You've completed the quiz. Final score: {quiz.score}/{quiz.question_number}")
    return quiz.score


if __name__ == "__main__":
    main()
