from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.drodd.com/html7/silly-nicknames.html")
bsObj = BeautifulSoup(html,"html.parser")

list_elements = bsObj.find("ul").findAll("li") #getting the list elements
names = []

#there are nested tags and we only want the text so it has to be stripped from
#those other tags
for list_element in list_elements:
    for tag_content in list_element:
        names.append(tag_content)
        break #so we only get the text (first tag_content)
