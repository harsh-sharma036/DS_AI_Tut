import streamlit as st

st.title("Advance Calculator")

num1 = st.number_input("enter first number: ")

num2 = st.number_input("enter second number: ")

op = st.radio("chooose operation", ["addition", "substraction", "multiplication", "division", "modulo", "power"])

if(op == "addition"):
    result = num1+num2
elif(op == "substraction"):
    result = num1 -num2
elif(op == "multiplication"):
    result = num1*num2
elif(op == "division"):
    if(num2 != 0):
        result = num1/num2
    else:
        print("error")
elif(op == "modulo"):
    if(num1 != 0):
        result = num1 % num2
    else:
        print("error by modulo")
elif(op == "power"):
    result = num1**num2

st.write("### Result : ", result)




