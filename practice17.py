import streamlit as st
import datetime


if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title("💰 Expense Tracker")

menu = st.radio(
    "Choose an option:",
    ["Add expense", "Category total", "Monthly total"]
)


if menu == "Add expense":
    st.subheader("➕ Add Expense")

    date = st.date_input(
        "Date",
        value=datetime.date.today()
    )

    category = st.text_input("Category")
    amount = st.number_input("Amount", min_value=0.0, step=0.01)

    if st.button("Add expense"):
        st.session_state.expenses.append(
            [str(date), category, amount]
        )
        st.success("Expense added!")


elif menu == "Category total":
    st.subheader("📊 Category-wise Total")

    totals = {}
    for e in st.session_state.expenses:
        totals[e[1]] = totals.get(e[1], 0) + e[2]

    if totals:
        for cat, total in totals.items():
            st.write(f"**{cat}** : {total}")
    else:
        st.info("No expenses added yet.")


elif menu == "Monthly total":
    st.subheader("📅 Monthly Total")

    month = st.text_input("Enter month (YYYY-MM)")

    if st.button("Calculate"):
        total = 0
        for e in st.session_state.expenses:
            if e[0].startswith(month):
                total += e[2]

        st.success(f"Monthly total: {total}")
