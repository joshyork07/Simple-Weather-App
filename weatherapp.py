import requests as rq
import os
from pprint import pprint
from dotenv import load_dotenv

# Get weather data based on zipcode
load_dotenv()

while True:
    userlocation = input(
        "Enter area zipcode to see temperature: "
    )
    if userlocation.isdigit():
        if len(userlocation) !=  5:
            pprint("Please enter a valid 5 digit zipcode.")
            continue
        else:
            weather = rq.get(
                "https://weatherapi-com.p.rapidapi.com/current.json",
                params={"q": {userlocation}},
                headers={
                    "X-RapidAPI-Key": os.getenv("API_KEY"),
                    "X-RapidAPI-Host": os.getenv("WEATHER_HOST"),
                },
            )
            data = weather.json()
            pprint(f"The Current temperature in {data['location']['name']}, {data['location']['region']} is {data['current']['temp_f']}F"
                   )
    else:
        pprint("Please enter a valid 5 digit Zipcode")

  
