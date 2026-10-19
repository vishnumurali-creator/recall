cards = [
    {"question": "What does git add do?", "answer": "Moves changes to the staging area"},
    {"question": "What does git commit do", "answer": "Saves staged changes as a snapshot"},
    {"question": "What is the difference between an interpretor and a compiler", "answer": "A compiler converts the code into machine language well before running while an interpreter runs the code line by line during execution"},
    ]

q = input("Question:")
a = input("Answer:")

def make_card(question, answer):
    return{"question" : question, "answer": answer}

cards.append(make_card(q,a))
for card in cards:
    print("Q:", card["question"])
    print("A:", card["answer"])
    print()
print(len(cards))



