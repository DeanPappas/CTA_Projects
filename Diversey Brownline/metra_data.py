import requests
import os

parameters = {
    "key": "Request API key here: https://www.transitchicago.com/developers/traintrackerapply/",
    "mapid": 40530,
    "outputType": "JSON",
    "rt": "brn"
}

response = requests.get("http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx", params=parameters)
response.raise_for_status()
try:
    stop_eta_data = response.json()["ctatt"]["eta"]
except KeyError:
    stop_eta_data = []

kimball_stops = []
loop_stops = []

def init_info(stop_data):
    for x in stop_data:
        if x["destNm"] == "Kimball":
            time_str = x["arrT"].split("T")[1] # Get time in "HH:MM:SS" 24hr format
            time_tuple = time_str.split(":") # Split time_str into a tuple ("HH","MM","SS")
            current_hour = int(time_tuple[0]) # Convert "HH" into int
            if current_hour > 12: # Check if current_hour is > 13
                standard_hour = current_hour - 12 # Subtract 12 to convert hour to standard time (Not using AM/PM)
                time_tuple[0] = str(standard_hour) # Replacing time_tuple "HH" after converting back to str
                time_str = ":".join(time_tuple) # Merge time_tuple back to single string and set to time_str
                kimball_stops.append(time_str) # Appending converted time to kimball_stops
            else:
                kimball_stops.append(time_str)
        else:
            time_str = x["arrT"].split("T")[1]
            time_tuple = time_str.split(":")
            current_hour = int(time_tuple[0])
            if current_hour > 12:
                standard_hour = current_hour - 12
                time_tuple[0] = str(standard_hour)
                time_str = ":".join(time_tuple)
                loop_stops.append(time_str)
            else:
                loop_stops.append(x["arrT"].split("T")[1])

def refresh_data():
    kimball_stops.clear()
    loop_stops.clear()
    new_response = requests.get("http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx", params=parameters)
    new_response.raise_for_status()
    try:
        refreshed_stop_data = new_response.json()["ctatt"]["eta"]
    except KeyError:
        refreshed_stop_data = []

    init_info(refreshed_stop_data)

init_info(stop_eta_data)