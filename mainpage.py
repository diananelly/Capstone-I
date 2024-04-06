import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Crime Data Visualization Project")
st.subheader("Alejandro Rodriguez, Christopher Franco")

# Select a year to explore
data_year = st.selectbox("Select a year you would like to explore", options=["2021", "2022"])

if data_year == "2021":
    # Good for options for the user
    display = st.selectbox("Select the crime data you would like to look through from the selected year",
                           options=["Personal Offenses", "Property Offenses", "Societal Offenses"])



# Pie Chart Implementation-------------------------------------------------------------

    st.subheader("Total Personal Offenses throughout the Country")
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig = go.Figure(data=[go.Pie(labels=['California', 'Texas', 'Florida', 'New York'],
                                 values=[4500, 2500, 1053, 500])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    # streamlit display
    st.plotly_chart(fig)

    #End of PieChart---------------------------------------------------------------------------

    if display == "Personal Offenses":

        st.header("Personal Offenses Committed Data")

        # The modified Tableau Public link for embedding
        tableau_url = "https://public.tableau.com/views/BarChartsbyagency2022/Sheet1?:embed=y&:display_count=yes&:showVizHome=no"

        # Embedding the Tableau visualization in an iframe
        iframe = f'<iframe src="{tableau_url}" width="100%" height="525"></iframe>'
        st.markdown(iframe, unsafe_allow_html=True)

        st.write("Displaying offenses committed data for 2021.")
        # st.write super useful
    elif display == "Weapons Used":

        st.write("Displaying weapons used data for 2021.")
        # We should add some code here for the weapons used.
else:
    # 2022 INFO GOES BELOW--------------

    display = st.selectbox("Select the crime data you would like to look through from the selected year",
                           options=["Personal Offenses", "Property Offenses", "Societal Offenses"])

    ##Pie Chart Start-----

    st.subheader("Total Personal Offenses throughout the Country")
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig = go.Figure(data=[go.Pie(labels=['California', 'Texas', 'Florida', 'New York'],
                                 values=[3000, 1500, 2053, 500])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    st.plotly_chart(fig)

##Pie Chart End------

    st.write(f"Raw Bar Graph Data for {data_year} is not available yet. Please select another year.")


