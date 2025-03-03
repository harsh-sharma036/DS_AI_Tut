# import streamlit as st

# st.title("BMI Calculator")

# w = st.number_input("enter your weight (kg): ", min_value=1.0, step=0.1)
# h = st.number_input("enter your height (cm): ", min_value=1.0, step=1)

# h_m = h/100
# h_m = h_m**2

# if (w > 0 and h > 0):
#     bmi = w/h_m

# st.write(f"### Your BMI: {bmi: 0.2f}")

# if(bmi < 18.5):
#     st.warning("you are underweight")
# elif(bmi >= 18.5 and bmi<24.9):
#     st.success("you have a normal weight")
# elif(bmi >= 25 and bmi < 29.9):
#     st.warning("you are overweight")
# elif(bmi>30 and bmi<70):
#     st.error("You have to work hard")
# else:
#     st.error("please enter valid parameters")


    




import streamlit as st  # Importing Streamlit for web app development

# Displaying the title of the application
st.title("BMI Calculator")

# Taking user input for weight in kilograms
# min_value=1.0 ensures that weight cannot be zero or negative
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)

# Taking user input for height in centimeters
# min_value=1.0 ensures that height cannot be zero or negative
height_cm = st.number_input("Enter your height (cm):", min_value=1.0, step=1.0)

# Converting height from centimeters to meters for correct BMI calculation
height_m = height_cm / 100  

# Checking if valid inputs are provided
if weight > 0 and height_m > 0:
    # BMI calculation using the formula: weight (kg) / (height (m) ** 2)
    bmi = weight / (height_m ** 2)

    # Displaying the calculated BMI with 2 decimal places
    st.write(f"### Your BMI: {bmi:.2f}")

    # BMI category classification
    if bmi < 18.5:
        st.warning("You are *Underweight*. Consider a balanced diet and strength training for better health.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a *Normal weight*. Keep maintaining a healthy lifestyle!")
    elif 25 <= bmi < 29.9:
        st.warning("You are *Overweight*. Consider regular exercise and a nutritious diet for better fitness.")
    else:
        st.error("You are *Obese*. It's recommended to consult a healthcare professional for guidance.")
else:
    # Error message if weight or height values are invalid
    st.error("⚠ Please enter valid weight and height values!")