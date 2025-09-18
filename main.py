
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            # file = open("todos.txt", "r")
            # todos = file.readlines()
            # file.close()

            # контекстний мененджер
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            # file=open("todos.txt",'w')
            # file.writelines(todos)
            # file.close()

            with open("todos.txt",'w') as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # 1-й спосіб
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # 2-й спосіб
            # new_todos = [item.strip('\n') for item in todos]


            # print(todos)
            for index, item in enumerate(todos):
                row = f"{index+1}--{item.strip('\n')}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            # print('Here is todos existing', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # print('Will be todos', todos)

            with open("todos.txt",'w') as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            completed_todo = todos.pop(number - 1)

            with open("todos.txt",'w') as file:
                file.writelines(todos)

            message = f"\tТудушка \"{completed_todo.strip('\n')}\" була успішно виконана!"
            print(message)
        case "exit":
            break
        case _:
            print("Invalid input")







print("Babay!")