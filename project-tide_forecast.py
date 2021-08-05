import requests
from bs4 import BeautifulSoup
import tkinter as tk


def main():
    URL = "https://tide-forecast.com/locations/Calcutta-Garden-Reach-India/tides/latest"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    tide_forecast = soup.find(class_="tide-day-tides")

    count = 0
    arr = [None]*25

    root = tk.Tk()

    root.geometry("512x300")

    root.minsize(256, 128)
    root.maxsize(1024, 512)

    photo = tk.PhotoImage(file="tide_forecast.png")

    for elem1 in tide_forecast.stripped_strings:
        arr[count] = elem1
        count += 1
        if(count >= 4 and count % 4 == 0):
            pass

    vadim_label = tk.Label(
        root, text=f"{arr[4]} = {arr[5]}\n{arr[9]} = {arr[10]}\n{arr[14]} = {arr[15]}\n{arr[19]} = {arr[20]}", image=photo, compound="top")
    vadim_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
