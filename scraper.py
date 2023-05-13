from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver


start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/ssony/Downloads/PRO-C127-Student-Boilerplate-Code-main/PRO-C127-Student-Boilerplate-Code-main/chromedriver.exe")
time.sleep(10)
scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    
    bright_star_table = soup.find_all("table",attrs={"class","wikitable"})
    table_body=bright_star_table.find_all('tbody')
    table_rows=table_body.find_all('tr')
    for i in table_rows:
        table_cols=i.find_all('td')
        print(table_cols)
        temp_list=[]

        for col_data in table_cols:
            #print(col_data.text)
            data=col_data.text.strip()
            print(data)
            temp_list.append(data)
        scraped_data.append(temp_list)


stars_data=[]
for j in range(0,len(scraped_data)):
    stars_name=scraped_data[j][1]
    distance=scraped_data[j][3]
    mass=scraped_data[j][5]
    radius=scraped_data[j][6]
    lum=scraped_data[j][7]

    required_data=[stars_name,distance,mass,radius,lum]
    stars_data.append(required_data)

headers = ["stars_name","distance","mass","radius","lum"]
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv('scrape_Data.csv',index=True,index_label="id")




