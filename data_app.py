import streamlit as st
import pandas as pd
import fonctions as fn






# Sidebar menu
st.sidebar.title("User Input Features")
page_indexes = st.sidebar.selectbox("page indexes", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

option = st.sidebar.selectbox("options", ["Scrape data using selenium", "Download scraped data", "Dashbord of the data", "Fill the form"])

#data1, data2, data3 = load_data()

# Display selected option
if option == "Scrape data using selenium" :
    st.title("Scrape data using selenium")
    dataframes = fn.auto_data_scrape(page_indexes)
    fn.load_(dataframes, ' Darkar Auto ', '1')
elif option == "Download scraped data":
    #st.title("Dakar Auto")
    st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)

    st.markdown("""
    This app allows you to download scraped data on auto from dakar-auto.com,  
    * **Python libraries:** base64, pandas, streamlit
    * **Data source:** [dakar-auto](https://dakar-auto.com/senegal/voitures-4 ).
    """)

    # définir quelques styles liés aux box
    st.markdown('''<style> .stButton>button {
        font-size: 12px;
        height: 3em;
        width: 25em;
    }</style>''', unsafe_allow_html=True)
    # Charger les données 
    fn.load_(pd.read_csv('data/web_scraper/raw/dakar_auto.csv'), ' Darkar Auto ', '1')
    fn.load_(pd.read_csv('data/web_scraper/raw/scooters.csv'), 'Scooters', '2')
    fn.load_(pd.read_csv('data/web_scraper/raw/voitures_location.csv'), 'Voitures de  locations', '3')
    

    #st.write(data1)
elif option == "Dashbord of the data":
    st.title("Dashbord of the data")
    #st.write(data2)
elif option == "Fill the form":
    st.title("Fill the form")
    st.markdown("""
        <iframe src="https://ee.kobotoolbox.org/i/gWcKxzLO" width="800" height="800"></iframe>
    """, unsafe_allow_html=True)

    
    
    #st.write(data3)





          




 


