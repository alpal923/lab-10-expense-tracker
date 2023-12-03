import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize an empty list to store expenses
expenses = []

# Sidebar for user input
st.sidebar.header("Expense Tracker")

date = st.sidebar.date_input("Date", pd.Timestamp.now())
category = st.sidebar.selectbox("Category", ["Food", "Transportation", "Entertainment", "Others"])
amount = st.sidebar.number_input("Amount ($)", value=0.0, step=1.0)
comment = st.sidebar.text_input("Comment", "")

if st.sidebar.button("Add Expense"):
    new_expense = {"Date": date, "Category": category, "Amount": amount, "Comment": comment}
    expenses.append(new_expense)

# Display expenses table as a DataFrame
st.header("Expenses")
expenses_df = pd.DataFrame(expenses)
st.dataframe(expenses_df)

# Check if "Amount" column exists before calculating the total expenses
if "Amount" in expenses_df.columns:
    # Total expenses
    total_expenses = expenses_df["Amount"].sum()
    st.sidebar.subheader("Total Expenses")
    st.sidebar.write(f"${total_expenses:.2f}")

# Check if "Category" column exists before grouping
if "Category" in expenses_df.columns:
    # Interactive chart to show expenses by category
    category_expenses = expenses_df.groupby("Category")["Amount"].sum().reset_index()
    fig = px.pie(category_expenses, values="Amount", names="Category", title="Expense Distribution")
    st.plotly_chart(fig)
