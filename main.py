
todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index}--{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            existing_todo = todos[number]
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Invalid input")







print("Babay!")