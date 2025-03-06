# import streamlit as st

# st.title("Smart Contact Book: ")

# # st.session_state()
# if("contacts" not in st.session_state):
#     st.session_state.contacts = {}

# def add_contact(name, phone):
#     if(name and phone):
#         if name in st.session_state.contacts:
#             st.warning(f"\"contact\"{name} already exits")
#         else:
#             st.session_state.contacts[name] = phone
#             st.success(f"Contact {name} added succesfully")
#     else:
#         st.error("name and phone number cannot be empty")


# def search_contact(name):
#     if name in st.session_state.contacts:
#         return f"{name}: {st.session_state.contact[name]}"
#     else:
#         return "contact not found"

# def remove_contact(name):
#     if name in st.session_state.contacts:

import streamlit as st  # Importing Streamlit to create the web application

# Setting the title of the application
st.title("📞 Smart Contact Book App")

# Initialize session state to store contacts (dictionary format)
if "contacts" not in st.session_state:
    st.session_state.contacts = {}  # Empty dictionary to store contacts

# Function to add a contact
def add_contact(name, phone):
    if name and phone:  # If-Else Condition to check for valid input
        if name in st.session_state.contacts:  # Checking if contact already exists
            st.warning(f"⚠ Contact '{name}' already exists! Try a different name.")
        else:
            st.session_state.contacts[name] = phone  # Storing name and phone number
            st.success(f"✅ Contact '{name}' added successfully!")
    else:
        st.error("❌ Name and Phone number cannot be empty!")

# Function to search for a contact
def search_contact(name):
    if name in st.session_state.contacts:  # Checking if the contact exists in the dictionary
        return f"📌 {name}: {st.session_state.contacts[name]}"  # Returning contact details
    else:
        return "❌ Contact not found!"  # If contact is not in the list

# Function to remove a contact
def remove_contact(name):
    if name in st.session_state.contacts:  # Checking if the contact exists
        del st.session_state.contacts[name]  # Deleting the contact
        st.success(f"❌ Contact '{name}' removed successfully!")
    else:
        st.error("❌ Contact does not exist!")

# User input section for adding a new contact
st.subheader("➕ Add a New Contact")
name = st.text_input("Enter Name:")  # Text input for name
phone = st.text_input("Enter Phone Number:")  # Text input for phone number
if st.button("Save Contact"):  # Button to trigger the add_contact function
    add_contact(name, phone)

# Section for searching a contact
st.subheader("🔍 Search a Contact")
search_name = st.text_input("Enter Name to Search:")  # Input field for search
if st.button("Search"):  # Button to trigger search
    result = search_contact(search_name)  # Calling the search function
    st.markdown(f"### {result}")  # Displaying the search result

# Display saved contacts using a loop
st.subheader("📋 Your Contacts")
if st.session_state.contacts:  # Checking if there are saved contacts
    for contact_name, contact_phone in st.session_state.contacts.items():  # Looping through contacts
        st.write(f"📌 {contact_name}: {contact_phone}")  # Displaying each contact

    # Section for removing a contact
    st.subheader("🗑 Remove a Contact")
    contact_to_remove = st.selectbox("Select a contact to remove:", list(st.session_state.contacts.keys()))  # Dropdown to select contact
    if st.button("Delete Contact"):  # Button to trigger delete function
        remove_contact(contact_to_remove)  # Calling remove_contact function
else:
    st.write("No contacts saved yet.")  # Display message if no contacts exist