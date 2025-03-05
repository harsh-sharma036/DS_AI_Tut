# My code
import streamlit as st

st.title("TO-DO LIST")

if "tasks" not in st.session_state:
    st.session_state.tasks = []  # creating an empty list for storing tasks


def add_task():
    task = st.text_input("Enter a new task")
    if st.button("add task"):
        if task:
            st.session_state.tasks.append(task)
            st.rerun()


def remove_task():
    if st.session_state.tasks:
        task_to_remove = st.selectbox("select task to remove: ", st.session_state.tasks)
        if st.button("remove task"):
            if task_to_remove in st.session_state.tasks:
                st.session_state.tasks.remove(task_to_remove)
                st.rerun()


st.subheader("Your to-do list: ")

for task in st.session_state.tasks:
    st.write(f"✅{task}")

st.sidebar.subheader("manage tasks")
add_task()
if st.session_state.tasks:
    remove_task()



# ## referenced code
# import streamlit as st  # Importing Streamlit for building the web app

# # Setting the title of the web application
# st.title("📝 Simple To-Do List")

# # Initialize session state to store tasks (to persist data across reruns)
# if "tasks" not in st.session_state:
#     st.session_state.tasks = []  # Create an empty list to store tasks

# # Function to add a new task
# def add_task():
#     task = st.text_input("Enter a new task:")  # User input field for task
#     if st.button("Add Task"):  # Button to add the task
#         if task:  # Ensure the task is not empty
#             st.session_state.tasks.append(task)  # Add task to session state list
#             st.rerun()  # Rerun the app to update the UI

# # Function to remove an existing task
# def remove_task():
#     if st.session_state.tasks:  # Ensure there are tasks to remove
#         task_to_remove = st.selectbox("Select a task to remove:", st.session_state.tasks)  # Dropdown to select task
#         if st.button("Remove Task"):  # Button to remove selected task
#             if task_to_remove in st.session_state.tasks:  # Ensure the task is in the list
#                 st.session_state.tasks.remove(task_to_remove)  # Remove selected task
#                 st.rerun()  # Rerun the app to update the UI

# # Display the list of tasks
# st.subheader("Your To-Do List:")
# for task in st.session_state.tasks:  # Loop through stored tasks
#     st.write(f"✅ {task}")  # Display each task with a checkmark

# # User Interface for task management in the sidebar
# st.sidebar.subheader("Manage Tasks")
# add_task()  # Call function to add tasks
# if st.session_state.tasks:  # Display remove option only if tasks exist
#     remove_task()  # Call function to remove tasks
