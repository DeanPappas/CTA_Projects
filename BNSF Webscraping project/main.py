import datetime as dt
import requests
import json
from bs4 import BeautifulSoup

current_unix_time = dt.datetime.now().timestamp()
# unix_departure_times = []
# converted_departure_times = []
train_departures = {}
train_arrivals = {}

starting_station = input("Leaving from: ")
arrival_station = input("Heading to: ")

aurora_to_union_url = (f"https://www.metra.com/schedules?line=BNSF&orig=CUS&dest=AURORA&time={current_unix_time}"
                       f"&allstops=0")

BNSF_STOPS = ["CUS", "HALSTED", "BNWESTERN", "CICERO", "LAVERGNE", "BERWYN", "HARLEM", "RIVERSIDE", "HOLLYWOOD",
              "BROOKFIELD", "CONGRESSPK", "LAGRANGE", "STONEAVE", "WESTSPRING", "HIGHLANDS", "HINSDALE", "WHINSDALE",
              "CLARNDNHIL", "WESTMONT", "FAIRVIEWDG", "MAINST-DG", "BELMONT", "LISLE", "NAPERVILLE", "ROUTE59",
              "AURORA"]

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}
# response = requests.get(union_to_aurora_url, headers=headers)
#
# soup = BeautifulSoup(response.content, 'html.parser')
# data_text = soup.find("script", {"type": "application/json"}).text
# data = json.loads(data_text)
# with open("data.json", "w") as f:
#     json.dump(data["schedule"], f)
# print(data["schedule"])
with (open("data.json", "r") as f):
    data = json.load(f)
    for x in data:
        departure_time = dt.datetime.fromtimestamp(int(data[x]["departureTime"])).strftime("%H:%M:%S")
        arrival_time = dt.datetime.fromtimestamp(int(data[x]["stops"][BNSF_STOPS[24]]["arrivalTimestamp"])).strftime("%H:%M:%S")
        train_departures.update({data[x]["trainNumber"]:[departure_time, arrival_time]})

for x in train_departures:
    print(f"Train: {x} Departure Time: {train_departures[x][0]} Arrival Time: {train_departures[x][1]}")
