import csv
import os
def input_marks(subject):
    value=input(f"Enter {subject} marks: ").strip()
    while True:
        if not value.isdigit():
            print(f"{subject} marks should be numerical")
        elif not (0<=int(value) <= 100):
            print(f"{subject} marks should be within 0-100")
        else:
                break
        value = input(f"Enter {subject} marks again: ").strip() 
    return int(value)

def calculate_grade(grade_points):
    if grade_points>=80:
        return 'A'
    elif 65<=grade_points<=79:
        return 'B'
    elif 55<=grade_points<=64:
        return 'C'
    elif 45<=grade_points<=54:
        return 'D'
    else:
        return 'E'

def get_remarks(grade):
    remarks = {
        "A": "Excellent work! Keep it up! ⭐",
        "B": "Good performance. 👍",
        "C": "Fair effort. You can do better. 🙂",
        "D": "Below average. Work harder. 💪",
        "E": "Needs serious improvement. 📚"
    }
    return remarks[grade]

def id_exists(student_id):
    if not os.path.exists("grades.csv"):
        return False
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  
        for row in reader:
            if row and row[0] == student_id:  
                return True
    return False

def save_to_csv(student_id, name, marks, total, average, grade):
    header = ["ID", "Name"] + list(marks.keys()) + ["Total", "Average", "Grade"]

    file_exists = os.path.exists("grades.csv")
    write_header = not file_exists or os.path.getsize("grades.csv") == 0

    with open("grades.csv","a",newline="") as file:
        writer=csv.writer(file)
        if write_header:
            writer.writerow(header)
        writer.writerow([student_id, name] + list(marks.values()) + [total, average, grade])

def grader():
    print("\n----------- STUDENT GRADING SYSTEM -----------\n")

    student_id = input("Enter student ID: ").strip()
    while id_exists(student_id):
        print("This ID already exists! Each student must have a unique ID.")
        student_id = input("Enter a different student ID: ").strip()

    name=input("Enter student name: ").capitalize().strip()
    subjects=[
        'Maths',
        'English',
        'Kiswahili',
        'CRE',
        'Geography',
        'Biology',
        'Chemistry',
        'Physics'
        ]
    marks={}

    for subject in subjects:
        marks[subject]=input_marks(subject)

    total_score=sum(marks.values()) 
    grade_points=round(total_score/len(subjects),2) 
    grade=calculate_grade(grade_points)

    best=max(marks,key=marks.get)
    worst=min(marks,key=marks.get)

    remarks=get_remarks(grade)
   
   

    print("\n--- Student Report Card ---")
    print(f"ID: {student_id}")
    print(f"Name:, {name}")
    for sub, score in marks.items():
        print(f"{sub}: {score}")
    
    print(f"Total Marks: {total_score}")
    print(f"Average Score: {grade_points}")
    print(f"Grade: {grade}")
    print(f"Remarks: {remarks}")
    print(f"Strongest Subject: {best} ({marks[best]})")
    print(f"Weakest Subject: {worst} ({marks[worst]})")

    save_to_csv(student_id,name, marks, total_score, grade_points, grade)
    print("\nRecord saved to grades.csv ✅")

    print("\n-----------------------------------")

                       
def main():
    while True:
        grader()
        another = input("\nDo you want to enter another student? (yes/no): ").lower()
        if another != "yes":
            print("\nExiting program... Goodbye! 👋")
            break

main()       