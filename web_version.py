import streamlit as st
import functions as f


tasks = f.get_tasks()


def add_task():
    task = st.session_state["new_task"]
    tasks.append(task)
    f.write_tasks(tasks)


st.title('Python Web App')
st.subheader("Increase your productivity!")


for task in tasks:
    st.checkbox(task)

st.text_input(label=' ', placeholder='Enter a task',
              key='new_task', on_change=add_task)

st.session_state