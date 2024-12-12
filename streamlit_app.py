import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("WorkScope")
st.write("Welcome to WorkScope! This is a simple web app that allows you to track the earnings and data of your employees.")
st.write("Check this example below:")

# Load data
data = pd.read_csv("employees.csv")

# Display data table
st.dataframe(data)

# Separation of the sections
st.markdown("---")

# Display data graph options
st.title("Graph personalization")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    bar_color = st.color_picker("Choose a color for the bars", "#3475B3")
with col2:
    show_names = st.toggle("Show names on the axis")
with col3:
    show_salaries = st.toggle("Show salaries on the graph")
with col4:
    sorted_data = st.selectbox("Sort data by", ["Name", "Salary"])
with col5:
    sort_order = st.selectbox("Order", ["Ascending", "Descending"])

ascending = True if sort_order == "Ascending" else False
if sorted_data == "Salary":
    data = data.sort_values("salary", ascending=ascending)
else:
    data = data.sort_values("full name", ascending=ascending)


# Create graph
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(data["full name"], data["salary"], color=bar_color)

# Set x-axis limit
ax.set_xlim(0, 4500)

# Add or Remove texts on the graph
if show_names:
    ax.set_yticks(range(len(data["full name"])))
    ax.set_yticklabels(data["full name"], fontsize=12)
else:
    ax.set_yticks([])

if show_salaries:
    for bar in bars:
        ax.text(
            bar.get_width() + 10, bar.get_y() + bar.get_height() / 2, 
            f"{int(bar.get_width())}€", va="center", fontsize=12, color="black"
        )

# Set labels
ax.set_ylabel("Employees", fontsize=14, fontweight="bold", labelpad=10)
ax.set_xlabel("Salaries", fontsize=14, fontweight="bold", labelpad=10)
ax.set_title("Salaries of the employees", fontsize=16, fontweight="bold")

# Display graph
st.pyplot(fig)

st.markdown("---")

st.title("Upload your own data (CSV file)")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        bar_color = st.color_picker("Choose a color for the bars", "#3475B3", key="bar_color_file_uploaded")
    with col2:
        show_names = st.toggle("Show names on the axis", key="show_names_file_uploaded")
    with col3:
        show_salaries = st.toggle("Show salaries on the graph", key="show_salaries_file_uploaded")
    with col4:
        sorted_data = st.selectbox("Sort data by", ["Name", "Salary"], key="sorted_data_file_uploaded")
    with col5:
        sort_order = st.selectbox("Order", ["Ascending", "Descending"], key="sort_order_file_uploaded")

    ascending = True if sort_order == "Ascending" else False
    if sorted_data == "Salary":
        data = data.sort_values(by="salary", ascending=ascending)
    else:
        data = data.sort_values(by="full name", ascending=ascending)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data["full name"], data["salary"], color=bar_color)

    ax.set_xlim(0, 4500)

    if show_names:
        ax.set_yticks(range(len(data["full name"])))
        ax.set_yticklabels(data["full name"], fontsize=12)
    else:
        ax.set_yticks([])

    if show_salaries:
        for bar in bars:
            ax.text(
                bar.get_width() + 10, bar.get_y() + bar.get_height() / 2, 
                f"{int(bar.get_width())}€", va="center", fontsize=12, color="black"
            )

    ax.set_ylabel("Employees", fontsize=14, fontweight="bold", labelpad=10)
    ax.set_xlabel("Salaries", fontsize=14, fontweight="bold", labelpad=10)
    ax.set_title("Salaries of the employees", fontsize=16, fontweight="bold")

    st.pyplot(fig)
else:
    st.warning("**The CSV needs to have the same structure as the table above.**")