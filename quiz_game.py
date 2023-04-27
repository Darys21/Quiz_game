import requests
import json

# Function to get a list of random questions and their correct answers from the Open Trivia API
def get_questions(num_questions):
    response = requests.get(f"https://opentdb.com/api.php?amount={num_questions}")
    data = json.loads(response.text)
    questions = [q["question"] for q in data["results"]]
    correct_answers = [q["correct_answer"] for q in data["results"]]
    return questions, correct_answers

# Function to play the quiz game
def play_quiz(num_questions):
    questions, correct_answers = get_questions(num_questions)
    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q}")
        answer = input("Enter your answer: ")
        if answer == "":  # Allow for blank answers
            continue
        if answer.lower() == "quit":
            break
        if answer.lower() == "skip":
            continue
        if answer.lower() == "pass":
            print(f"The correct answer is: {correct_answers[i]}")
            continue
        if answer.lower() == correct_answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answers[i]}")
    print(f"You scored {score} out of {num_questions}.")

# Main function to start the quiz game
def main():
    num_questions = 20  # Change this to change the number of questions in the quiz
    play_quiz(num_questions)

if __name__ == "__main__":
    main()
