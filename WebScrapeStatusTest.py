import requests
from bs4 import BeautifulSoup

#IDK if it's better to add a class for each result
#class RowResult:
#    def __init__(self, title, location, date_posted):
#        self.title = title
#        self.location = location
#        self.date_posted = date_posted



job_title = input("Enter job title: ")
title_fixed = job_title.replace(" ", "+")
location = input("Enter city and state: ")
city, state = location.split(' ')

# A fix for 'C#'
if "#" in title_fixed:
    title_fixed = title_fixed.replace("#", "%23")
    print("00000000000000000000000000{}".format(title_fixed))

indeed_url = "https://www.indeed.com/jobs?q={}&l={}%2C+{}&sort=date".format(title_fixed, city, state)

page = requests.get(indeed_url)
soup = BeautifulSoup(page.text, "html.parser")

def get_titles(soup):
    titles = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            titles.append(a["title"])
    return titles

def get_locations(soup): 
    locations = []
    for span in soup.find_all(name="span", attrs={"class": "location"}):
        locations.append(span.text)
    return locations

def get_dates(soup):
    dates = []
    for span in soup.find_all(name="span", attrs={"class":"date"}):
        dates.append(span.text)
    return dates

def display_results(titles, locations, dates):
    for title, location, date in zip(titles, locations, dates):
        print(line)
        print("TITLE: {}".format(title))
        print("Location: {}".format(location))
        print("Date Posted: {}".format(date))

line = "- - - - - - - - - - - - - - - - - - - - - - - - - - - -"

print(line)
print("SEARCH RESULTS: \"{}\" in \"{}, {}\"".format(job_title, city, state))
display_results(get_titles(soup), get_locations(soup), get_dates(soup))