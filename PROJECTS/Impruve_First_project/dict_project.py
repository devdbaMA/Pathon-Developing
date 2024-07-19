import json
import random

# Define the dictionary with questions and answers
qa_dict = {
    "What is the capital of France?": {
        "correct": "Paris",
        "incorrect": ["London", "Berlin", "Madrid"]
    },
    "What is the largest planet in our solar system?": {
        "correct": "Jupiter",
        "incorrect": ["Earth", "Saturn", "Mars"]
    },
    "Who wrote 'To Kill a Mockingbird'?": {
        "correct": "Harper Lee",
        "incorrect": ["Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"]
    },
    "What is the boiling point of water?": {
        "correct": "100°C",
        "incorrect": ["90°C", "110°C", "120°C"]
    },
    "What is the speed of light?": {
        "correct": "299,792,458 meters per second",
        "incorrect": ["150,000,000 meters per second", "300,000,000 meters per second", "250,000,000 meters per second"]
    },
    "What is the smallest prime number?": {
        "correct": "2",
        "incorrect": ["1", "3", "5"]
    },
    "Who painted the Mona Lisa?": {
        "correct": "Leonardo da Vinci",
        "incorrect": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet"]
    },
    "What is the capital of Japan?": {
        "correct": "Tokyo",
        "incorrect": ["Beijing", "Seoul", "Bangkok"]
    },
    "Who developed the theory of relativity?": {
        "correct": "Albert Einstein",
        "incorrect": ["Isaac Newton", "Nikola Tesla", "Galileo Galilei"]
    },
    "What is the tallest mountain in the world?": {
        "correct": "Mount Everest",
        "incorrect": ["K2", "Kangchenjunga", "Lhotse"]
    },
    "What is the chemical symbol for gold?": {
        "correct": "Au",
        "incorrect": ["Ag", "Pb", "Pt"]
    },
    "Who is known as the father of computers?": {
        "correct": "Charles Babbage",
        "incorrect": ["Alan Turing", "John von Neumann", "Steve Jobs"]
    },
    "What is the main ingredient in traditional sushi?": {
        "correct": "Rice",
        "incorrect": ["Fish", "Seaweed", "Soy Sauce"]
    },
    "What is the largest ocean on Earth?": {
        "correct": "Pacific Ocean",
        "incorrect": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
    },
    "What is the square root of 64?": {
        "correct": "8",
        "incorrect": ["6", "7", "9"]
    },
    "Who was the first president of the United States?": {
        "correct": "George Washington",
        "incorrect": ["Thomas Jefferson", "John Adams", "Benjamin Franklin"]
    },
    "What is the currency of the United Kingdom?": {
        "correct": "Pound Sterling",
        "incorrect": ["Euro", "Dollar", "Yen"]
    },
    "What is the primary gas in the Earth's atmosphere?": {
        "correct": "Nitrogen",
        "incorrect": ["Oxygen", "Carbon Dioxide", "Hydrogen"]
    },
    "Who wrote the play 'Romeo and Juliet'?": {
        "correct": "William Shakespeare",
        "incorrect": ["Christopher Marlowe", "Ben Jonson", "John Milton"]
    },
    "What is the hardest natural substance on Earth?": {
        "correct": "Diamond",
        "incorrect": ["Gold", "Iron", "Quartz"]
    }
}

# Specify the file path
file_path = "qa_dict.json"

# Save the dictionary to a file
with open(file_path, 'w') as file:
    json.dump(qa_dict, file)

print(f"Dictionary saved to {file_path}")


# Function to ask questions
def ask_question(qa_dict):
    questions = list(qa_dict.keys())
    asked_questions = set()

    while len(asked_questions) < len(questions):
        question = random.choice(questions)
        if question in asked_questions:
            continue

        asked_questions.add(question)
        options = qa_dict[question]["incorrect"] + [qa_dict[question]["correct"]]
        random.shuffle(options)

        print(f"\nQuestion: {question}")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")

        answer = input("Your answer (1-4): ")

        try:
            answer_idx = int(answer) - 1
            if options[answer_idx] == qa_dict[question]["correct"]:
                print("Correct! Here's the next question.")
            else:
                print(f"Wrong! The correct answer was: {qa_dict[question]['correct']}")
                break
        except (ValueError, IndexError):
            print("Invalid answer. Please enter a number between 1 and 4.")
            break


# Load the dictionary from the file
with open(file_path, 'r') as file:
    loaded_qa_dict = json.load(file)

# Start the quiz
ask_question(loaded_qa_dict)
