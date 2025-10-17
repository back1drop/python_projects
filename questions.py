import random
import time
questions=[
    {
    "question": " Which is the smallest continent?",
    "A": "Asia",
    "B": "Europe",
    "C": "Australia",
    "D": "Africa",
    "correctAnswer": "Australia",
    },
    {
    "question": " Which planet is known as the Red Planet?",
    "A": "Mars",
    "B": "Venus",
    "C": "Jupiter",
    "D": "Saturn",
    "correctAnswer": "Mars",
    },
    {
    "question": " What is the capital of Japan?",
    "A": "Beijing",
    "B": "Tokyo",
    "C": "Seoul",
    "D": "Bangkok",
    "correctAnswer": "Tokyo",
    },
    {
    "question": "Which gas do plants absorb?",
    "A": "Oxygen",
    "B": "Nitrogen",
    "C": "Carbon Dioxide",
    "D": "Hydrogen",
    "correctAnswer": "Carbon Dioxide",
    },
]



def loader():
    random.shuffle(questions)
    score=0

    print("======  QUIZ STARTEDDDD  =======")

    start_time=time.time()
    

    for i,quiz in enumerate(questions,start=1) :
        print(f"{i}. {quiz['question']}")
        print(f"A. {quiz['A']}")
        print(f"B. {quiz['B']}")
        print(f"C. {quiz['C']}")
        print(f"D. {quiz['D']}")

        while True:
            trial=input("Please enter your choice: ").upper().strip()
            if trial not in['A','B','C','D']:
                print("Invalid option!")
            else:
                break

        if quiz[trial]==quiz['correctAnswer']:
            print("Correct")
            score+=1   
        else:
            print("Wronggg")
            print(f"The correct answer is {quiz['correctAnswer']}")
        input("Press Enter to continue...\n")
    
    end_time=time.time()
    elapsed_time=round(end_time-start_time,2)
        
    print("======  Quiz complete!!  ======")
    print(f"You scored {score}/{len(questions)}")
    percent_score=(score/len(questions))*100
    print(f"Percentage: {percent_score:.2f}%")
    print(f"Time taken: {elapsed_time} seconds")


    if percent_score >=80:
        print("🤩Excellent work")
    elif percent_score>=50:
        print("👍🏾Good job")
    else:
        print("💪🏾Try again next time")

    with open('scores.txt','a') as file:
        file.write(f"Score: {score}/{len(questions)}  ({percent_score:.2f}%) | Time: {elapsed_time}s\n")

    replay=input("Would you like to redo the questions(yes/no): ").lower().strip()
    if replay=='yes':
        loader()
    else:
        print("\nThanks for playing")



loader()
