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

   #Hemispheres
    mars_hemispheres_urls = ("https://marshemispheres.com/")
    cerberus_url = ("https://marshemispheres.com/cerberus.html")
    response = requests.get(cerberus_url)
    c_soup = BeautifulSoup(response.text, 'html.parser')
    cerberus_soup = c_soup.find_all('div', class_="wide-image-wrapper")
    for img in cerberus_soup:
        pic = img.find('li')
        c_img = pic.find('a')['href']
    cerberus_url=mars_hemispheres_urls + c_img

    schiaparelli_url = ("https://marshemispheres.com/schiaparelli.html")
    response = requests.get(schiaparelli_url)
    s_soup = BeautifulSoup(response.text, 'html.parser')

    schiaparelli_soup = s_soup.find_all('div', class_="wide-image-wrapper")

    for img in schiaparelli_soup:
        pic = img.find('li')
        s_img = pic.find('a')['href']
    schiaparelli_url=mars_hemispheres_urls + s_img

    syrtis_url = ("https://marshemispheres.com/syrtis.html")
    response = requests.get(syrtis_url)
    syrtis_soup = BeautifulSoup(response.text, 'html.parser')

    syrtis_soup = syrtis_soup.find_all('div', class_="wide-image-wrapper")

    for img in syrtis_soup:
        pic = img.find('li')
        syrtis_img = pic.find('a')['href']
    syrtis_url=mars_hemispheres_urls + syrtis_img

    valles_url = ("https://marshemispheres.com/valles.html")
    response = requests.get(valles_url)
    valles_soup = BeautifulSoup(response.text, 'html.parser')

    valles_soup = valles_soup.find_all('div', class_="wide-image-wrapper")

    for img in valles_soup:
        pic = img.find('li')
        valles_img = pic.find('a')['href']
    valles_url=mars_hemispheres_urls + valles_img

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "valles_url"},
    {"title": "Cerberus Hemisphere", "img_url": "cerberus_url"},
    {"title": "Schiaparelli Hemisphere", "img_url": "schiparelli_url"},
    {"title": "Syrtis Major Hemisphere", "img_url": "syrtis_url"},
]

    dictionary["5"] = hemisphere_image_urls
    return dictionary

