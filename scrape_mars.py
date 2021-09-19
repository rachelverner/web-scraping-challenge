from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests


def scrape(): 
    #Mars News
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.title.text
    news_title = soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_='article_teaser_body').text

    dictionary = {'1':{'news_title': news_title},'2':{'news_p': news_p}}

#Mars Images
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    image_url = "https://spaceimages-mars.com/"
    browser.visit(image_url)

    html_img = browser.html
    soup = BeautifulSoup(html_img, 'html.parser')

    for item in soup.find_all('img', class_="headerimage fade-in"):
        print(item['src'])   
    
    mars_pic=item['src']

    main_url = 'https://spaceimages-mars.com/'

    featured_image_url = main_url + mars_pic       
    dictionary['3']={}
    dictionary['3']['link'] = featured_image_url

    #Mars Facts
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    table = pd.read_html(facts_url)
    facts_df=table[0]
    facts_df.columns = ["Description","Mars","Earth"]
    facts_df=facts_df.set_index(["Description"])
    facts_df=facts_df.drop(["Mars - Earth Comparison"])   

    mars_facts = facts_df.to_dict('index')
    dictionary['4']={}
    dictionary['4']['table'] = mars_facts

    #Hemisphere Pics
    first_image = {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/cerberus_enhanced.tif"}
    second_image = {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced.tif"}
    third_image = {"title": "Syrtis Major", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced.tif"}
    fourth_image = {"title": "Valles Marineris", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced.tif"}

    # main dictionary - add 5-8 elements
    dictionary['5']={}
    dictionary['5']['1'] = {}
    dictionary['5']['2'] = {}
    dictionary['5']['3'] = {}
    dictionary['5']['4'] = {}
    dictionary['5']['1'] = first_image
    dictionary['5']['2'] = second_image
    dictionary['5']['3'] = third_image
    dictionary['5']['4'] = fourth_image


    return dictionary

