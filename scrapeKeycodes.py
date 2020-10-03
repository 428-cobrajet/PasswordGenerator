from bs4 import BeautifulSoup
from requests import get
from csv import DictWriter
# scrapeKeycodes.py to recreate keycodes.csv

def scrapeHTML():
    # Used to scrape ascii HTML from site
    url = "https://asciichart.com/"
    page = get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    HTML = soup.prettify()
    return HTML

def parseHTML(HTML):
    # Reads keycodes and returns a 2d array of char:keycode dictionaries
    keycodes = []
    soup = BeautifulSoup(HTML, "html.parser")
    data = soup.findAll("td")

    # A dictionary is created for each keycode+char pair
    for i in range(0, len(data)-1, 2):
        dict = {}
        # Whitespace and newline chars are removed
        keycode = ((str(data[i].text)).replace(" ", "")).replace("\n", "")
        char = ((str(data[i+1].text)).replace(" ", "")).replace("\n", "")
        dict["keycode"] = keycode
        dict["char"] = char
        keycodes.append(dict)
    return keycodes

def writeToCSV(data):
    # Writes scraped dictionary to keycodes.csv
    fields = ["char", "keycode"]
    try:
        with open("keycodes.csv", "w", newline="") as csvfile:
            writer = DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for i in data:
                writer.writerow(i)
        print("CSV wrote successfully")

    except Exception as e:
        print("Could not write to csv: ", e)

HTML = scrapeHTML()
keycodes = parseHTML(HTML)
writeToCSV(keycodes)
