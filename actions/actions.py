# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from weather import Weather
import requests

def Weather(city):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    #city = input('Enter the City Name: ')
    url = api_address + city
    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    print("Weather is {0} Temperature is minimum {1} Celcius and Maximum is {2} Celcius".format(json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-272)))
    return format_add

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_weather_api"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          city = tracker.latest_message['text']
          temp = int(Weather(city)['temp']-273)
          #temp = Weather(city)
          #dispatcher.utter_template("utter_temp",tracker,temp=temp)
          dispatcher.utter_message(response="utter_temp",temp=temp)
          return []
