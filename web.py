import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My todo App")
st.subheader("This is my todo app.")
st.write("Цей додаток для покращення власної продуктивності")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    print('checkbox',checkbox)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add todo",
              label_visibility='hidden',
              placeholder="Add new todo ...",
              on_change=add_todo,
              key='new_todo')


print('Hello')

st.session_state