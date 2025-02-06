import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)


#  Fonction qui permet de Scraper les données de voiture à vendre 


def auto_data_scrape(pages):
    df = pd.DataFrame()
    for p in range(1, pages + 1):
        # Instantier l'objet chrome options
        options = webdriver.ChromeOptions()
        # définir l'option d'utiliser chrome en mode headless (utiliser afin de lancer le script en background)
        options.add_argument("--headless=new")
        # initialiser l'instance de chrome driver en mode headless
        driver = webdriver.Chrome(options=options)

        # obtenir l'url
        driver.get(f'https://dakar-auto.com/senegal/voitures-4?&page={p}')
        # trouver les containers
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listings-cards__list-item mb-md-3 mb-3']")
        
        data = []
        for container in containers:
            try:
                marque_annee = container.find_element(By.CLASS_NAME, 'listing-card__header__title.mb-md-2.mb-0').find_element(By.TAG_NAME, 'a').text
                prix = container.find_element(By.CLASS_NAME, 'listing-card__header__price.font-weight-bold.text-uppercase.mb-0').text.replace("F CFA", "")
                adresse = container.find_element(By.CLASS_NAME, 'col-12.entry-zone-address').text
                kilometrage = container.find_element(By.CSS_SELECTOR, 'ul li.listing-card__attribute.list-inline-item:nth-child(2)').text.replace("km", "")
                boite_vitesse = container.find_element(By.CSS_SELECTOR, 'ul li.listing-card__attribute.list-inline-item:nth-child(3)').text
                carburant = container.find_element(By.CSS_SELECTOR, 'ul li.listing-card__attribute.list-inline-item:nth-child(4)').text
                proprietaire = container.find_element(By.CLASS_NAME, 'time-author.m-0').text.replace("Par", "")
                
                dic = {
                    "marque_annee": marque_annee,
                    "prix": prix,
                    "adresse": adresse,
                    "kilometrage": kilometrage,
                    "boite_vitesse": boite_vitesse,
                    "carburant": carburant,
                    "proprietaire": proprietaire
                }
                data.append(dic)
            except:
                pass
        
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
        driver.quit()
    
    #df.to_csv('auto_data_scraped_by_selenium.csv', index=False, header=True)
    return df




# Fonction qui permet de Scraper les données de scooters

def scooters_data_scrape(pages):
    df = pd.DataFrame()
    for p in range(1, pages + 1):
        # Instantier l'objet chrome options
        options = webdriver.ChromeOptions()
        # définir l'option d'utiliser chrome en mode headless (utiliser afin de lancer le script en background)
        options.add_argument("--headless=new")
        # initialiser l'instance de chrome driver en mode headless
        driver = webdriver.Chrome(options=options)

        # obtenir l'url
        driver.get(f'https://dakar-auto.com/senegal/motos-and-scooters-3?&page={p}')
        # trouver les containers
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listings-cards__list-item mb-md-3 mb-3']")
        
        data = []
        for container in containers:
            try:
                marque_annee = container.find_element(By.CLASS_NAME, 'listing-card__header__title.mb-md-2.mb-0').find_element(By.TAG_NAME, 'a').text
                prix = container.find_element(By.CLASS_NAME, 'listing-card__header__price.font-weight-bold.text-uppercase.mb-0').text.replace("F CFA", "")
                adresse = container.find_element(By.CLASS_NAME, 'col-12.entry-zone-address').text
                kilometrage = container.find_element(By.CSS_SELECTOR, 'ul li.listing-card__attribute.list-inline-item:nth-child(2)').text.replace("km", "")
                proprietaire = container.find_element(By.CLASS_NAME, 'time-author.m-0').text.replace("Par", "")
                
                dic = {
                    "marque_annee": marque_annee,
                    "prix": prix,
                    "adresse": adresse,
                    "kilometrage": kilometrage,
                    "proprietaire": proprietaire
                }
                data.append(dic)
            except:
                pass
        
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
        driver.quit()
    
    #df.to_csv('auto_data_scraped_by_selenium.csv', index=False, header=True)
    return df





#  Fonction qui permet de Scraper les données de voiture à vendre 


def rented_auto_data_scrape(pages):
    df = pd.DataFrame()
    for p in range(1, pages + 1):
        # Instantier l'objet chrome options
        options = webdriver.ChromeOptions()
        # définir l'option d'utiliser chrome en mode headless (utiliser afin de lancer le script en background)
        options.add_argument("--headless=new")
        # initialiser l'instance de chrome driver en mode headless
        driver = webdriver.Chrome(options=options)

        # obtenir l'url
        driver.get(f'https://dakar-auto.com/senegal/location-de-voitures-19?&page={p}')
        # trouver les containers
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listings-cards__list-item mb-md-3 mb-3']")
        
        data = []
        for container in containers:
            try:
                marque_annee = container.find_element(By.CLASS_NAME, 'listing-card__header__title.mb-md-2.mb-0').find_element(By.TAG_NAME, 'a').text
                prix = container.find_element(By.CLASS_NAME, 'listing-card__header__price.font-weight-bold.text-uppercase.mb-0').text.replace("F CFA", "")
                adresse = container.find_element(By.CLASS_NAME, 'col-12.entry-zone-address').text
                proprietaire = container.find_element(By.CLASS_NAME, 'time-author.m-0').text.replace("Par", "")
                
                dic = {
                    "marque_annee": marque_annee,
                    "prix": prix,
                    "adresse": adresse,
                    "proprietaire": proprietaire
                }
                data.append(dic)
            except:
                pass
        
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
        driver.quit()
    
    return df


