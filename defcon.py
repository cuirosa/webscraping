from urllib.request import urlopen
from bs4 import BeautifulSoup

#og time, title, link
def talk_scraper(url):
    talks = []
    html = urlopen(url)
    bs_obj = BeautifulSoup(html,"html.parser")
    rows = bs_obj.find_all("ul", {"class":"scheduleRow"})
    for item in rows:
        talk = []
        ogTime = item.p.get_text().strip()
        talkName = item.h4.get_text().strip()
        if("Bytes In Disguise" in item.h4.get_text()):
            talkName = "Bytes In Disguise"
        link = "https://www.defcon.org/html/defcon-safemode/" + item.h4.a['href'].strip()
        talk.append(ogTime)
        talk.append(talkName)
        talk.append(link)
        talks.append(talk)

    return talks

talks = talk_scraper("https://www.defcon.org/html/defcon-safemode/dc-safemode-schedule.html")

with open('talks.txt', 'w') as file:
    for talk in talks:
        for item in talk:
            file.write(item + '*')
        file.write('\n')
