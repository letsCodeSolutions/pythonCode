from random import choice
questions =["Why is the sky blue? ", "Why is there a face on the moon? ", "Where are the dinasour? "]
question = choice(questions)
answer = input(question).strip().title()
while answer != "Just Because":
    answer = input("Why? ").strip().title()
print("ohh..")
