import requests
import json
import time

# Reuse the HTTP connection using a session object
session = requests.Session()

# Use a generator to retrieve questions one at a time
def get_questions(num_questions, language):
    if language == "english":
        lang_code = "en"
    elif language == "french":
        lang_code = "fr"
    else:
        raise ValueError(f"Invalid language: {language}")
    url = f"https://opentdb.com/api.php?amount={num_questions}&lang={lang_code}"
    for _ in range(num_questions):
        response = session.get(url)
        data = json.loads(response.text)
        question = data["results"][0]["question"]
        correct_answer = data["results"][0]["correct_answer"]
        yield question, correct_answer

# Combine the two versions of the play_quiz() function
def play_quiz(num_questions, language, timeout=None):
    questions = get_questions(num_questions, language)
    score = 0
    for i, (question, correct_answer) in enumerate(questions):
        print(f"Question {i+1}: {question}")
        answer = input("Enter your answer (or 'skip', 'pass', or 'quit'): ")
        if answer == "":  # Allow for blank answers
            continue
        if answer.lower() == "quit":
            break
        if answer.lower() == "skip":
            continue
        if answer.lower() == "pass":
            print(f"The correct answer is: {correct_answer}")
            continue
        # Only accept 'yes' or 'oui' as valid answers for French questions
        if language == "french" and not answer.lower().startswith("oui"):
            print("Invalid answer. Please respond with 'oui' or leave blank to skip the question.")
            continue
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            if timeout is not None:
                time.sleep(timeout)
    print(f"You scored {score} out of {num_questions}.")
    return score

# Main function to start the quiz game
def main():
    print("Hello and welcome to Quizzy!")
    num_questions = 20  # Change this to change the number of questions in the quiz
    language = input("Choose your preferred language (English or French): ").lower()
    while language not in ["english", "french"]:
        language = input("Invalid language. Please choose English or French: ").lower()
    score = play_quiz(num_questions, language)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again == "yes" or play_again == "oui":
        score = play_quiz(num_questions, language)
        play_again = input("Do you want to play again? (yes/no): ").lower()
    print(f"Thanks for playing! Your final score is {score} out of {num_questions}.")

if __name__ == "__main__":
    main()
