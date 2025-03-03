import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title="Simple Calculator", layout="centered")

    # Title and description
    st.title("Demo Calculator")
    st.write("This is a demo calculator used to do basic calculations")

    # Create columns for better layout
    col1, col2 = st.columns(2)

    # Get user input
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)

    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    # Select operation (Fixed Dropdown)
    operation = st.selectbox(
        "Select operation",
        ["Addition", "Subtraction", "Multiplication", "Division"]
    )

    # Debugging message
    st.write(f"Debug: Selected Operation = {operation}")  # Ensures dropdown is being rendered

    # Button to trigger calculation
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Error: Cannot divide by zero"
        
        # Display result
        st.success(f"Result: {result}")

    # Refresh button to clear the UI state
    if st.button("Refresh"):
        st.rerun()

# Run the app
if __name__ == "__main__":
    main()
