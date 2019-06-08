from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.happier.com/blog/nice-things-to-say-100-compliments")
bsObj = BeautifulSoup(html,"html.parser")

list_elements = bsObj.findAll("ol") #getting the list elements
compliments = []
for list_element in list_elements:
    for i in list_element.findAll("li"):
        compliments.append(i.text)
