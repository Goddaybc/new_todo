import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    '''We use this function to get what was
    inputed and apepnd it to the todos list
    and write it there'''
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my web app.")
st.write("This app is to increase your productivity.")
for index, todo in enumerate(todos):
    # check the box with their index
    checkbox = st.checkbox(todo, key=todo)
    # when we click a check box that index
    # is removed and we write the list back
    # again into the todos.txt
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # we also remove it from the session
        # state even as we remove it from
        # the list and rerun
        del st.session_state[todo]
        st.experimental_rerun()
# text input,we add the function and key of the
# text input
st.text_input(label="", placeholder="Add new todo..."
              ,on_change=add_todo, key="new_todo")

#print("Hello")
#Session state to show the code at the bottom
#st.session_state






