def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a Task")
    print("2. Mark a Task as Completed")
    print("3. Delete a Task")
    print("4. Exit")

def view_tasks(tasks):
    print("*" * 70)
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. {task['title']} - {status}")
    print("\n")
    print("*" * 70)

def add_task(tasks):
    title = input("\nEnter the task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")
    print("\n")
    view_tasks(tasks)

def mark_task_completed(tasks):
    if tasks:
        try:
            task_no = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]['completed'] = True
                print(f"Task '{tasks[task_no - 1]['title']}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        print("\n")
        view_tasks(tasks)
    else:
        print("\n")
        print("*" * 70)
        print("\nNo tasks available currently.\nAdd a task to get started.\n")
        print("*" * 70)

def delete_task(tasks):
    if tasks:
        try:
            task_no = int(input("\nEnter the task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed_task = tasks.pop(task_no - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        print("\n")
        view_tasks(tasks)
    else:
        print("\n")
        print("*" * 70)
        print("\nNo tasks available currently.\nAdd a task to get started.\n")
        print("*" * 70)

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_completed(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nExiting To-Do List. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()