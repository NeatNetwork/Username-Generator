adjectives = ['sassy', 'sad', 'jumpy', 'quiet', 'sleepy', 'noisy', 'neat', 'messy', 'organised', 'thinking', 'working', 'trying', 'typing', 'typed', 'done', 'thought', 'motorised', 'energised', 'troubled', 'sleepy']
objects = ['porpoise', 'turtle', 'frog', 'goat', 'leamur', 'telly', 'table', 'helmet', 'computer', 'basket', 'tree', 'grass', 'flower', 'pot', 'plate', 'fork', 'beef', 'pork', 'chicken']
def go():
    import random
    first = random.choice(adjectives)
    second = random.choice(objects)
    third = random.choice(range(100, 999))
    print("your username is " + str(first) + str(second) + str(third))
    import time
    time.sleep(5)
    print("----------------------------------")
    a = input("\nwould you like another username? \n")
    if a.lower() == "yes":
        print("----------------------------------")
        go()
    else:
        exit(1)
a = input("Welcome to Neat's Username Generator")
go()

