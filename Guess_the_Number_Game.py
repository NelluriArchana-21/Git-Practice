import random
original_num = random.randint(1,100)
count=0
guessed_number = int(input("Enter the guessed number: "))
while(True):
    if(original_num==guessed_number):
        print("You won the game with",count,"attempts",sep=' ')
        break
    elif(original_num>guessed_number):
        print("Your guessed number is too low")
        guessed_number = int(input("Enter the guessed number: "))
        count+=1
    else:
        print("Your guessed number is too high")
        guessed_number = int(input("Enter the guessed number: "))
        count+=1

    