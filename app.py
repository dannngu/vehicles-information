import pandas as pd
import plotly.express as px
import streamlit as st


# Read the dataset
car_data = pd.read_csv("vehicles_us.csv")

# Page configuration
st.set_page_config(page_title="Vehicles Information")
st.header('Checking Vehicle Information')


# Checkboxe's to select the type of chart
# TODO: Make Graphs checkboxes only selected one at a time.
build_histogram = st.checkbox('Create a Histogram Chart')
build_scatter = st.checkbox('Create a Scatter Chart')
build_bar = st.checkbox('Create a Bar Chart')

# Button to crete the selected chart
create_chart = st.button('Build a Graph')


# Functions to crete the Charts
def create_histogram():
    st.write('Creating a histogram for car odometer counting')
    # Create the Histrogram
    fig = px.histogram(car_data, x="odometer")
    # Show the Interactive Ploty Chart
    st.plotly_chart(fig, use_container_width=True)


def create_scatter():
    st.write(
        'Creation of a scatter plot on the relationship between odometers and price.')
    # Create the Scatterplot
    fig = px.scatter(car_data, x='odometer', y='price')
    # Show the Interactive Ploty Chart
    st.plotly_chart(fig, use_container_width=True)


def create_bar():
    st.write('Creating a line chart for price trend')
    # Create the Bar
    fig = px.bar(car_data, x='type', title='Vehicles Distribution Types')
    # Show the Interactive Plotly Chart
    st.plotly_chart(fig, use_container_width=True)


# Dictionary to emulate Swtich Case like Dart
options = {
    'histogram': create_histogram,
    'scatter': create_scatter,
    'bar': create_bar
}


# Validator of the chart selected by the user
if create_chart:
    if build_histogram:
        options["histogram"]()
    elif build_scatter:
        options["scatter"]()
    elif build_bar:
        options["bar"]()
    else:
        st.error("Please select a type of graphic")
else:
    st.dataframe(car_data)
