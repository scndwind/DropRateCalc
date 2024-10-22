import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape the drop table from a given URL
def scrape_monster_drops(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        drop_table = soup.find('table', {'class': 'wikitable'})
        
        if drop_table:
            rows = drop_table.find_all('tr')
            headers = [header.text.strip() for header in rows[0].find_all('th')]
            drops = []
            
            for row in rows[1:]:
                columns = row.find_all('td')
                drop_data = [column.text.strip() for column in columns]
                drops.append(dict(zip(headers, drop_data)))

            return drops
        else:
            return "No drop table found."
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}"

# Streamlit UI
st.title("Monster Drop Table Scraper")

# Input for monster type (you can have more options or a dropdown for other monsters)
monster_url = st.text_input("Enter Monster URL (e.g., https://idleon.wiki/wiki/Green_Mushroom)", 
                            "https://idleon.wiki/wiki/Green_Mushroom")

if st.button("Scrape Drop Table"):
    # Call the scraping function
    drops = scrape_monster_drops(monster_url)
    
    # Display the results
    if isinstance(drops, list):
        st.write("Drop Table:")
        for drop in drops:
            st.write(drop)
    else:
        st.write(drops)  # Display error message if scraping fails
