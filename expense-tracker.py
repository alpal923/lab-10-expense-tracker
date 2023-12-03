import streamlit as st
import pandas as pd
import plotly.express as px

# Load existing expenses data if available
expenses = pd.DataFrame(columns=["Date", "Category", "Amount", "Comment"])

# Sidebar for user input
st.sidebar.header("Expense Tracker")

date = st.sidebar.date_input("Date", pd.Timestamp.now())
category = st.sidebar.selectbox("Category", ["Food", "Transportation", "Entertainment", "Others"])
amount = st.sidebar.number_input("Amount ($)", value=0.0, step=1.0)
comment = st.sidebar.text_input("Comment", "")

if st.sidebar.button("Add Expense"):
    new_expense = {"Date": date, "Category": category, "Amount": amount, "Comment": comment}
    expenses = expenses.append(new_expense, ignore_index=True)

# Display expenses table
st.header("Expenses")
st.dataframe(expenses)

# Interactive chart to show expenses by category
category_expenses = expenses.groupby("Category")["Amount"].sum().reset_index()
fig = px.pie(category_expenses, values="Amount", names="Category", title="Expense Distribution")
st.plotly_chart(fig)

# Total expenses
total_expenses = expenses["Amount"].sum()
st.sidebar.subheader("Total Expenses")
st.sidebar.write(f"${total_expenses:.2f}")

# Optional: Save the expenses data to a CSV file
# expenses.to_csv("expenses.csv", index=False)
