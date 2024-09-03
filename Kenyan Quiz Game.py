def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "What is the capital city of Kenya?",
        "options": ["A. Mombasa", "B. Kisumu", "C. Nairobi", "D. Nakuru"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following is the largest freshwater lake in Kenya?",
        "options": ["A. Lake Turkana", "B. Lake Victoria", "C. Lake Naivasha", "D. Lake Baringo"],
        "answer": "B"
    },
    {
        "prompt": "Who was the first President of Kenya?",
        "options": ["A. Daniel arap Moi", "B. Uhuru Kenyatta", "C. Jomo Kenyatta", "D. Mwai Kibaki"],
        "answer": "C"
    },
    {
        "prompt": "Which is the national language of Kenya?",
        "options": ["A. English", "B. Swahili", "C. Kikuyu", "D. Luo"],
        "answer": "B"
    },
    {
        "prompt": "What is the currency used in Kenya?",
        "options": ["A. Kenyan Dollar", "B. Kenyan Shilling", "C. Kenyan Pound", "D. Kenyan Rupee"],
        "answer": "B"
    }
]

# Run the quiz
run_quiz(questions)
