while True:
    user_action = input("Type add,show,edit,delete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        # todo = input("Enter a todo : ") + "\n"

        todo = user_action[4:]

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todos = []

        for index, item in enumerate(todos):
            item = item.title().strip("\n")
            row = f"{index + 1} - {item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "delete" in user_action:
        number = int(user_action[7:])

        with open("todos.txt", "r") as file:
            file.readlines()
            index = number - 1
        todo_to_remove = todos[index].strip("\n")

        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")

print("Bye")
