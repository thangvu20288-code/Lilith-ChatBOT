import json

# Đọc dữ liệu từ brain.json
with open("brain.json", "r", encoding="utf-8") as file:
    brain = json.load(file)

print("Lilith-ChatBOT v1.0")
print("Type 'exit' to quit.\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    found = False

    for entry in brain["knowledge"]:
        if user_question.lower() == entry["question"].lower():
            print("Bot:", entry["answer"])
            found = True
            break

    if not found:
        print("Bot: I don't know the answer.")
