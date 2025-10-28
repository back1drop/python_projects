import random


def Checker():
    score=0
    while True:
        print("Please choose a difficulty level")
        print("1. Easy Level")
        print("2. Medium Level")
        print("3. Hard Level")
        print("4. quit")
        
        level=input("Enter your choice(1-4): ").strip()
        while level not in ['1','2','3','4']:
            print("Invalid option.Enter a valid option ")
            level=input("Enter your choice(1-3): ").strip()
        if level=='1':
            operation=random.choice(['-','+'])
            number1=random.randint(50,100)
            number2=random.randint(1,50)
        elif level=="2":
            operation=random.choice(['-','+','*'])
            number1=random.randint(100,200)
            number2=random.randint(50,100)
        elif level=="3":
            operation=random.choice(['-','+','*','/'])
            number1=random.randint(200,300)
            number2=random.randint(100,200)
        else:
            print(f"Your current score is: {score}")
            print("Quiting now")
            break

        if operation=='-':
            answer=number1-number2 
        elif operation=='+':
            answer=number1+number2
        elif operation=='*':
            answer=number1*number2
        else:
            answer=number1/number2
            
        print(f"What is: {number1} {operation} {number2}?:")
        trial=input("Enter answer: ").strip()
        while not trial.isdigit():
            print("Answer should be a number")
            trial=input("Enter answer: ").strip()
        if int(trial)==answer:
            print("Correct answer")
            score+=1
            print(f"Your current score is: {score}")
        else:
            print("Invalid answer .")
            print(f"The correct answer is: {answer}")
            print(f"Your current score is: {score}")
    
def main():
    while True:
        print("Please choose an option to proceed")
        print("1. Perform calculations")
        print("2. Exit")
        option=input("Selected option(1,2): ").strip()
        while option not in ['1','2']:
            print("Invalid option. Please try again ")
            option=input("Selected option(1,2): ").strip()
        if option=='1':
            Checker()
        else:
            print("leaving the game ,byeee")
            break

main()

