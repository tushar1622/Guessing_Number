import random
Computer_Guessing = random.randint(1,10)
count = 1

while(True):
    User_input = int(input("Enter the number between 1 t 10 = "))
    if(User_input==Computer_Guessing):
        print("Your Guess is right You win .. Congrats")
        print("The chance to Guess the Number is =" , count)
        break
    elif(User_input>Computer_Guessing):
        print("Your Choosen Number is bigger then the computer Number")
        count = count+1
    elif(User_input<Computer_Guessing):
        print("Your Number is Smaller than the Computer Number")
        count = count+1
    else:
        print("Wrong Input")
