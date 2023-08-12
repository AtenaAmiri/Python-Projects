while True:
    user_action = input("Type add,show,edit,delete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo : ") + "\n"


            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

          
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
          
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todos = []

            for index, item in enumerate(todos):
                item = item.title().strip("\n")
                row = f"{index + 1} - {item}"
                print(row)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "delete":
            number = int(input("Number of the todo to delete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Hey, you entered an unknown command ")

print("Bye")
