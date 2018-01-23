#Scraping Pt2
import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.century21.com/real-estate/new-york/LSNY")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all = soup.find_all("div", {"class":"property-card-primary-info"})#[0]
#print(all)
#beds = <div class="property-beds"><strong>
#baths = <div class="property-baths"><strong>
#sqft = <div class="property-sqft"><strong>
#city = <div class="property-city">

#beds = all.find_all("div",{"class":"property-beds"})[0].text.replace("\n","")
#print(beds)
#baths = all.find_all("div",{"class":"property-baths"})[0].text.replace("\n","")
#print(baths)
#sqft = all.find_all("div",{"class":"property-sqft"})[0].text.replace("\n","")
#print(sqft)
#city = all.find_all("div",{"class":"property-city"})[0].text.replace("\n","")
#print(city.lstrip(" "))
#price = all.find_all("a",{"class":"listing-price"})[0].text.replace("\n","").replace(" ","")
#print(price)

for item in all:
    price = item.find_all("a",{"class":"listing-price"})[0].text.replace("\n","").replace(" ","")
    print(price)
    
