print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Haunted House.")
print("Your mission is to find the hidden treasure.")

print("You are standing in front of a mysterious haunted house.")
print("The house has two doors. One on the left and one on the right.")

choice1 = input('Which door do you choose? "left" or "right"? \n').lower()

if choice1 == "left":
    print("You enter the left door and find yourself in a dark hallway.")
    print("As you move forward, you hear eerie sounds coming from different directions.")
    choice2 = input('What do you do? "continue" or "turn back"? \n').lower()
    if choice2 == "continue":
        print("You muster up your courage and continue down the hallway.")
        print("You come across three doors: one red, one green, and one blue.")
        choice3 = input('Which door do you choose? "red", "green", or "blue"? \n').lower()
        if choice3 == "green":
            print("Congratulations! You open the green door and find the hidden treasure.")
            print("You have successfully completed your mission. Well done!")
        elif choice3 == "red":
            print("Oh no! The red door leads to a room filled with traps. Game over!")
        elif choice3 == "blue":
            print("Oops! The blue door opens to a room with no way out. Game over!")
        else:
            print("You hesitate and cannot decide which door to choose. The house consumes you. Game over!")
    else:
        print("You turn back and exit the haunted house. You have escaped the danger. Good decision!")
        print("Although you didn't find the treasure, you are safe. Game over!")
else:
    print("You open the right door and find yourself in a small, empty room.")
    print("There is no treasure here. You should have chosen the other door. Game over!")
