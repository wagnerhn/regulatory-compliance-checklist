print("Regulatory Compliance Checklist")
print("--------------------------------")

questions = [
    "Is segregation of duties implemented?",
    "Are regulatory requirements documented?",
    "Are compliance policies formally approved?",
    "Is there periodic control testing?",
    "Are compliance responsibilities clearly assigned?",
    "Is regulatory monitoring performed regularly?"
]

score = 0

for question in questions:
    answer = input(question + " (y/n): ")
    if answer.lower() == "y":
        score += 1

total = len(questions)
percentage = (score / total) * 100

print("\nCompliance Score:", round(percentage,2), "%")

if percentage >= 80:
    print("Risk Level: Low")
elif percentage >= 60:
    print("Risk Level: Medium")
else:
    print("Risk Level: High")

