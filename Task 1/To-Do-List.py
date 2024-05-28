import os


def showTask(tasks):   ##function to show tasks
    if not tasks:
        print("No Tasks Found.")
    else:
        for i, tasks in enumerate(tasks, 1):
            print(f"{i}. {tasks}")


def addTask(tasks, newTask):    #function to add new tasks
    tasks.append(newTask)
    print("Task Added Successfully.")


def updateTask(tasks, index, updatedTask):   #function to update exixting task
    if 1 <= index <= len(tasks):
        tasks[index - 1] = updatedTask
        print("Task Updated Successfully.")
    else:
        print("Invalid Task Input. Try Again.")


def deleteTask(tasks, index):    #function to delete a tasks from the list
    if 1 <= index <= len(tasks):
        deleteTask = tasks.pop(index - 1)
        print("Task Deleted Successfully.")
    else:
        print("Invalid Task Input. Try Again.")


def loadTasks(file_pth):    #load function to load content of the file to the terminal
    task = []
    if os.path.exists(file_pth):
        with open(file_pth, "r") as file:
            task = file.read().splitlines()
    return task


def saveTask(file_pth, tasks):     #saving the tasks to a file name toDoList.txt
    with open(file_pth, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def main():
    file_pth = "toDoList.txt"
    tasks = loadTasks(file_pth)

    while True:     #loop to keep program running
        print("---Welcome to To-Do List App---")
        print("1. Add a new task.")
        print("2. Update a task.")
        print("3. View All task.")
        print("4. Delete a task.")
        print("5. Exit.")

        choice = input("Enter your choice: ")   #functionality of the program to be chosen
        if choice == "1":
            newTask = input("Enter a new task: ")
            addTask(tasks, newTask)
        elif choice == "2":
            index = int(input("Enter the index of the task to update: "))
            updatedTask = input("Enter a updated task: ")
            updateTask(tasks, index, updatedTask)
        elif choice == "3":
            showTask(tasks)
        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            deleteTask(tasks, index)
        elif choice == "5":
            saveTask(file_pth, tasks)
            print("Tasks Saved Successfully. GoodBye...")
            break
        else:
            print("Invalid Choice. Choose a Valid Input.")


if __name__ == '__main__':
    main()
