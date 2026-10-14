def display_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Update/Mark Task as Done")
    print("4. Delete a Task")
    print("5. Exit")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if not tasks:
                print("\nYour to-do list is empty.")
            else:
                print("\n--- YOUR TASKS ---")
                for idx, task in enumerate(tasks, start=1):
                    status = "Done" if task['completed'] else "Pending"
                    print(f"{idx}. {task['title']} [{status}]")

        elif choice == '2':
            title = input("Enter the task description: ").strip()
            if title:
                tasks.append({'title': title, 'completed': False})
                print(f"Task '{title}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == '3':
            if not tasks:
                print("\nNo tasks available to update.")
                continue
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    print(f"Task {task_num} marked as Done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("\nNo tasks available to delete.")
                continue
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed['title']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
