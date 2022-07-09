from time import strftime
import requests
from datetime import datetime
from tabulate import tabulate
import pyttsx3
from decouple import config



engine =pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate", 175)

def speech(txt):
    
    engine.say(txt)
    engine.runAndWait()

def weath():
    while True:
        API_KEY = ('bd9032b1b36cc1642b3c5528c1949c96')
        location = input("Enter The Name Of The City/country : ")
        weather = "https://api.openweathermap.org/data/2.5/weather?q="+ location +"&appid="+API_KEY
        api_link = requests.get(weather)
        api_data = api_link.json() 

        if api_data['cod'] == '404':
            print("Invalid City: '{}', please check the city name".format(location))
            speech("Invalid City: '{}', please check the city name".format(location))
        else:
            temp_city = ((api_data['main']['temp'])-273.15)
            weathe_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_speed = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y || %I:%M:%S: %p")
            tabel_heading = [f"Live Weather Status For {location.upper()} || {date_time}", "Reports"]
            mydata = [
                [f"Current Temperature In - {location.upper()}", f"{temp_city:.2f}"],
                [f"Current Weather Description In - {location.upper()}", f"{weathe_desc}"],
	            [f"Current Humidity In - {location.upper()}", f"{hmdt}'%'"],
	            [f"Current Wind Speed In - {location.upper()}", f"{wind_speed}'kmph'"]
            ]
            print(tabulate(mydata,headers=tabel_heading, tablefmt="grid"))
            speech(f"current temperature in {location} : {temp_city:.2f}")    
            speech(f"current weather discription in {location} {weathe_desc}")       
            speech(f"current humidity in {location} {hmdt} percentage")        
            speech(f"current wind speed in {location} {wind_speed} kilo meter per hour")


            quest = input("Do You Want To Continue....??? : ")
            if quest == 'y' or quest == 'yes':
                print("Thank You For Using Again The Ovila Live Weather Detector !!!")
                speech("thank you for using again the olivia live weather detector")
            else:
                print("The Olivia Live Weather Detector Is Now Stoped !!!")
                speech("the olivia live weather detector is now stoped")
                break



