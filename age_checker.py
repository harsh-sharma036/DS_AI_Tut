import streamlit as st

st.title("Age Checker")

age = st.number_input("Enter your age: ", min_value=0, step=1)

def classify_age_group(age):
    if(age == 0):
        return "You are newborn baby"
    elif(age >= 1 and age<=12):
        return "Your are a child"
    elif(age >= 13 and age<=19):
        return "You're a teenager"
    elif(age >= 20 and age<=35):
        return "You're a young adult"
    elif(age>=36 and age<=59):
        return "You're a middle aged adult"
    else:
        return "You're a senior citizen"
    
if(age > 0):
    result = classify_age_group(age)
    st.markdown(f"### {result}")


