from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
# from database_connectivity import DataUpdate
import mysql.connector
def DataUpdate(Feedback): 
        mydb = mysql.connector.connect( 
            host="localhost", 
            user="root",  
            passwd="8506", 
            database="rasa_feedback") 
        mycursor = mydb.cursor() 
        #sql = "CREATE TABLE FeedBack_rasa (feedback VARCHAR(255));"
        sql='INSERT INTO feedback_rasa (feedback) VALUES ("{0}");'.format(Feedback) 
        mycursor.execute(sql) 
        print(mycursor.rowcount, "record inserted")
        mydb.commit()
# class ActionHelloWorld1(Action):

#     def name(self) -> Text:
#         return "action_LastName"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(response="utter_LastName")

#         return [SlotSet('firstN',tracker.latest_message['text'])]

class ActionHelloWorld3(Action):

    def name(self) -> Text:
        return "action_Feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_Feedback")

        return [SlotSet('feedback',tracker.latest_message['text'])]

# class ActionHelloWorld2(Action):

#     def name(self) -> Text:
#         return "action_accept"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         print("indide accept")
#         dispatcher.utter_message(response="utter_accept")
    
#         return [SlotSet('lastN',tracker.latest_message['text'])]

class Actionstoredatabase(Action):

    def name(self) -> Text:
        return "action_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # fn= tracker.get_slot("firstN")
        # ln=tracker.get_slot("lastN")
        val= tracker.get_slot("feedback")
        DataUpdate(tracker.get_slot("feedback"))     

        #dispatcher.utter_message("Your first name is {0}\n your last name is {1}\n your feedback is {2}",fn,ln,fd)
        dispatcher.utter_message(response="utter_FeedbackScore",val=val)
        return []

   

