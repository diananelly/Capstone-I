import streamlit as st
import pandas as pd
import plotly.express as px

# Load the XLSX file containing offenses data
dataframe_offenses_weapons = pd.read_excel('Offenses_Involving_Weapon_Use_Off_Cat_by_Type_of_Weapon_Force_Involved_2021.xlsx')

# Streamlit app title and subheader
st.title("Welcome to the Main Page of our Project")
st.subheader("This is the first initial mock test of the data collected on GitHub.")

# Display the offenses data for the year 2021
dataframe_offenses_weapons_display = st.subheader("The following data contains offenses committed throughout the year of 2021:")
st.dataframe(dataframe_offenses_weapons)

# Select a year to explore
data_year = st.selectbox("Select a year you would like to explore", options=["2021", "2022"])

if data_year == "2021":
    # If the user selects 2021, provide additional options
    display = st.selectbox("Select the data you would like to see from the year", options=["Offenses Committed", "Weapons Used"])
    if display == "Offenses Committed":
        # You can customize this section to display specific offense-related data
        st.write("Displaying offenses committed data for 2021.")
        # Add your code here to show relevant information
    elif display == "Weapons Used":
        # You can customize this section to display specific weapon-related data
        st.write("Displaying weapons used data for 2021.")
        # Add your code here to show relevant information
else:
    # You can add similar logic for other years (e.g., 2022)
    st.write(f"Data for {data_year} is not available yet. Please select another year.")
