def get_todos(filepath="data/todos.txt"):
    with open(filepath, "r") as f:
        todos_local = f.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.lower().startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos("data/todos.txt")

        todos.append(todo)

        with open("data/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.lower().startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            row = f"{index+1}--{item.strip('\n')}"
            print(row)
    elif user_action.lower().startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open("data/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Ваша команда не зовсім зрозуміла")
            continue


    elif user_action.lower().startswith('complete'):
        number = int(user_action[9:])

        todos = get_todos()

        completed_todo = todos.pop(number - 1)

        with open("data/todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"\tТудушка \"{completed_todo.strip('\n')}\" була успішно виконана!"
        print(message)
    elif user_action.lower().startswith('exit'):
        break
    else:
        print('invalid input')

    print( ' Успішне виконня команди')







print("Babay!")