import csv
import random

questions = []

with open("general_knowledge_questions (1).csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        question = row['question'].strip()
        options =[row['option1'].strip(),
            row['option2'].strip(), row['option3'].strip()]
        answer = row['answer'].strip()

        questions.append({
            'question': question,
            'options': options,
            'answer': answer
        })

random.shuffle(questions)

score = 0

for q in questions:
    print("\n" + q["question"])

    options = q["options"][:]

    random.shuffle(options)

    for idx, option in enumerate(options, start=1):
        print(f"{idx}.{option}")

    try:
        choice = int(input("Your choice (1-3): "))
        if 1 <= choice <= 3:
            if options[choice - 1] == q["answer"]:
               print("Correct!")
               score += 1
            else:
                print(f"Wrong. The correct answer was {q['answer']}")
        else:
            print("Choice out of range. Skipping question.")
    except (ValueError, IndexError):
        print("Invalid input. Skipping question.")
print(f"\nYour final score is {score} out of {len(questions)}")
