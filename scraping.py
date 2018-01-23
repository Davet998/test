#http://pythonhow.com/example.html

import requests
from bs4 import BeautifulSoup
r=requests.get("http://pythonhow.com/example.html", "r")
#print(r)
c = r.content
#print(c)
soup = BeautifulSoup(c, "html.parser")
#print(soup.prettify())
all = soup.find_all("div", {"class":"cities"})
#print(all)
# Just the first entry
#all = soup.find("div", {"class":"cities"})
#print(all)
#Supports indexing
#all = soup.find_all("div", {"class":"cities"})[1]
#print(all)
city = all[0].find_all("h2")[0].text
print(city)
#for item in all:
#    print(item.find_all("h2")[0].text)

#for item in all:
#    print(item.find_all("p")[0].text)
