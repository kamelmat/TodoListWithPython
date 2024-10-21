"""
Todo App

This is a Todo module implementation for CLI in Python. 

Usage:
- Run the script to start the ToDo App.
- Follow the on screen instructions to manage your todo list and tasks

Actions:
    add - Adds a new task to the todo list
    delete - deletes a task from the todo list
    list - List all tasks in the todo list

"""


tasks = []

def add_task():
    """
    Adds a new task to the todo list 
    """

    task = input("Enter a new task: ")
    tasks.append(task)
    print("\nTask added succesfully")

def view_tasks():
    """
    View tasks on the todo list 
    """
    if len(tasks) == 0:
        print("\nNo tasks in your Todo List")
    else:
        print(f"\nYou have {len(tasks)} tasks in your Todo List")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task():
    """
    deletes a task from the to the todo list 
    """
    if len(tasks) == 0:
        print("\nNo Tasks left to delete")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice = int(input("\nEnter the task number to delete: "))
        if 0 < choice <= len(tasks):
            del tasks[choice -1]
            print("\nTask deleted succsefully")
        else:
            print("\nPlease enter a valid task number")

def main():
    """
    Runs the command line todo list application
    """
    while True:
        print("\n===== To-Do List Aplication ====")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Quit")

        choice = int(input("\nPlease enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do List App")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()



