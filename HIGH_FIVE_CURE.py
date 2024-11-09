#HIGH FIVE CURE


def mathQuestion(userAns, ans):
    global question
    question = 0
    while question == 0:
        if userAns == ans:
            print ("The journey continues")
            question = 1
            break
        else:
            userAns = input("Try again")
    return question


def yesOrNo():
    global question
    question = 0
    while question == 0:
        answer = input(" y or n?\n")
        if answer == "n":
            print ("You lose the game.")
            break
        elif answer == "y":
            print ("The journey continues")
            question = 1
            break

        elif  answer == "yn":
            print ("speacial line of text")
            break

        else:
            print ("That's not how to answer the QUESTION!!!!!!!!!!!!!!!!!")
    return question



print ("OH, POOOOOOP!")
print("You found out that you are alergec to high fives.")
#global question
question = 0
while question == 0:
    print ("Do you want to find the cure to the high five allergy?")
    answer = input(" y or n?")
    if answer == "n":
        print ("congradualations you won the game")
        break
    elif answer == "y":
         print ("The journey continues")
         question = 1
         break

    elif  answer == "yn":
         print ("speacial line of text")


    else: print ("That's not how to answer the QUESTION!!!!!!!!!!!!!!!!!")


while question == 1:
    print ("The worlds top scientists, including Bob Clark, have found out ")
    print ("that the cure for the high five allergy is in the SPOOKY castle.")
    print("Do you want to go into the SPOOKY castle?\n")
    yesOrNo()
    if question == 0:
        break
    print (question)

    print ("Hi. I am Brick Dude.")
    print ("I have a Brick head.")
    print ("People always tell me that my head is ")
    print ("weird and TOO BIG. Can you tell me how big my head is?")
    yesOrNo()
    if question == 0:
        break
    #print (question)
    print ("Oh! Thank you soooo much.")
    print ("My head is 4 feet hight, 8 feet long and 20 feet wide.")
    userAns = input("what is the volume of my head in cubic feet?")
    ans ="640"
    mathQuestion(userAns, ans)
    print ("Wow! Really, my head is that big!?")
    print ("I can hardly believe it!")

    print("Hi! I am Fist Bump Troll")
    input("Can you tell me why I have 3 fingers?")
    print("That is a very insightful answer.")
    print("Fist bump for Spring Break!!!")

    userAns = input("Hi! My identity is a mystry. Do you know who I am?")
    if userAns == "yes":
        print('You are a lier! Run!!!!!!!!!!!!!!!!!!')
    elif userAns == "no":
        print("I'm the MYSTEROUS CREATURE! Run!!!!!!!!!!!!!'")
    else:
        print("I don't understand what you said.")
        print("I'm the MYSTEROUS CREATURE! Run!!!!!!!!!!!!!'")
    print("Run!")
    input("Press Enter to run!")
    input("Run!")
    input("Run!")
    input("Run!")
    input("Run!")
    input("Run!")

    print("You have made it to the end of a long hallway.")
    print("A woman is there in a long pink dress.")
    print("Hi. You must be looking for the cure for High Five Allergy.")
    print('"How did you know?", you ask.')
    print("I am Ms. Hexxagon, the witch of the SPOOKY castle.")
    print("I made the cure to the High Five Allergy, through magic.")
    print("Go down the hall and to the left, and you will find the cure")
    print("to the high five allergy.")
    print("You say 'Thanks! See you later.'")
    userAns = input("You go down the hallway. Do you take a left or a right?")
    if userAns == "left":
        print("You found the cure! You win the game!")
        print("Go high five someboby elf!")
        print("See you in the next game.")
    else:
        print("You lose! Bye!")
    break


