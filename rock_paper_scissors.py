import random
options=["rock","paper","scissors"]

player_score=0
computer_score=0

while True:
    user_choice=input("Enter rock,paper or scissors: ").lower().strip()

    while user_choice not in["rock","paper","scissors"]:
        print("Invalid response ")
        user_choice=input("Enter rock,paper or scissors: ").lower().strip()
    computer_choice=random.choice(options)

    print(f"your choice is: {user_choice} ")
    print(f"Computer choice is: {computer_choice}")
    
    if computer_choice==user_choice:
        print("Its a tie")
    elif (user_choice=='rock' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='paper')or (user_choice=='paper' and computer_choice=='rock'):
        print("User wins this round")
        player_score+=1
    else:
        print("Computer wins")
        computer_score+=1
    
    choce=input("Do you wish to continue(yes or no): ").lower().strip()
    if choce =="no":
        break
    else:
        continue

print(f"Your total score is : {player_score}")
print(f"Computer total score is : {computer_score}")

if player_score> computer_score:
    print("Congratulations you are the overall winner!!!!")
elif computer_score>player_score:
    print("The computer is the overall winner")
else:
    print("It's a tie overall")

print("Thank you for playing !!!🤩")



