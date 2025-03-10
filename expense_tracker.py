import streamlit as st
import pandas as pd
import random

st.title("Expense Tracker App")

# Initialize session state for expense storage
if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

# User Inputs for Expense
expense_name = st.text_input("Expense Name:")
expense_amount = st.number_input("Amount:", min_value=0.0, format="%.2f")
expense_category = st.selectbox("Category:", ["Food", "Travel", "Shopping", "Bills", "Other"])

# Add Expense Button
if st.button("Add Expense"):
    if expense_name and expense_amount > 0:
        st.session_state["expenses"].append({"Name": expense_name, "Amount": expense_amount, "Category": expense_category})
        st.success("✅ Expense Added!")
    else:
        st.error("⚠ Please enter valid details!")

# Convert to DataFrame
if st.session_state["expenses"]:
    df = pd.DataFrame(st.session_state["expenses"])
    st.subheader("📊 Expense Summary")
    st.dataframe(df)

# Calculate Total Expense
    total_expense = df["Amount"].sum()
    st.subheader(f"💵 Total Spent: ₹{total_expense:.2f}")

# Filter Expenses by Category
    selected_category = st.selectbox("🔍 Filter by Category:", ["All"] + list(df["Category"].unique()))
    if selected_category != "All":
        df = df[df["Category"] == selected_category]
        st.dataframe(df)