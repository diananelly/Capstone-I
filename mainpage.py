import streamlit as st
import pandas as pd
import plotly.express as px

# This loads the xlsx files we want to display.
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
    # Good for options for the user
    display = st.selectbox("Select the data you would like to see from the year", options=["Offenses Committed", "Weapons Used"])
    if display == "Offenses Committed":
    
        st.write("Displaying offenses committed data for 2021.")
        # st.write super useful
    elif display == "Weapons Used":
        
        st.write("Displaying weapons used data for 2021.")
        #We should add some code here for the weapons used.
else:
    # 2022 can go here
    st.write(f"Data for {data_year} is not available yet. Please select another year.")

# The modified Tableau Public link for embedding
tableau_url = "https://public.tableau.com/views/BarChartsbyagency2022/Sheet1?:embed=y&:display_count=yes&:showVizHome=no"

# Embedding the Tableau visualization in an iframe
iframe = f'<iframe src="{tableau_url}" width="100%" height="525"></iframe>'
st.markdown(iframe, unsafe_allow_html=True)
