print("Hello welcome to my to-do list app 👾")

import json
import os

task=[]

def load_tasks():
    """Load saved tasks from JSON file"""
    global task
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            task = json.load(f)


def save_tasks():
    """Save tasks to JSON file"""
    with open("tasks.json", "w") as f:
        json.dump(task, f, indent=4)


def view_tasks():
    if not task:
        print("No tasks found")
    else:
        print("\nYour tasks:")
        for i, t in enumerate(task,start=1):
            print(f'{i}. {t['title']} [{t['status']}]')
        print()

            

def add_task():
    task_name=input("Please enter task name: ").strip()
    new_task={
        'title':task_name, 'status':'❌'
    }
    task.append(new_task)
    save_tasks()
    print("task has been added successfully!!!")

    


def mark_task():
    view_tasks()
    if not task:
        return
    
    task_no=int(input("Enter the task number you wish to mark as done"))
    if 0 < task_no <= len(task) :
        task_check=task[task_no - 1]
        task_check["done"]='✅'
        save_tasks()
        print("Task marked as done")
    else:
        print("Task does not exist")

def delete_task():
    view_tasks()
    if not task:
        return
    task_no=int(input("Enter the number of the task you wish to delete: "))
    if 0 < task_no <= len(task) :
        removed=task.pop(task_no - 1)
        save_tasks()
        print(f"🗑️ '{removed['title']}' removed successfully!")    
    else:
        print("⚠️ Task does not exist.")

def editor():
    view_tasks()
    if not task:
        return
    task_no=int(input("Enter the number of the task you wish to edit: "))
    if 0 < task_no <= len(task) :
        task_check=task[task_no - 1]
        location=input("Do you wish to edit the title or the status of the task (title or task): ").lower().strip()
        if location == 'title':
            new_name=input("Enter new title: ").lower().strip()
            task_check['title']=new_name
        elif location == 'status':
            new_status=input("Do you wish to mark it as done or not done(✅ or ❌) ").lower().strip()
            if new_status in ["✅", "❌"]:
                task_check['status']=new_status
               
            else:
                print("Invalid response")
        else:
            print("⚠️ Invalid choice.")
            return
        save_tasks()
        print("✏️ Task updated successfully!")
    else:
        print("Task does not exist")

def search():  
    keyword = input("Enter a keyword to search for: ").lower().strip()
    results = [t for t in task if keyword in t["title"].lower()]
    if results:
        print(f"\n🔍 Found {len(results)} matching task(s):")
        for t in results:
            print(f"- {t['title']} [{t['status']}]")
    else:
        print("No matching tasks found.")


def clear_all():
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").lower().strip()
    if confirm == "yes":
        task.clear()
        save_tasks()
        print("🧹 All tasks cleared!")
    else:
        print("Cancelled.")

load_tasks()         


while True:
    print("\n 📃Please select an option from the menu: ")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Edit a task")
    print("6. Search for a task using title")
    print("7. Clear all tasks")
    print("8. Exit")
    user_choice=input("Enter the option you wish to proceed with (1-8): ").strip()

    while user_choice not in ['1','2','3','4','5','6','7','8']:
        print("Enter a valid choice")
        user_choice=input("Enter the option you wish to proceed with (1,2,3,4,5,6,7): ").strip()

    if user_choice =='1':
        add_task()
    elif user_choice =='2':
        view_tasks()
    elif user_choice =='3':
        mark_task()
    elif user_choice =='4':
        delete_task()
    elif user_choice =='5':
        editor()
    elif user_choice =='6':
        search()
    elif user_choice == "7":
        clear_all()
    elif user_choice =='8':
        print("Closing the app now....")
        break
    else:
        print("⚠️ Invalid choice, please try again.")



