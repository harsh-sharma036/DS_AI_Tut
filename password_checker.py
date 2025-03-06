# import re
# import streamlit as st

# st.title("Password Checker")

# def check_password_strength(password):
#     strength = 0
#     remarks = ""
#     if len(password)>= 8:
#         strength+= 1
#     if re.search(r"[A-Z]", password):
#         strength += 1
#     if re.search(r"[a-z]", password):
#         strength += 1
#     if re.search(r"\d", password):
#         strength += 1
#     if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#         strength += 1
#     if strength == 5:
#         remarks = "strong"
#         colour = "green"
#     elif strength>= 3:
#         remrks = "moderate"
#         colour = "yellow"
#     else:
#         remarks = "weak"
#         colour = "red"
    
#     return strength, remarks, colour

# password = st.text_input("enter the password: ", type = "password")
# if password:
#     strength, remarks, colour = check_password_strength(password)
#     # st.markdown(f"### Strength:  < span style ='colour: {colour}; font size : 20px;'>{remarks}</span>", unsafe_allow_html = True)
#     # Display password strength with dynamic color styling
#     st.markdown(f"### Strength: <span style='colour:{colour}; font-size:20px;'>{remarks}</span>", unsafe_allow_html=True)
#     st.subheader("how to improve your password?")
#     if strength < 5:  # If password is not strong, provide improvement tips
#         suggestions = []  # Initialize empty list for suggestions
        
#         # Suggest increasing password length if it's less than 8 characters
#         if len(password) < 8:
#             suggestions.append("Increase password length (at least 8 characters).")
        
#         # Suggest adding an uppercase letter if missing
#         if not re.search(r"[A-Z]", password):
#             suggestions.append("Add at least one uppercase letter.")
        
#         # Suggest adding a lowercase letter if missing
#         if not re.search(r"[a-z]", password):
#             suggestions.append("Add at least one lowercase letter.")
        
#         # Suggest adding a number if missing
#         if not re.search(r"\d", password):
#             suggestions.append("Include at least one number.")
        
#         # Suggest adding a special character if missing
#         if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
#             suggestions.append("Use at least one special character (!@#$%^&* etc.).")
        
#         # Display all suggestions as a checklist
#         for suggestion in suggestions:
#             st.write(f"✅ {suggestion}")

import streamlit as st  # Importing Streamlit for building the web app
import re  # Importing the regular expression module for pattern matching

# Setting the title of the web application
st.title("🔐 Password Strength Checker")

# Function to check the strength of the password
def check_password_strength(password):
    strength = 0  # Initialize strength score
    remarks = ""  # Variable to store password strength remarks
    
    # Check for password length (should be at least 8 characters)
    if len(password) >= 8:
        strength += 1  # Increase strength if condition met
    
    # Check for at least one uppercase letter (A-Z)
    if re.search(r"[A-Z]", password):
        strength += 1
    
    # Check for at least one lowercase letter (a-z)
    if re.search(r"[a-z]", password):
        strength += 1
    
    # Check for at least one numeric digit (0-9)
    if re.search(r"\d", password):
        strength += 1
    
    # Check for at least one special character (!@#$%^&* etc.)
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Assign remarks and color based on strength score
    if strength == 5:
        remarks = "Strong 💪"  # Password is strong
        color = "green"  # Green color for strong password
    elif strength >= 3:
        remarks = "Moderate 🙂"  # Password is moderate
        color = "orange"  # Orange color for moderate password
    else:
        remarks = "Weak ❌"  # Password is weak
        color = "red"  # Red color for weak password
    
    return strength, remarks, color  # Returning the strength score, remarks, and color

# Taking user input for password (input field will mask characters)
password = st.text_input("Enter a password:", type="password")

# If the user enters a password, evaluate its strength
if password:
    strength, remarks, color = check_password_strength(password)  # Call function to check strength
    
    # Display password strength with dynamic color styling
    st.markdown(f"### Strength: <span style='color:{color}; font-size:20px;'>{remarks}</span>", unsafe_allow_html=True)
    
    # Provide suggestions for improvement if password is not strong
    st.subheader("🔹 How to Improve Your Password?")
    
    if strength < 5:  # If password is not strong, provide improvement tips
        suggestions = []  # Initialize empty list for suggestions
        
        # Suggest increasing password length if it's less than 8 characters
        if len(password) < 8:
            suggestions.append("Increase password length (at least 8 characters).")
        
        # Suggest adding an uppercase letter if missing
        if not re.search(r"[A-Z]", password):
            suggestions.append("Add at least one uppercase letter.")
        
        # Suggest adding a lowercase letter if missing
        if not re.search(r"[a-z]", password):
            suggestions.append("Add at least one lowercase letter.")
        
        # Suggest adding a number if missing
        if not re.search(r"\d", password):
            suggestions.append("Include at least one number.")
        
        # Suggest adding a special character if missing
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            suggestions.append("Use at least one special character (!@#$%^&* etc.).")
        
        # Display all suggestions as a checklist
        for suggestion in suggestions:
            st.write(f"✅ {suggestion}")