from urllib.request import urlopen
from bs4 import BeautifulSoup

#INFO: a scraper to get all the undergrad n postgrad subjects taught at Uni of Glasgow in 2020

def course_scraper(url):
    courses = []
    html = urlopen(url)
    bs_obj = BeautifulSoup(html,"html.parser")
    for item in bs_obj.body("li"):
        if "data-subject" in item.attrs:
            if(item["data-subject"] != "[]"):
                course = item.get_text()
                courses.append(course)

    return courses

def merge(list1, list2):
    merged_list = []
    list1_index = 0
    list2_index = 0
    list1_length = len(list1)
    list2_length = len(list2)

    while(list1_index < list1_length and list2_index < list2_length):
        if(list1[list1_index] < list2[list2_index]):
            merged_list.append(list1[list1_index])
            list1_index += 1

        else:
            merged_list.append(list2[list2_index])
            list2_index += 1

    while(list1_index < list1_length):
        merged_list.append(list1[list1_index])
        list1_index += 1

    while(list2_index < list2_length):
        merged_list.append(list2[list2_index])
        list2_index += 1

    return merged_list

undergrad = course_scraper("https://www.gla.ac.uk/undergraduate/2020/")
postgrad = course_scraper("https://www.gla.ac.uk/postgraduate/taught/")

course_list = merge(undergrad, postgrad)
with open('courses.txt', 'w') as file:
    for course in course_list:
        file.write(course + '\n')
