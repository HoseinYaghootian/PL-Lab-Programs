import random
computer_number = random.randint(0, 40)
i=0
flag=0
print("Enter number between 0 and 40")
while flag==0:
    i+=1
    user_number = int(input())

    if user_number < computer_number:
        print(f"Go Up! ⬆")

    if user_number > computer_number:
        print(f"Go Down! ⬇")

    if user_number == computer_number:
        print(f"Correct! \n The number of your guesses is {i}")
        flag=1


    
