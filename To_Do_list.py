tasks = []

while True:
    print("\n===== TO-DO LIST ====")
    print("1. Add Task")
    print("2.View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your Choice(1-5):")
    
    if choice =="1":
        task = input("Enter new Task: ")
        tasks.append(task)
        print("Task added successfully")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("No Task available.")
        else:
            print("\nYour Task:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    
    elif choice == "3":
        if len(tasks)==0:
            print("No Task Updated.")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
                
            index = int(input("Enter task number to update : ")) - 1
            
            if 0<= index < len(tasks):
                new_task = input("Enter new task: ")
                tasks[index] = new_task
                print("Task Updated Successfully")
            else:
                print("Invalid Task Number.")
    elif choice == "4":
        if len(tasks) == 0:
            print("No Task deleted")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
                
                index = int(input("Enter task number to delete:")) - 1
                
                if 0<= index < len(tasks):
                    deleted = tasks.pop(index)
                    print(deleted, "Deleted Successfully!")
                
                else: 
                    print("Invalid Tasks Number.")
                    
    elif choice == "5":
        print("Thank you! Exiting To-Do List.")
        break
    
    else: 
        print("Invalid choice! Please enter a number between 1 to 5.")
     