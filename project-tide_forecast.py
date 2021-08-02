import requests
from bs4 import BeautifulSoup
import csv
import html5lib

def main():
    URL = "https://tide-forecast.com/locations/Calcutta-Garden-Reach-India/tides/latest"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    tide_forecast = soup.find(class_="tide-day-tides")

    count = 0
    for elem1 in tide_forecast.stripped_strings:
        print(elem1)
        count += 1
        if(count>=4 and count%4==0):
            print("\n")




if __name__ == "__main__":
    main()