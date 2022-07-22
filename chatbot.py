print("Welcome to my chatbot")
print("======================")
print("you may ask any one of these questions")
print("Hi")
print("How are you?")
print("Are you working?")
print("what is your name?")
print("what did you do yesterday?")
print("Quit")
while True:
    question = input("Enter one question from above list: ")

    question = question.lower()

    if question in ['hi']:
        print("Hello")
    elif question in ['how are you?', 'how do you do?']:
        print("I am fine")
    elif question in ['are you working?', 'are you doing any job']:
        print("Yes. I'm working in CUB")
    elif question in ['what is your name?']:
        print("My name is SOJOL")
        name=input("Enter your name?")
        print("Nice name and nice to meeting you", name)
    elif question in ['what did you do yesterday? ' ]:
        print("I saw a film ")
    elif question in ['quit']:
        break
    else:
        print("I don't understand what you said? ")