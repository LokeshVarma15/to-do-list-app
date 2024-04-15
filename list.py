# Define a list to store tasks
tasks = []

def add_task():
  """Adds a new task to the to-do list."""
  task = input("Enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

def list_tasks():
  """Prints all tasks in the to-do list."""
  if not tasks:
    print("There are no tasks in the list.")
    return
  
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

def remove_task():
  """Removes a task from the to-do list."""
  if not tasks:
    print("There are no tasks to remove.")
    return
  
  list_tasks()
  index = int(input("Enter the number of the task to remove: ")) - 1
  if index < 0 or index >= len(tasks):
    print("Invalid task number.")
    return
  
  task = tasks.pop(index)
  print(f"Task '{task}' removed from the list.")

def main():
  """Main function to handle user interaction."""
  print("Welcome to your to-do list!")
  while True:
    print("\nMenu:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      add_task()
    elif choice == '2':
      list_tasks()
    elif choice == '3':
      remove_task()
    elif choice == '4':
      print("Exiting the to-do list app.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
