from urllib.request import urlopen
from bs4 import BeautifulSoup
import unidecode #to remove the accents

input_city = input("HOLA: ")
city = unidecode.unidecode(input_city)

#Fun fact: it will show the weather forecast for Budapest if it's an unknown city
html = urlopen("https://www.idokep.hu/elorejelzes/{0}".format(city))
page = BeautifulSoup(html, "html.parser")

for item in page.find_all("div", attrs = {"class": "oszlop"}):
    if item.find("div", attrs = {"class": "ora"}) != None:
        hr = item.find("div", attrs = {"class": "ora"})
        weather = item.find("div", attrs = {"class": "buborek-text"})
        temperature = item.find("div", attrs = {"class": "hoerzet"})
        warning_sth = item.find("strong", attrs = {"class": "csapadek-text"})
        rain_probability = item.find("p", attrs = {"class": "valoszinuseg"})
        if rain_probability == None:
            if warning_sth == None:
                print("{0} óra: {1} fok, {2}. Nem várható csapadék.".format(hr.text[:-1],temperature.text,weather.text))
            else:
                print("{0} óra: {1} fok, {2}. {3}".format(hr.text[:-1],temperature.text,weather.text, warning_sth.text))
        else:
            print("{0} óra: {1} fok, {2}. Csapadék: {3}, {4}".format(hr.text[:-1],temperature.text,weather.text,warning_sth.text,rain_probability.text))
        print()
