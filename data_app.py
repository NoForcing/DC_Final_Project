import streamlit as st
import pandas as pd
import fonctions as fn
import seaborn as sns
import matplotlib.pyplot as plt






# Sidebar menu
st.sidebar.title("User Input Features")
page_indexes = st.sidebar.selectbox("page indexes", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

option = st.sidebar.selectbox("options", ["Scrape data using Selenium","Scrape data using Beautifulsoup" ,"Download scraped data", "Dashbord of the data", "Fill the form"])


# Display selected option
if option == "Scrape data using Selenium" :
    st.title("Scrape data using selenium")

    if st.button('Scrape Auto Data'):
        dataframe = fn.auto_data_scrape(page_indexes)
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)
    
    
    if st.button('Scrape Scooter Data'):
        dataframe=fn.scooters_data_scrape(page_indexes)
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

    if st.button('Scrape Rental Car Data'):
        dataframe=fn.rented_auto_data_scrape(page_indexes)
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)


elif option == "Scrape data using Beautifulsoup" :
    st.title("Scrape data using beautifulsoup")

    if st.button('Scrape Auto Data'):
        dataframe = fn.bs4_auto_data_scrape(page_indexes)
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)
    
    
    if st.button('Scrape Scooter Data'):
        dataframe=fn.bs4_scooters_data_scrape(page_indexes)
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

    if st.button('Scrape Rental Car Data'):
        dataframe=fn.bs4_rented_auto_data_scrape(page_indexes)
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

elif option == "Download scraped data":
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
    df=pd.read_csv('data/auto_data_cleaned.csv')
    top_marques = df['marque'].value_counts().nlargest(5).reset_index()
    
    # Diagramme à barres
    plt.figure(figsize=(8, 5))
    sns.barplot(data=top_marques, x='marque',y='count', hue='marque',palette='viridis')
    plt.title("Top 5 des marques les plus vendues")
    plt.xlabel("Marque")
    plt.show()
    fig = sns.pairplot(data=df)
    #st.pyplot(fig)
elif option == "Fill the form":
    st.title("Fill the form")
    st.markdown("""
        <iframe src="https://ee.kobotoolbox.org/i/gWcKxzLO" width="800" height="800"></iframe>
    """, unsafe_allow_html=True)

    
    





          




 


