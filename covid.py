from bs4 import BeautifulSoup
from urllib.request import urlopen
import re, csv

html = urlopen("https://koronavirus.gov.hu/elhunytak")
soup = BeautifulSoup(html, 'html.parser')

last_page_href = soup.find("li", class_='pager-last').a['href']
last_page_string = ''.join([str(c) for c in last_page_href])
last_page = int(re.search("[0-9]+", last_page_string)[0]) + 1

patients = []

for page in range(0,last_page):
    url = "https://koronavirus.gov.hu/elhunytak?page=" + str(page)
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("td")

    for i in range(0,len(table)-3,4):
        patient = []
        
        for j in range(i,i+4):
            patient_data = str(table[j].contents[0]).strip()
            patient.append(patient_data)

        patients.append(patient)

with open('covid.txt', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(patients)
