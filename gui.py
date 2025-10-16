import functions
import FreeSimpleGUI as sg
import time


sg.theme('LightBlue6')
clock = sg.Text('',key='clock')

label = sg.Text('Type a todo')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(size=10, image_source="add1.png", tooltip="Add new todo", key='Add', mouseover_colors="LightBlue2")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 12])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My TODO App", layout=[
    [clock],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
], font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)


    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Оберіть тудушку", font=("Helvetica", 20))
        case 'todos':
            print(values['todos'][0])
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Оберіть тудушку для завершення", font=("Helvetica", 20))

        case 'Exit' :
            break

        case sg.WIN_CLOSED:
            break

    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))


window.close()

print('Babay')

