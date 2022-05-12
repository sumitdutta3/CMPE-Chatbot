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

from sre_parse import State
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#import sys
#sys.path.append('C:\Omkar\SJSU_Notes\AI&DataEngineering\ChatBot\actions')
#from fake_abc_api import demograph

import requests 

def demograph(state):
    URL = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=2019"
    r = requests.get(url = URL) 
    data = r.json() 
    #ui=input("enter state:")
    l=[]
    flag=False
    for i in data['data']:
        if(i['State']==state):
            l.append(i)
            print(i)
            flag=True
            break
    if not flag:
        print("does not exist")
        return None
    return l

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_demograph_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        state=tracker.latest_message['text']
        temp=demograph(state)[0]['Population']
        dispatcher.utter_message(response="utter_popu",temp=temp)

        return []



