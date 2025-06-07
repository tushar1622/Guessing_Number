import random
Computer_Guessing = random.randint(1,10)

while(True):
    User_input = int(input("Enter the number between 1 t 10 = "))
    if(User_input==Computer_Guessing):
        print("Your Guess is right You win .. Congrats")
        break
    elif(User_input>Computer_Guessing):
        print("Your Choosen Number is bigger then the computer Number")
    elif(User_input<Computer_Guessing):
        print("Your Number is Smaller than the Computer Number")
    else:
        print("Wrong Input")
