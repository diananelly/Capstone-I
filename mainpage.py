import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Crime Data Visualization Project")


# Select a year to explore
data_year = st.selectbox("Select a year you would like to explore", options=[" ","2021", "2022"])

if data_year == "2021":
    # Good for options for the user
    display = st.selectbox("Select the crime data you would like to look through from the selected year",
                           options=[" ", "Personal Offenses", "Property Offenses", "Societal Offenses"])


    if display == "Personal Offenses":


        sidebar_2021 = st.checkbox("Would You Like to See a Pie Chart of All Personal Offenses?")
        if sidebar_2021:
            st.subheader("Total Personal Offenses throughout Miami Dade County")
            tableau_url3 = "https://public.tableau.com/views/Miami-Dadecrimes2022exceptSimpleandAggravatedAssault/Miami-DadeCrimes2022?:embed=y&:display_count=yes&:showVizHome=no"
            iframe3 = f'<iframe src="{tableau_url3}" width="100%" height="525"></iframe>'
            st.markdown(iframe3, unsafe_allow_html=True)

        personal_offense_2021 = st.selectbox("Select what personal offense you would like to view",
                                        options=[" ", "Assault", "Sex Offenses", "Homicide", "Kidnapping", "Human Trafficking"])

        if personal_offense_2021 == "Assault":

            st.markdown("Assault By Location")
            tableau_url14 = "https://public.tableau.com/views/AssaultOffensesbyLocation2021/AssaultbyLocation2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe14 = f'<iframe src="{tableau_url14}" width="100%" height="525"></iframe>'
            st.markdown(iframe14, unsafe_allow_html=True)

            st.markdown("Assault By Time")
            tableau_url19 = "https://public.tableau.com/views/AssaultOffensesbyTime2021/AssaultOffensesbyTime2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe19 = f'<iframe src="{tableau_url19}" width="100%" height="525"></iframe>'
            st.markdown(iframe19, unsafe_allow_html=True)

        if personal_offense_2021 == "Sex Offenses":

            st.markdown("Sex Offenses By Location")
            tableau_url18 = "https://public.tableau.com/views/SexOffensesbyLocation2021/SexOffensesbyLocation2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe18 = f'<iframe src="{tableau_url18}" width="100%" height="525"></iframe>'
            st.markdown(iframe18, unsafe_allow_html=True)

            st.markdown("Sex Offenses By Time")
            tableau_url23 = "https://public.tableau.com/views/SexOffensesbyTime2021/SexOffensesbyTime2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe23 = f'<iframe src="{tableau_url23}" width="100%" height="525"></iframe>'
            st.markdown(iframe23, unsafe_allow_html=True)

        if personal_offense_2021 == "Homicide":

            st.markdown("Homicide By Location")
            tableau_url15 = "https://public.tableau.com/views/HomicideOffensesbyLocation2021/HomicidebyLocation2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe15 = f'<iframe src="{tableau_url15}" width="100%" height="525"></iframe>'
            st.markdown(iframe15, unsafe_allow_html=True)

            st.markdown("Homicide By Time")
            tableau_url20 = "https://public.tableau.com/views/HomicideOffensesbyTime2021/HomicideOffensesbyTime2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe20 = f'<iframe src="{tableau_url20}" width="100%" height="525"></iframe>'
            st.markdown(iframe20, unsafe_allow_html=True)

        if personal_offense_2021 == "Kidnapping":

            st.markdown("Kidnapping By Location")
            tableau_url17 = "https://public.tableau.com/views/KidnappingOffensesbyLocation2021/KidnappingbyLocation2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe17 = f'<iframe src="{tableau_url17}" width="100%" height="525"></iframe>'
            st.markdown(iframe17, unsafe_allow_html=True)

            st.markdown("Kidnapping By Time")
            tableau_url22 = "https://public.tableau.com/views/KidnappingOffensesbyTime2021/KidnappingOffensesbyTime2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe22 = f'<iframe src="{tableau_url22}" width="100%" height="525"></iframe>'
            st.markdown(iframe22, unsafe_allow_html=True)

        if personal_offense_2021 == "Human Trafficking":

            st.markdown("Human Trafficking By Location")
            tableau_url16 = "https://public.tableau.com/views/HumanTraffickingOffensesbyLocation2021/HumanTraffickingbyLocation2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe16 = f'<iframe src="{tableau_url16}" width="100%" height="525"></iframe>'
            st.markdown(iframe16, unsafe_allow_html=True)

            st.markdown("Human Trafficking By Time")
            tableau_url21 = "https://public.tableau.com/views/HumanTraffickingOffensesbyTime2021/HumanTraffickingOffensesbyTime2021?:embed=y&:display_count=yes&:showVizHome=no"
            iframe21 = f'<iframe src="{tableau_url21}" width="100%" height="525"></iframe>'
            st.markdown(iframe21, unsafe_allow_html=True)






elif data_year == "2022":
    # 2022 INFO GOES BELOW--------------

    display = st.selectbox("Select the crime data you would like to look through from the selected year",
                           options=[" ","Personal Offenses", "Property Offenses", "Societal Offenses"])


    #Personal Offenses---------------

    if display == "Personal Offenses":

        sidebar_2022 = st.checkbox("Would You Like to See a Pie Chart of All Personal Offenses?")
        if sidebar_2022:

            # PIE CHART 2022 PERSONAL OFFENSES-----------------------
            st.subheader("Total Personal Offenses throughout Miami Dade County")
            tableau_url3 = "https://public.tableau.com/views/Miami-Dadecrimes2022exceptSimpleandAggravatedAssault/Miami-DadeCrimes2022?:embed=y&:display_count=yes&:showVizHome=no"
            iframe3 = f'<iframe src="{tableau_url3}" width="100%" height="525"></iframe>'
            st.markdown(iframe3, unsafe_allow_html=True)
            # PIE CHART 2022 PERSONAL OFFENSES END--------------------

        personal_offense_2022 = st.selectbox("Select what personal offense you would like to view",
                                        options=[" ", "Assault", "Sex Offenses", "Homicide", "Kidnapping/Abduction"])



        if personal_offense_2022 == "Assault":

            st.markdown("Assault By Location")
            # Embedding the fourth Tableau visualization in an iframe
            tableau_url4 = "https://public.tableau.com/views/AssaultOffensesbyLocation2022/AssaultbyLocation2022?:embed=y&:display_count=yes&:showVizHome=no"
            iframe4 = f'<iframe src="{tableau_url4}" width="100%" height="525"></iframe>'
            st.markdown(iframe4, unsafe_allow_html=True)

            st.markdown("Assault By Time")
            # Embedding the ninth Tableau visualization in an iframe
            tableau_url9 = "https://public.tableau.com/views/AssaultIncidentsbyTime/AssaultOffensesbyTime?:embed=y&:display_count=yes&:showVizHome=no"
            iframe9 = f'<iframe src="{tableau_url9}" width="100%" height="525"></iframe>'
            st.markdown(iframe9, unsafe_allow_html=True)


        if personal_offense_2022 == "Sex Offenses":

            st.markdown("Sex Offenses By Location")
            # Embedding the fifth Tableau visualization in an iframe
            tableau_url5 = "https://public.tableau.com/views/SexOffensesbyLocation2022/SexOffensesbyLocation2022?:embed=y&:display_count=yes&:showVizHome=no"
            iframe5 = f'<iframe src="{tableau_url5}" width="100%" height="525"></iframe>'
            st.markdown(iframe5, unsafe_allow_html=True)

            st.markdown("Sex Offenses By Time")
            # Embedding the thirteenth Tableau visualization in an iframe
            tableau_url13 = "https://public.tableau.com/views/SexOffensesbyTime/SexOffensesbyTime?:embed=y&:display_count=yes&:showVizHome=no"
            iframe13 = f'<iframe src="{tableau_url13}" width="100%" height="525"></iframe>'
            st.markdown(iframe13, unsafe_allow_html=True)

        if personal_offense_2022 == "Homicide":

            st.markdown("Homicide By Location")
            # Embedding the sixth Tableau visualization in an iframe
            tableau_url6 = "https://public.tableau.com/views/HomicideOffensesbyLocation2022/HomicidebyLocation20222?:embed=y&:display_count=yes&:showVizHome=no"
            iframe6 = f'<iframe src="{tableau_url6}" width="100%" height="525"></iframe>'
            st.markdown(iframe6, unsafe_allow_html=True)

            st.markdown("Homicide By Time")
            # Embedding the tenth Tableau visualization in an iframe
            tableau_url10 = "https://public.tableau.com/views/HomicideIncidentsbyTime/HomicideOffensesbyTime?:embed=y&:display_count=yes&:showVizHome=no"
            iframe10 = f'<iframe src="{tableau_url10}" width="100%" height="525"></iframe>'
            st.markdown(iframe10, unsafe_allow_html=True)


        if personal_offense_2022 == "Kidnapping/Abduction":

            st.markdown("Kidnapping By Location")
            # Embedding the seventh Tableau visualization in an iframe
            tableau_url7 = "https://public.tableau.com/views/KidnappingbyLocation2022/KidnappingAbductionbyLocation20223?:embed=y&:display_count=yes&:showVizHome=no"
            iframe7 = f'<iframe src="{tableau_url7}" width="100%" height="525"></iframe>'
            st.markdown(iframe7, unsafe_allow_html=True)

            st.markdown("Kidnapping By Time")
            # Embedding the twelfth Tableau visualization in an iframe
            tableau_url12 = "https://public.tableau.com/views/KidnappingIncidentsbyTime/KidnappingOffensesbyTime?:embed=y&:display_count=yes&:showVizHome=no"
            iframe12 = f'<iframe src="{tableau_url12}" width="100%" height="525"></iframe>'
            st.markdown(iframe12, unsafe_allow_html=True)





    #Property Offenses-------------------------------------
    if display == "Property Offenses":
        st.selectbox("Select what property offense you would like to view",
                     options=[" "])







